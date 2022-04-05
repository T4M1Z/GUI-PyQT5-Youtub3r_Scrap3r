###################################################################################
##                                                                               ##
## BY: ANDREA TAMI                                                               ##
## PROJECT MADE WITH: Qt Designer and PyQT5                                      ##
## V: 1.0.0                                                                      ##
##                                                                               ##
## This project can be used freely for all uses, as long as they maintain the    ##
## respective credits only in the Python scripts, any information in the visual  ##
## interface (GUI) can be modified without any implication.                      ##
##                                                                               ##
###################################################################################

import os
import sys
from grpc import Channel
import requests
from matplotlib import style
from modules import *
# from PyQt5.QtChart import QCandlestickSeries, QCandlestickSet, QChart, QChartView, QLineSeries
from PyQt5.QtWidgets import QFileDialog, QFrame, QGraphicsOpacityEffect, QHBoxLayout, QLabel, QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPainterPath, QPalette,QMovie, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer, QEasingCurve, pyqtSignal
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QPoint
from scraper_channel.test_db import MongoDB



class MainWindow(QMainWindow):
    # Globals

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ----- MOVE WINDOW ----- #
        def moveWindow(event):
            if UIFunctions.returStatus() == 1:
                cursor = QtGui.QCursor()
                UIFunctions.maximize_restore(self, cursor.pos().x(), cursor.pos().y())

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.title_frame.mouseMoveEvent = moveWindow
        # ----------------------- # 


        # ------ FUNCTIONS ------ #
        UIFunctions.uiDefinitions(self)
        # ----------------------- #

        # ------ Settings ------ #
        self.door = False
        self.ui.stop_scraping_btn.hide()
        self.ui.scraping_monitoring_frame.setMaximumHeight(0)
        self.ui.frame.setContentsMargins(2, 2, 10, 10)
        self.ui.label_gif.hide()

        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)


        # ------ Actions ------ #
        self.ui.drag_btn.pressed.connect(self.pressed_window)
        self.ui.cluster_checkBox.toggled.connect(self.enable_cluster)
        self.ui.start_scraping_btn.pressed.connect(self.start_scraping)
        self.ui.stop_scraping_btn.pressed.connect(self.stop_scraping)
        self.ui.test_db_btn.pressed.connect(self.test_connection_db)
        # Loading the GIF
        self.movie = QMovie("ui/icons/loading/loading_circle.gif")
        self.ui.label_gif.setMovie(self.movie)

        self.show()
        # ------------------------ #
        
    ########################################################################
    ## ----- Grip window Move ----- ##
    def mouseMoveEvent(self, event): # Mouse coordinate when Btn_drag pressed
        if self.door:
            self.resize(event.x(), event.y())
    def mouseReleaseEvent(self, event): # Btn_drag released
        self.door = False
    def pressed_window(self): # Btn_drag pressed
        self.door = True
    def mousePressEvent(self, event): # Title_fram pressed for moving window
        self.dragPos = event.globalPos()
    ## ---------------------------- ##
    ########################################################################
    ## ==> END Configuration GUI ##




    ########################################################################
    ## ----- Scraping Settings ----- ##
    # GIF Animation
    def startAnimation(self):
        self.movie.start()
        


    def enable_cluster(self):
        # If you want to use cluster
        if self.ui.cluster_checkBox.isChecked():
            self.ui.cluster_spinBox.setEnabled(True)
        else: 
            self.ui.cluster_spinBox.setEnabled(False)


    def test_connection_db(self):
        self.ui.username_db.setStyleSheet(stylesheet.input_style)
        self.ui.password_db.setStyleSheet(stylesheet.input_style) 

        if not self.ui.username_db.text() or not self.ui.password_db.text():
            self.ui.username_db.setStyleSheet(stylesheet.input_style_error)
            self.ui.password_db.setStyleSheet(stylesheet.input_style_error)

        else:
            ### - Starting QTrhead - ###
            self.serialReaderDatabase = MongoDB(self.ui.username_db.text(), 
                                                self.ui.password_db.text())
            self.serialReaderDatabase.receivedPacketSignal.connect(self.return_status_db)
            self.serialReaderDatabase.start()

            # Start loading GIF
            self.movie.start()
            self.ui.label_gif.show()




    def return_status_db(self, return_status):
        if return_status == "connected":
            self.ui.status_db_connection.setText("ONLINE")
            self.ui.status_db_connection.setStyleSheet(stylesheet.db_online)
            self.serialReaderDatabase.stop()
        else: 
            if "error" in return_status:
                self.ui.username_db.setStyleSheet(stylesheet.input_style_error)
                self.ui.password_db.setStyleSheet(stylesheet.input_style_error)
            self.ui.status_db_connection.setText("Offline")
            self.ui.status_db_connection.setStyleSheet(stylesheet.db_offline)
            self.serialReaderDatabase.stop()

        # Stop loading GIF
        self.movie.stop()
        self.ui.label_gif.hide()


    def start_scraping(self):
        self.reset_user()

        # Cluster state
        cluster = self.ui.cluster_spinBox.value() if self.ui.cluster_spinBox.isEnabled() else False 
        
        # Input URL 
        if not self.ui.url_Input.text():
        # if "https://www.youtube.com/channel" not in self.ui.url_Input.text():
            self.ui.url_Input.setStyleSheet(stylesheet.input_style_error)
        else: 
            self.ui.url_Input.setStyleSheet(stylesheet.input_style)

        # Database Status
        if self.ui.status_db_connection.text() == "OFFLINE":
            self.ui.username_db.setStyleSheet(stylesheet.input_style_error)
            self.ui.password_db.setStyleSheet(stylesheet.input_style_error)
        else:
            self.ui.username_db.setStyleSheet(stylesheet.input_style)
            self.ui.password_db.setStyleSheet(stylesheet.input_style)

        # Final controll
        if self.ui.status_db_connection.text() == "ONLINE" and self.ui.url_Input.styleSheet() != stylesheet.input_style_error:

            self.animation_scraping_settings()
            self.ui.start_scraping_btn.hide()
            self.ui.stop_scraping_btn.show()
            ### - Starting QTrhead - ###
            self.serialReaderChannelScraping = Channel_Scraping(self.ui)
            self.serialReaderChannelScraping.receivedPacketSignal.connect(self.return_data_scraping)
            self.serialReaderChannelScraping.finished.connect(self.insert_data_channel)
            self.serialReaderChannelScraping.start()


    def return_data_scraping(self, packet):
        if "message" in packet.keys():
            print(packet["message"])

        elif "links" in packet.keys():
            print("funziona?")
            for l,t,v,idx in zip(packet["links"], packet["title"], packet["visual"], packet["index"]):
                self.ui.tableWidget.insertRow(idx)
                self.ui.tableWidget.setItem( idx, 0, QTableWidgetItem(str(idx)))
                self.ui.tableWidget.setItem( idx, 1, QTableWidgetItem(l))
                self.ui.tableWidget.setItem( idx, 2, QTableWidgetItem(t))
                self.ui.tableWidget.setItem( idx, 3, QTableWidgetItem(v))

        elif "channel_data" in packet.keys():
            self.ui.stop_scraping_btn.hide()
            self.ui.start_scraping_btn.show()
            self.packet_data = packet["channel_data"]



    def insert_data_channel(self):  
        self.animation_scraping_settings()

        # Deleting previuous selenium widget in the layout
        for i in reversed(range(self.ui.selenium_layout.count())): 
            self.ui.selenium_layout.itemAt(i).widget().setParent(None)

        
        self.ui.stop_scraping_btn.hide()
        self.ui.start_scraping_btn.show()
        
        try:
            self.download_image(self.packet_data["profile_img"])
            # Username
            self.ui.username_channel.setText(self.packet_data["username"])
            # Flag Country
            if self.packet_data["location"] != "":
                self.ui.flag_label.setStyleSheet(stylesheet.flag(str(self.packet_data["location"][:2]).lower())) 
            else: self.ui.flag_label.setStyleSheet(stylesheet.no_flag)
            # Total Video
            self.ui.totVideo_channel.setText(str(self.packet_data["tot_video"])+" Video")
            # Total Views
            self.ui.totViews_channel.setText(self.packet_data["tot_visual"])
            # Subscriber
            self.ui.totSubs_channel.setText(self.packet_data["subs"])
            # Joined Date
            self.ui.joinedDate_channel.setText("Joined on "+self.packet_data["joined_date"])
            # Social
            print(self.packet_data["social"])
            self.ui.social_comboBox.addItems(self.packet_data["social"])
            # Channel Description
            self.ui.description_channel.clear()
            self.ui.description_channel.setText(self.packet_data["channel_desc"])
        except:
            print("Programm stopped without data input")
        


    def stop_scraping(self):
        self.reset_user()
        self.serialReaderChannelScraping.quit()
        self.serialReaderChannelScraping.terminate()
        self.ui.start_scraping_btn.show()
        self.ui.stop_scraping_btn.hide()
        
        for i in reversed(range(self.ui.selenium_layout.count())): 
            self.ui.selenium_layout.itemAt(i).widget().setParent(None)
        
        self.animation_scraping_settings()




    ## ---------------------------- ##
    ##############################################################
    ## ==> END Scraping configuration ##


    def download_image(self, link):
        print(link)
        img_data = requests.get(link).content
        with open('ui/icons/channel/profile_new.jpg', 'wb') as handler:
            handler.write(img_data)

        pixmap = QtGui.QPixmap('ui/icons/channel/profile_new.jpg')
        self.ui.profile_image.setPixmap(pixmap.scaled(134,134))
        self.ui.profile_image.adjustSize()


    def reset_user(self):
        ### CLEAR ###
        self.ui.profile_image.clear()
        self.ui.username_channel.setText("Username")
        self.ui.flag_label.setStyleSheet(stylesheet.no_flag)
        self.ui.totVideo_channel.setText("Total videos")
        self.ui.totViews_channel.setText("Total views")
        self.ui.totSubs_channel.setText("Subscribers")
        self.ui.joinedDate_channel.setText("Joined Date")
        self.ui.social_comboBox.clear()
        self.ui.social_comboBox.addItem("Social")
        self.ui.description_channel.clear()
        self.ui.description_channel.setText("Channel description")




    def animation_scraping_settings(self):
        self.top_panel = QtCore.QPropertyAnimation(self.ui.scraping_setting_frame, b"maximumHeight")
        self.bottom_panel = QtCore.QPropertyAnimation(self.ui.scraping_monitoring_frame, b"maximumHeight")
        group_animation = QParallelAnimationGroup(self)
        
        animation = {self.top_panel:[self.ui.scraping_setting_frame,130,0],
                    self.bottom_panel:[self.ui.scraping_monitoring_frame,300,0]}
        
        for k,v in animation.items():
            if v[0].height() > 0:
                h1, h2 = v[1],v[2]
            else:
                h1, h2 = v[2],v[1]

            k.setDuration(400)
            k.setStartValue(h1)
            k.setEndValue(h2)
            k.start()
            group_animation.addAnimation(k)

        group_animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()

    sys.exit(app.exec_())













