from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from widget.db_history_channel.db_history_channel_ui import Ui_Form
from animation import FaderWidget

class DBHistoryChannel(QWidget):
    # Globals
    def __init__(self, ui_main):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui_main = ui_main

        self.ui.exit_db_btn.pressed.connect(self.exit_selection)
        self.ui.db_exit_yes_btn.pressed.connect(self.confirm_exit)
        self.ui.db_exit_no_btn.pressed.connect(self.decline_exit)


    def exit_selection(self):
        FaderWidget(self.ui.stackedWidget.currentWidget(), self.ui.stackedWidget.widget(1))
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.exit_db_btn.hide()
        self.ui.refresh_db_btn.hide()

    def confirm_exit(self):
        # Animation open Database Info
        self.left_panel_animation = QtCore.QPropertyAnimation(self.ui_main.db_settings_frame, b"maximumHeight")
        h1, h2 = 0,450
        self.left_panel_animation.setDuration(750)
        self.left_panel_animation.setStartValue(h1)
        self.left_panel_animation.setEndValue(h2)
        self.left_panel_animation.start()

        # Restore DB_Offline widget page
        FaderWidget(self.ui_main.stackedWidget.currentWidget(), self.ui_main.stackedWidget.widget(0))
        self.ui_main.stackedWidget.setCurrentIndex(0)
        # Reset string test 
        self.ui_main.db_connection_input.setText("")
        # Restore initial user history page and btn
        FaderWidget(self.ui.stackedWidget.currentWidget(), self.ui.stackedWidget.widget(0))
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.exit_db_btn.show()
        self.ui.refresh_db_btn.show()

    def decline_exit(self):
        FaderWidget(self.ui.stackedWidget.currentWidget(), self.ui.stackedWidget.widget(0))
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.exit_db_btn.show()
        self.ui.refresh_db_btn.show()
