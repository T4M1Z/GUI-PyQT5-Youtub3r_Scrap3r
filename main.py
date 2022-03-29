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
        self.ui.frame.setContentsMargins(2, 2, 10, 10)
        self.ui.label_gif.hide()




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
            self.serialReaderThread = MongoDB(self.ui.username_db.text(), 
                                    self.ui.password_db.text())
            self.serialReaderThread.receivedPacketSignal.connect(self.return_status_db)
            self.serialReaderThread.start()

            # Start loading GIF
            self.movie.start()
            self.ui.label_gif.show()


    # GIF Animation
    def startAnimation(self):
        self.movie.start()


    def return_status_db(self, return_status):
        if return_status == "connected":
            self.ui.status_db_connection.setText("Online")
            self.ui.status_db_connection.setStyleSheet(stylesheet.db_online)
        else: 
            self.ui.status_db_connection.setText("Offline")
            self.ui.status_db_connection.setStyleSheet(stylesheet.db_offline)

        # Stop loading GIF
        self.movie.stop()
        self.ui.label_gif.hide()


    def start_scraping(self):
        # Cluster state
        cluster = self.ui.cluster_spinBox.value() if self.ui.cluster_spinBox.isEnabled() else False 
        
        # Input URL 
        if not self.ui.url_Input.text():
        # if "https://www.youtube.com/channel" not in self.ui.url_Input.text():
            self.ui.url_Input.setStyleSheet(stylesheet.input_style_error)
        else: 
            self.ui.url_Input.setStyleSheet(stylesheet.input_style)

        # Database Status
        if self.ui.status_db_connection.text() == "Offline":
            self.ui.username_db.setStyleSheet(stylesheet.input_style_error)
            self.ui.password_db.setStyleSheet(stylesheet.input_style_error)
        else:
            self.ui.username_db.setStyleSheet(stylesheet.input_style)
            self.ui.password_db.setStyleSheet(stylesheet.input_style)

        # Final controll
        if self.ui.status_db_connection.text() == "Online" and self.ui.url_Input.styleSheet() != stylesheet.input_style_error:
            self.ui.start_scraping_btn.hide()
            self.ui.stop_scraping_btn.show()

            ### - Starting QTrhead - ###
            self.serialReaderThread = Scraping(self.ui.url_Input.text(), 
                                                self.ui.threads_spinBox.value(),
                                                cluster)
            self.serialReaderThread.receivedPacketSignal.connect(self.return_data_scraping)
            self.serialReaderThread.start()

    def stop_scraping(self):
        self.serialReaderThread.stop()
        self.ui.stop_scraping_btn.hide()
        self.ui.start_scraping_btn.show()


    ## ---------------------------- ##
    ########################################################################
    ## ==> END Scraping configuration ##

    def return_data_scraping(self, packet):
        if "message" in packet.keys():
            print(packet["message"])
        if "channel_data" in packet.keys():
            packet_data = packet["channel_data"]
            print( f""" {packet_data["username"]}, 
                        {packet_data["location"]}, 
                        {packet_data["joined_date"]},
                        {packet_data["tot_video"]}, 
                        {packet_data["tot_visual"]}, 
                        {packet_data["subs"]}, 
                        {packet_data["profile_img"]}, 
                        {packet_data["cover_img"]}, 
                        {packet_data["social"]}
                        """)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()

    sys.exit(app.exec_())













