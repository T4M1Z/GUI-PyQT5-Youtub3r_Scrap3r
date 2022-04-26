# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'channel_history_uianYIXJ.ui'
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

class Ui_user(object):
    def setupUi(self, user):
        if user.objectName():
            user.setObjectName(u"user")
        user.resize(335, 65)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(user.sizePolicy().hasHeightForWidth())
        user.setSizePolicy(sizePolicy)
        user.setMinimumSize(QSize(0, 0))
        user.setMaximumSize(QSize(16777215, 65))
        user.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(user)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 3, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.frame1 = QFrame(user)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"QFrame #frame1{\n"
"	background-color: rgb(222, 222, 222);\n"
"border:2px solid rgb(140, 140, 140);\n"
"border-radius:8px\n"
"}")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 9, 0)
        self.frame_4 = QFrame(self.frame1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 4, 4, 4)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(50, 50, 50);")

        self.horizontalLayout.addWidget(self.label)

        self.profile_photo = QLabel(self.frame_4)
        self.profile_photo.setObjectName(u"profile_photo")
        self.profile_photo.setMinimumSize(QSize(30, 30))
        self.profile_photo.setMaximumSize(QSize(30, 30))
        self.profile_photo.setStyleSheet(u"background-color: rgb(41, 42, 53);\n"
"border-radius:15px;")

        self.horizontalLayout.addWidget(self.profile_photo)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.username_label = QLabel(self.frame_2)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(10)
        self.username_label.setFont(font1)
        self.username_label.setStyleSheet(u"color: rgb(50, 50, 50);")

        self.verticalLayout_2.addWidget(self.username_label)

        self.last_update_label = QLabel(self.frame_2)
        self.last_update_label.setObjectName(u"last_update_label")
        self.last_update_label.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(7)
        self.last_update_label.setFont(font2)
        self.last_update_label.setStyleSheet(u"color: rgb(50, 50, 50);")

        self.verticalLayout_2.addWidget(self.last_update_label)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.frame_btn = QFrame(self.frame1)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMaximumSize(QSize(16777215, 30))
        self.frame_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.user_btn = QPushButton(self.frame_btn)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setMinimumSize(QSize(16, 16))
        self.user_btn.setMaximumSize(QSize(16, 16))
        self.user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.user_btn.setStyleSheet(u"QPushButton{image: url(:/channel/icons/channel/user_btn.svg);\n"
"border:none;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.user_btn)

        self.chart_btn = QPushButton(self.frame_btn)
        self.chart_btn.setObjectName(u"chart_btn")
        self.chart_btn.setMinimumSize(QSize(20, 20))
        self.chart_btn.setMaximumSize(QSize(20, 20))
        self.chart_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.chart_btn.setStyleSheet(u"QPushButton{\n"
"image: url(:/channel/icons/channel/chart_btn.svg);\n"
"border:none;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.chart_btn)


        self.horizontalLayout_4.addWidget(self.frame_btn)

        self.horizontalLayout_4.setStretch(1, 1)

        self.horizontalLayout_5.addWidget(self.frame1)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)


        self.retranslateUi(user)

        QMetaObject.connectSlotsByName(user)
    # setupUi

    def retranslateUi(self, user):
        user.setWindowTitle(QCoreApplication.translate("user", u"Form", None))
        self.label.setText(QCoreApplication.translate("user", u"1", None))
        self.profile_photo.setText("")
        self.username_label.setText(QCoreApplication.translate("user", u"Examplename_23", None))
        self.last_update_label.setText(QCoreApplication.translate("user", u"last_update: 24/04/2022", None))
        self.user_btn.setText("")
        self.chart_btn.setText("")
    # retranslateUi

