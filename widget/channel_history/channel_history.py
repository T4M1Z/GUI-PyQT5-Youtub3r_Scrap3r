import requests
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from widget.channel_history.channel_history_ui import Ui_user

class ChannelHistory(QWidget):
    # Globals
    def __init__(self, idx, picture, username, last_update):
        super().__init__()
        self.ui = Ui_user()
        self.ui.setupUi(self)
        self.picture = picture
        self.idx = idx


        self.download_picture()
        self.ui.label.setText(str(idx))
        self.ui.username_label.setText(username)
        self.ui.last_update_label.setText(f"Last update: {last_update}")

    def download_picture(self):
        print("sto scaricando")

        img_data = requests.get(self.picture).content
        with open(f'widget/channel_history/profile_picture/profile_new_{self.idx}.jpg', 'wb') as handler:
            handler.write(img_data)

        self.ui.profile_photo.setStyleSheet(f"""
                border: 2px solid black; 
                border-image: url('widget/channel_history/profile_picture/profile_new_{self.idx}.jpg'); 
                border-radius: 15px;""")



