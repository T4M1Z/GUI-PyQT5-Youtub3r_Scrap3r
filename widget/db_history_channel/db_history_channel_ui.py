# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db_history_channel_uiofxyIn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from ui import img_ui_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(342, 676)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.db_channel_history = QFrame(Form)
        self.db_channel_history.setObjectName(u"db_channel_history")
        self.db_channel_history.setFrameShape(QFrame.StyledPanel)
        self.db_channel_history.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.db_channel_history)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.db_channel_history)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 41))
        self.frame_35.setStyleSheet(u"QFrame{\n"
"background-color: rgb(55, 55, 55);\n"
"border-top-left-radius:2px;\n"
"border-top-right-radius:2px;\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_35)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(13, 9, 13, 9)
        self.label_14 = QLabel(self.frame_35)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(15, 0))
        self.label_14.setStyleSheet(u"image: url(:/database/icons/db/db_s_white.svg);")

        self.horizontalLayout.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_35)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.label_15)

        self.refresh_gif = QLabel(self.frame_35)
        self.refresh_gif.setObjectName(u"refresh_gif")
        self.refresh_gif.setMinimumSize(QSize(24, 23))
        self.refresh_gif.setMaximumSize(QSize(24, 23))
        self.refresh_gif.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.refresh_gif)

        self.refresh_db_btn = QPushButton(self.frame_35)
        self.refresh_db_btn.setObjectName(u"refresh_db_btn")
        self.refresh_db_btn.setMinimumSize(QSize(24, 15))
        self.refresh_db_btn.setMaximumSize(QSize(24, 15))
        self.refresh_db_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.refresh_db_btn.setStyleSheet(u"QPushButton{\n"
"image: url(:/database/icons/db/reload_db.png);\n"
"border-radius:4px;\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(63, 63, 63);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.refresh_db_btn)

        self.exit_db_btn = QPushButton(self.frame_35)
        self.exit_db_btn.setObjectName(u"exit_db_btn")
        self.exit_db_btn.setMinimumSize(QSize(26, 18))
        self.exit_db_btn.setMaximumSize(QSize(26, 18))
        self.exit_db_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_db_btn.setStyleSheet(u"QPushButton{\n"
"image: url(:/database/icons/db/exit_db.png);\n"
"border-radius:8px;\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(59, 59, 59);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.exit_db_btn)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_18.addWidget(self.frame_35)

        self.stackedWidget = QStackedWidget(self.db_channel_history)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(74, 74, 74);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"QWidget #page_1{\n"
"	background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.511182, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(71, 71, 71, 255));\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.page_1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea1 = QScrollArea(self.page_1)
        self.scrollArea1.setObjectName(u"scrollArea1")
        self.scrollArea1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));")
        self.scrollArea1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea1.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.scroll_widget.setGeometry(QRect(0, 0, 338, 631))
        self.scroll_widget.setStyleSheet(u"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.scroll_widget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, -1, -1, -1)
        self.channel_list_widget = QVBoxLayout()
        self.channel_list_widget.setSpacing(0)
        self.channel_list_widget.setObjectName(u"channel_list_widget")
        self.channel_list_widget.setContentsMargins(-1, 0, -1, 13)

        self.verticalLayout_19.addLayout(self.channel_list_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer)

        self.scrollArea1.setWidget(self.scroll_widget)

        self.verticalLayout_2.addWidget(self.scrollArea1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QWidget #page_2{\n"
"background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.511182, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame #frame{\n"
"	background-color: qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.511182, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(71, 71, 71, 255));\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(18, 9, 18, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame_menu_exit = QFrame(self.frame)
        self.frame_menu_exit.setObjectName(u"frame_menu_exit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu_exit.sizePolicy().hasHeightForWidth())
        self.frame_menu_exit.setSizePolicy(sizePolicy)
        self.frame_menu_exit.setMinimumSize(QSize(0, 98))
        font1 = QFont()
        font1.setPointSize(7)
        self.frame_menu_exit.setFont(font1)
        self.frame_menu_exit.setStyleSheet(u"QFrame {\n"
"background-color: rgb(54, 54, 54);\n"
"border-radius:4px;\n"
"}")
        self.frame_menu_exit.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_exit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_menu_exit)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(14, 6, 14, 15)
        self.label = QLabel(self.frame_menu_exit)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(15)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.frame_menu_exit)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(9)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(253, 111, 96);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_4 = QLabel(self.frame_menu_exit)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(11)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(223, 111, 96);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.verticalLayout_3.addWidget(self.frame_menu_exit)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(14)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 35)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.db_exit_yes_btn = QPushButton(self.frame_3)
        self.db_exit_yes_btn.setObjectName(u"db_exit_yes_btn")
        self.db_exit_yes_btn.setMinimumSize(QSize(100, 35))
        self.db_exit_yes_btn.setMaximumSize(QSize(16777215, 35))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setWeight(75)
        self.db_exit_yes_btn.setFont(font5)
        self.db_exit_yes_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.db_exit_yes_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(190, 79, 64);\n"
"color: #ffffff;\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(221, 221, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(210, 79, 64);\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(190, 79, 64);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.db_exit_yes_btn)

        self.db_exit_no_btn = QPushButton(self.frame_3)
        self.db_exit_no_btn.setObjectName(u"db_exit_no_btn")
        self.db_exit_no_btn.setMinimumSize(QSize(100, 35))
        self.db_exit_no_btn.setMaximumSize(QSize(16777215, 35))
        self.db_exit_no_btn.setFont(font5)
        self.db_exit_no_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.db_exit_no_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(119, 177, 88);\n"
"color: #ffffff;\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(221, 221, 221);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(119, 200, 88);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(119, 190, 88);\n"
"}")

        self.horizontalLayout_3.addWidget(self.db_exit_no_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 300))
        font6 = QFont()
        font6.setPointSize(9)
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"image: url(:/database/icons/db/db_s_exit.svg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));")

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_18.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.db_channel_history)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Channels History</span></p></body></html>", None))
        self.refresh_gif.setText("")
        self.refresh_db_btn.setText("")
        self.exit_db_btn.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Do you really want to exit?", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>If you are not connected to a database </p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" text-decoration: underline;\">all the data will not be saved</span></p></body></html>", None))
        self.db_exit_yes_btn.setText(QCoreApplication.translate("Form", u"Yes", None))
        self.db_exit_no_btn.setText(QCoreApplication.translate("Form", u"No", None))
        self.label_3.setText("")
    # retranslateUi

