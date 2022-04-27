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
import requests
import webbrowser

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




class MainWindow(QMainWindow):
    # Globals

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ----- WIDGET ------- #
        self.c_panel = CenterPanel()
        self.animation = Animation(self.ui, self.c_panel)
        self.DB_offline = DBOffline()
        self.DB_history_channel = DBHistoryChannel(self.ui)

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
        
        self.ui.btn_combo_box.hide()

        self.ui.loading_gif.hide()
        self.DB_history_channel.ui.refresh_gif.hide()

        self.ui.db_status_layout.addWidget(self.DB_offline)
        self.ui.db_channels_history.addWidget(self.DB_history_channel)

        self.c_panel.ui.right_bottom_frame.hide() # Table widget hide
        self.ui.social_comboBox.setEnabled(False)


        # self.ui.scraping_monitoring_frame.setMaximumHeight(0)
        self.ui.central_panel_layout.addWidget(self.c_panel)
        # self.ui.label_gif.hide()
        
        # Hide monitoring panel
        self.c_panel.ui.scraping_monitoring_frame.setMaximumHeight(0)
        
        # Width of columns in QTable monitoring
        header = self.c_panel.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        item1 = self.c_panel.ui.tableWidget.horizontalHeaderItem(0)
        item1.setForeground(QtGui.QColor(255, 0, 0))
        item1.setBackground(QtGui.QColor(0, 0, 0))  # Black background! does not work!!
        self.c_panel.ui.tableWidget.setHorizontalHeaderItem(0, item1)


        # ------ Actions ------ #
        self.ui.drag_btn.pressed.connect(self.pressed_window)
        self.ui.cluster_checkBox.toggled.connect(self.enable_cluster)
        self.ui.start_scraping_btn.pressed.connect(self.start_scraping)
        self.ui.stop_scraping_btn.pressed.connect(self.stop_scraping)
        self.ui.left_panel_btn.pressed.connect(self.animation.show_left_panel)
        self.ui.btn_combo_box.pressed.connect(self.open_social_url)
        self.ui.db_connect_btn.pressed.connect(self.test_connection_db)
        self.DB_history_channel.ui.refresh_db_btn.pressed.connect(self.refresh_channels_list)

        # self.ui.test_db_btn.pressed.connect(self.test_connection_db)
        
        # Loading the GIF
        self.movie = QMovie("ui/icons/loading/loading_circle_2.gif")
        self.ui.loading_gif.setMovie(self.movie)
        
        # Set left panel Closed
        self.ui.left_panel.setMaximumWidth(0)

        self.lista = []
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


    # Btn open socila url combobox
    def open_social_url(self):
        webbrowser.open(self.ui.social_comboBox.currentText())


    # GIF Animation
    def startAnimation(self):
        self.movie.start()

    ########################################################################
    ## ----- Scraping Settings ----- ##
        
    def enable_cluster(self):
        # If you want to use cluster
        if self.ui.cluster_checkBox.isChecked():
            print("add cluster option")
            self.animation.animation_db_settings_frame()
        else: 
            print("remove cluster option")
            self.animation.animation_db_settings_frame()
            # self.ui.cluster_checkBox.setEnabled(False)


    # ||||||||||||||||||||||||||||||||||||||||||||||||| Da sistemare ||||||||||||||||||||||||||||||||||||||||||||||||| #
    def test_connection_db(self):
        self.ui.db_connection_input.setStyleSheet(stylesheet.input_style) 

        if not self.ui.db_connection_input.text():
            self.ui.db_connection_input.setStyleSheet(stylesheet.input_style_error)
        else:
            ### - Starting QTrhead - ###
            self.serialReaderDatabase = DBConnection(self.ui.db_connection_input.text(), "first_connection")
            self.serialReaderDatabase.receivedPacketSignal.connect(self.return_status_db)
            self.serialReaderDatabase.start()

            # Start loading GIF
            self.movie.start()
            self.ui.loading_gif.show()

    def return_status_db(self, return_status, query):

        if return_status == "first_connection":
            self.ui.db_connection_input.setStyleSheet(stylesheet.input_style)
            # Cleaning previous widget
            self.layout_cleaning(self.DB_history_channel.ui.channel_list_widget)

            # Display History Channels after connected to Database
            FaderWidget(self.ui.stackedWidget.currentWidget(), self.ui.stackedWidget.widget(1))
            self.ui.stackedWidget.setCurrentIndex(1)
            self.animation.animation_db_settings_frame()

            # Fill the history channel with the data inside the database
            for idx, channel in enumerate(query):
                UserWidget = ChannelHistory(idx+1,channel["profile_img"],channel["username"],channel["joined_date"])
                self.DB_history_channel.ui.channel_list_widget.addWidget(UserWidget)

        if return_status == "refresh_channels_list":
            self.layout_cleaning(self.DB_history_channel.ui.channel_list_widget)
            for idx, channel in enumerate(query):
                UserWidget = ChannelHistory(idx+1,channel["profile_img"],channel["username"],channel["joined_date"])
                self.DB_history_channel.ui.channel_list_widget.addWidget(UserWidget)
            print("fine refresh")
                    # Start loading GIF
            self.movie.stop()
            self.DB_history_channel.ui.refresh_gif.hide()
            self.DB_history_channel.ui.refresh_db_btn.show()


        if "error" in return_status:
            self.ui.db_connection_input.setStyleSheet(stylesheet.input_style_error)
            print(f"Error connection: {return_status}")

        self.serialReaderDatabase.stop()

        # Stop loading GIF
        self.movie.stop()
        self.ui.loading_gif.hide()

    def exit_database(self):
        print("ciao sono il main")


    def refresh_channels_list(self):
        # Loading the GIF   
        self.movie = QMovie("ui/icons/loading/loading_circle_16.gif")
        self.DB_history_channel.ui.refresh_db_btn.hide()
        self.DB_history_channel.ui.refresh_gif.setMovie(self.movie)
        self.DB_history_channel.ui.refresh_gif.setScaledContents(True)
        # Start GIF Animation
        self.movie.start()
        self.DB_history_channel.ui.refresh_gif.show()
        ### - Starting QTrhead - ###
        self.serialReaderDatabase = DBConnection(self.ui.db_connection_input.text(), "refresh_channels_list")
        self.serialReaderDatabase.receivedPacketSignal.connect(self.return_status_db)
        self.serialReaderDatabase.start()


    # ||||||||||||||||||||||||||||||||||||||||||||||||| Da sistemare ||||||||||||||||||||||||||||||||||||||||||||||||| #

    def start_scraping(self):

        # Input URL 
        if not self.ui.url_Input.text():
            self.ui.url_Input.setStyleSheet(stylesheet.input_style_error)
        else: 
            self.ui.url_Input.setStyleSheet(stylesheet.input_style)


        # Final controll
        if self.ui.url_Input.styleSheet() != stylesheet.input_style_error:
            self.reset_user()

            # Top panel animation
            self.animation.animation_top_panel()

            if self.c_panel.ui.central_panel_frame.height() == 0:
                self.animation.animation_central_panel("resize")
                self.animation.animation_bottom_left_panel("resize")
                self.animation.animation_bottom_panel("resize")
            else:
                self.animation.animation_bottom_panel()

            self.ui.start_scraping_btn.hide()
            self.ui.stop_scraping_btn.show()

            # Clear links in the QWidget Tabel
            self.c_panel.ui.tableWidget.clearContents()

            ### - Starting QTrhead - ###
            self.serialReaderChannelScraping = Channel_Scraping(self.ui, self.c_panel.ui)
            self.serialReaderChannelScraping.receivedPacketSignal.connect(self.return_data_scraping)
            # When signal finish, start inserting data
            # self.serialReaderChannelScraping.finished.connect(self.insert_data_channel)
            self.serialReaderChannelScraping.start()


    ############################################################
    ##--- Signal() return data from: channeler_scraping.py ---##
    def return_data_scraping(self, packet):
        try:
            if "message" in packet.keys():
                print(packet["message"])
            
            elif "links" in packet.keys():
                for l,t,v,idx in zip(packet["links"], packet["title"], packet["visual"], packet["index"]):
                    if l not in set(self.lista):
                        print(idx, l)
                        idx_tab = QTableWidgetItem(str(idx+1))
                        idx_tab.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                        self.c_panel.ui.tableWidget.setItem(idx, 0, idx_tab)
                        self.c_panel.ui.tableWidget.setItem(idx, 1, QTableWidgetItem(l))
                        self.c_panel.ui.tableWidget.setItem(idx, 2, QTableWidgetItem(t))
                        self.c_panel.ui.tableWidget.setItem(idx, 3, QTableWidgetItem(v))
                    self.lista.append(l)
            
            elif "channel_data" in packet.keys():
                # Insert data in the left-panel-channel-info
                self.packet_data = packet["channel_data"]
                self.insert_data_channel()

                # Hide_Selenium_Layout , Full_Size_Table , Resize_Top_Panel
                self.animation.animation_top_panel()
                self.animation.animation_central_panel()
                self.animation.animation_bottom_left_panel()
                # Btn start and stop
                self.ui.stop_scraping_btn.hide()
                self.ui.start_scraping_btn.show()
                # Save data variable

        except Exception as e:
            print(f"Programm stopped without signals packet: ERROR {e}")



    def insert_data_channel(self):  
        try:
            self.download_image(self.packet_data["profile_img"])
            # Username
            self.ui.username_channel.setText(self.packet_data["username"])
            # Flag Country
            if self.packet_data["location"] != "":
                # self.ui.flag_label.setStyleSheet(stylesheet.flag(str(self.packet_data["location"][:2]).lower())) 
                self.ui.country_channel.setText(self.packet_data["location"]) 
            else: self.ui.country_channel.setText("Country not found")
                # self.ui.flag_label.setStyleSheet(stylesheet.no_flag)
            # Total Video
            self.ui.totVideo_channel.setText(str(self.packet_data["tot_video"])+" Video")
            # Total Views
            self.ui.totViews_channel.setText(self.packet_data["tot_visual"])
            # Subscriber
            self.ui.totSubs_channel.setText(self.packet_data["subs"])
            # Joined Date
            self.ui.joinedDate_channel.setText("Joined on "+self.packet_data["joined_date"])
            # Social
            self.ui.social_comboBox.addItems(self.packet_data["social"])
            # Channel Description
            self.ui.description_channel.clear()
            self.ui.description_channel.setText(self.packet_data["channel_desc"])
        except Exception as e:
            print(f"Programm stopped without data input: ERROR {e}")
        
        
        # Deleting previuous selenium widget in the layout
        for i in reversed(range(self.c_panel.ui.selenium_layout.count())): 
            self.c_panel.ui.selenium_layout.itemAt(i).widget().setParent(None)

        self.ui.stop_scraping_btn.hide()
        self.ui.start_scraping_btn.show()



    def stop_scraping(self):
        self.reset_user()
        self.serialReaderChannelScraping.quit()
        self.serialReaderChannelScraping.terminate()
        self.ui.start_scraping_btn.show()
        self.ui.stop_scraping_btn.hide()
        
        for i in reversed(range(self.c_panel.ui.selenium_layout.count())): 
            self.c_panel.ui.selenium_layout.itemAt(i).widget().setParent(None)
        
        self.animation.animation_top_panel()
        self.animation.animation_bottom_panel()




    ## ---------------------------- ##
    ##############################################################
    ## ==> END Scraping configuration ##



    def reset_user(self):
        ### CLEAR ###
        self.lista = []

        self.c_panel.ui.right_bottom_frame.hide() # tablewidget hide

        self.ui.profile_image.clear()
        self.ui.username_channel.setText("Username")
        # self.ui.flag_label.setStyleSheet(stylesheet.no_flag)
        self.ui.totVideo_channel.setText("Total videos")
        self.ui.totViews_channel.setText("Total views")
        self.ui.totSubs_channel.setText("Subscribers")
        self.ui.joinedDate_channel.setText("Joined Date")
        self.ui.social_comboBox.setEnabled(False)
        self.ui.social_comboBox.clear()
        self.ui.social_comboBox.addItem("Social")
        self.ui.btn_combo_box.hide()
        self.ui.description_channel.clear()
        self.ui.description_channel.setText("Channel description")
        self.ui.country_channel.setText("Country")


    def download_image(self, link):
        print(link)
        if len(link) > 2:
            img_data = requests.get(link).content
            with open('ui/icons/channel/profile_new.jpg', 'wb') as handler:
                handler.write(img_data)

            pixmap = QtGui.QPixmap('ui/icons/channel/profile_new.jpg')
            self.ui.profile_image.setPixmap(pixmap.scaled(134,134))
            self.ui.profile_image.adjustSize()


    def layout_cleaning(self, layout):
        # Deleting previuous selenium layout in the layout
            # Delete elements inside a layout
            # self.ui.db_status_layout.removeWidget(self.DB_offline)
            # self.DB_offline.deleteLater()
            # self.DB_offline = None
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()

    sys.exit(app.exec_())













