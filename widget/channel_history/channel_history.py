import requests
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from widget.channel_history.channel_history_ui import Ui_user
from global_variables import GlobalVariables 
from database.db_access import DBConnection
import pandas as pd
from functions import DataFrameModel
from animation import Animation, FaderWidget

class ChannelHistory(QWidget):
    # Globals
    def __init__(self, uis, idx=None, picture=None, username=None, last_update=None, _id=None):
        super().__init__()
        self.ui = Ui_user()
        self.ui.setupUi(self)
            
        self.ui_main = uis[0]
        self.ui_cpanel = uis[1]
        self.DB_history_channel = uis[2]

        self.animation = Animation(self.ui_main, self.ui_cpanel)

        self.idx = idx
        self.picture = picture
        self.username = username
        self.last_update = last_update.split(" ")[0]
        self._id = _id

        if picture: 
            self.download_picture()

        
        self.ui.chart_btn.pressed.connect(self.select_channel_data)
        self.ui.remove_btn.pressed.connect(self.remove_channel_data)


    def download_picture(self, photo = None):
        img_data = requests.get(self.picture if not photo else photo ).content

        if photo:
            with open('ui/icons/channel/profile_new.jpg', 'wb') as handler:
                handler.write(img_data)

            pixmap = QtGui.QPixmap('ui/icons/channel/profile_new.jpg')
            self.ui_main.profile_image.setPixmap(pixmap.scaled(134,134))
            self.ui_main.profile_image.adjustSize()

        else:
            with open(f'widget/channel_history/profile_picture/profile_new_{self.idx}.jpg', 'wb') as handler:
                handler.write(img_data)
            self.ui.profile_photo.setStyleSheet(f"""
                    border: 2px solid black; 
                    border-image: url('widget/channel_history/profile_picture/profile_new_{self.idx}.jpg'); 
                    border-radius: 15px;""")

            self.ui.label.setText(str(self.idx))
            self.ui.username_label.setText(self.username)
            self.ui.last_update_label.setText(f"Last update: {self.last_update}")


    def select_channel_data(self):
        GlobalVariables.SELECTED_DATA_CHANNEL = self._id
        ### - Starting QTrhead - ###
        self.serialReaderDatabase = DBConnection(GlobalVariables.DB_STRING, "select_channel")
        self.serialReaderDatabase.receivedPacketSignal.connect(self.insert_data_channel)
        self.serialReaderDatabase.start()

    def remove_channel_data(self):
        GlobalVariables.SELECTED_DATA_CHANNEL = self._id
        ### - Starting QTrhead - ###
        print(self._id, self.username)


        self.DB_history_channel.ui.photo_remove_label.setStyleSheet(f"""
                    border-image: url('widget/channel_history/profile_picture/profile_new_{self.idx}.jpg'); 
                    """)


        self.DB_history_channel.ui.username_remove_label.setText(self.username)
        FaderWidget(self.DB_history_channel.ui.stackedWidget.currentWidget(), self.DB_history_channel.ui.stackedWidget.widget(2))
        self.DB_history_channel.ui.stackedWidget.setCurrentIndex(2)
        self.DB_history_channel.ui.exit_db_btn.hide()
        self.DB_history_channel.ui.refresh_db_btn.hide()

        # self.serialReaderDatabase = DBConnection(GlobalVariables.DB_STRING, "select_channel")
        # self.serialReaderDatabase.receivedPacketSignal.connect(self.insert_data_channel)
        # self.serialReaderDatabase.start()


    def insert_data_channel(self, return_status, query):
        self.ui_main.social_comboBox.setEnabled(True)
        self.ui_main.btn_combo_box.show()
        self.ui_main.social_comboBox.clear()
        self.ui_main.social_comboBox.addItem("Social")

        try:
            self.download_picture(query[0]["profile_img"])
            # Username
            self.ui_main.username_channel.setText(query[0]["username"])
            # Flag Country
            if query[0]["location"] != "":
                # self.ui_main.flag_label.setStyleSheet(stylesheet.flag(str(query[0]["location"][:2]).lower())) 
                self.ui_main.country_channel.setText(query[0]["location"]) 
            else: self.ui_main.country_channel.setText("Country not found")
                # self.ui_main.flag_label.setStyleSheet(stylesheet.no_flag)
            # Total Video
            self.ui_main.totVideo_channel.setText(str(query[0]["tot_video"])+" Video")
            # Total Views
            self.ui_main.totViews_channel.setText(query[0]["tot_visual"])
            # Subscriber
            self.ui_main.totSubs_channel.setText(query[0]["subs"])
            # Joined Date
            self.ui_main.joinedDate_channel.setText("Joined on "+query[0]["joined_date"])
            # Social
            self.ui_main.social_comboBox.addItems(query[0]["social"])
            # Channel Description
            self.ui_main.description_channel.clear()
            self.ui_main.description_channel.setText(query[0]["channel_desc"])
        except Exception as e:
            print(f"Programm stopped without data input: ERROR {e}")

        # Insert data into TableView
        if GlobalVariables.ANIMATION_SELECTION == 0:
            self.ui_cpanel.ui.right_bottom_frame.show()
            self.animation.animation_central_panel()
            self.animation.animation_bottom_left_panel()
            self.animation.animation_bottom_panel()
            GlobalVariables.ANIMATION_SELECTION = 1
        
        try:
            df = pd.DataFrame(list(zip(query[0]["links"], query[0]["video_title"])), columns=["Links", "Title"])
            model = DataFrameModel(df)
            self.ui_cpanel.ui.tableView.setModel(model)
        except:
            df = pd.DataFrame(query[0]["links"], columns=["Links"])
            model = DataFrameModel(df)
            self.ui_cpanel.ui.tableView.setModel(model)
