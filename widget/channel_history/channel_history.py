from urllib.request import build_opener
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from widget.channel_history.channel_history_ui import Ui_user

class ChannelHistory(QWidget):
    # Globals
    def __init__(self, idx, picture, username, last_update):
        super().__init__()
        self.ui = Ui_user()
        self.ui.setupUi(self)

        self.ui.username_label.setText(username)
        self.ui.last_update_label.setText(f"Last update: {last_update}")





