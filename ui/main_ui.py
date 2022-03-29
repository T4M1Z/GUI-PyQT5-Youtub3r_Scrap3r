# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_gui_styleIniucm.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1121, 708)
        MainWindow.setMinimumSize(QSize(0, 708))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"border:none")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 30))
        self.frame_top.setMaximumSize(QSize(16777215, 30))
        self.frame_top.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));\n"
"border:0px;")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(self.frame_top)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMinimumSize(QSize(0, 28))
        self.title_frame.setMaximumSize(QSize(16777215, 26))
        self.title_frame.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"border:none;")
        self.title_frame.setFrameShape(QFrame.NoFrame)
        self.title_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.title_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.page_1_title = QFrame(self.title_frame)
        self.page_1_title.setObjectName(u"page_1_title")
        self.page_1_title.setMaximumSize(QSize(16777215, 26))
        self.page_1_title.setStyleSheet(u"background-color: rgb(195, 75, 75);\n"
"border-bottom-right-radius:26px;\n"
"border:0px;\n"
"margin-right:8px;")
        self.page_1_title.setFrameShape(QFrame.StyledPanel)
        self.page_1_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.page_1_title)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.frame_16 = QFrame(self.page_1_title)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_16)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(28, 25))
        self.label.setMaximumSize(QSize(0, 16777215))
        self.label.setStyleSheet(u"\n"
"image: url(:/16x16/icons/16x16/cil-chart-pie.png);")

        self.horizontalLayout_19.addWidget(self.label)

        self.label_11 = QLabel(self.frame_16)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_11)


        self.horizontalLayout_21.addWidget(self.frame_16)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_5.addWidget(self.page_1_title)


        self.horizontalLayout_2.addWidget(self.title_frame)

        self.window_btn = QFrame(self.frame_top)
        self.window_btn.setObjectName(u"window_btn")
        self.window_btn.setMinimumSize(QSize(124, 28))
        self.window_btn.setMaximumSize(QSize(124, 26))
        self.window_btn.setStyleSheet(u"	background-color: rgb(59, 59, 59);\n"
"border:0px;")
        self.window_btn.setFrameShape(QFrame.StyledPanel)
        self.window_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.window_btn)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_btn = QFrame(self.window_btn)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(0, 30))
        self.frame_btn.setMaximumSize(QSize(16777215, 30))
        self.frame_btn.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"border:0px;\n"
"border-top-right-radius:3px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:3px;")
        self.frame_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btn)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(0, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(44, 44, 44);\n"
"	image: url(:/16x16/icons/16x16/cil-window-minimize.png);\n"
"border-radius:0px;\n"
"	border:0px;\n"
"padding-bottom:8px\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(68, 68, 68);\n"
"	image: url(:/16x16/icons/16x16/cil-window-minimize.png);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(29, 29, 29);\n"
"	image: url(:/16x16/icons/16x16/cil-window-minimize.png);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_minimize)

        self.btn_resize = QPushButton(self.frame_btn)
        self.btn_resize.setObjectName(u"btn_resize")
        sizePolicy.setHeightForWidth(self.btn_resize.sizePolicy().hasHeightForWidth())
        self.btn_resize.setSizePolicy(sizePolicy)
        self.btn_resize.setMaximumSize(QSize(40, 16777215))
        self.btn_resize.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(58, 58, 58);\n"
"	image: url(:/16x16/icons/16x16/cil-window-restore.png);\n"
"	border:0px;\n"
"background-color: rgb(44, 44, 44);\n"
"border-radius:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(68, 68, 68);\n"
"image: url(:/16x16/icons/16x16/cil-window-restore.png);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(29, 29, 29);\n"
"	image: url(:/16x16/icons/16x16/cil-window-restore.png);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_resize)

        self.btn_close = QPushButton(self.frame_btn)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(59, 59, 59);\n"
"	image: url(:/16x16/icons/16x16/cil-x.png);\n"
"	border:0px;\n"
"background-color: rgb(44, 44, 44);\n"
"border-radius:0px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(68, 68, 68);\n"
"	image: url(:/16x16/icons/16x16/cil-x.png);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(29, 29, 29);\n"
"	image: url(:/16x16/icons/16x16/cil-x.png);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_close)


        self.horizontalLayout_3.addWidget(self.frame_btn)


        self.horizontalLayout_2.addWidget(self.window_btn)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(59, 59, 59);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, 20, 15, 20)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 630))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 9)
        self.frame_left = QFrame(self.frame_8)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setMinimumSize(QSize(220, 590))
        self.frame_left.setMaximumSize(QSize(220, 590))
        self.frame_left.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(66, 66, 66, 255), stop:1 rgba(81, 81, 81, 255));\n"
"\n"
"border-radius:4px;\n"
"border:2px solid  rgb(55,55,55);\n"
"\n"
"\n"
"\n"
"}\n"
"")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, 9)
        self.frame_6 = QFrame(self.frame_left)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 300))
        self.frame_6.setStyleSheet(u"border:none")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(12, 16, 9, 10)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 1)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.frame_25 = QFrame(self.frame_9)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(140, 140))
        self.frame_25.setMaximumSize(QSize(140, 140))
        self.frame_25.setStyleSheet(u"border:1px solid rgb(91, 91, 91);\n"
"border-radius:65px;\n"
"background-color:  rgb(91, 91, 91);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_27.setSpacing(6)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 9, 0)
        self.picture_channel = QFrame(self.frame_25)
        self.picture_channel.setObjectName(u"picture_channel")
        self.picture_channel.setMinimumSize(QSize(140, 140))
        self.picture_channel.setMaximumSize(QSize(140, 140))
        self.picture_channel.setStyleSheet(u"\n"
"background-color: rgb(89, 89, 89);\n"
"\n"
"border-radius:70px;\n"
" border-image: url(:/channel/icons/channel/profile.jpg);\n"
"")
        self.picture_channel.setFrameShape(QFrame.StyledPanel)
        self.picture_channel.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_27.addWidget(self.picture_channel)


        self.verticalLayout_5.addWidget(self.frame_25)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.username_channel = QLineEdit(self.frame_7)
        self.username_channel.setObjectName(u"username_channel")
        self.username_channel.setMinimumSize(QSize(0, 28))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setBold(False)
        font1.setWeight(50)
        self.username_channel.setFont(font1)
        self.username_channel.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(55, 55, 55);\n"
"	color: rgb(181, 181, 181);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}\n"
"\n"
"")
        self.username_channel.setFrame(True)
        self.username_channel.setAlignment(Qt.AlignCenter)
        self.username_channel.setDragEnabled(False)
        self.username_channel.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.username_channel)

        self.frame_21 = QFrame(self.frame_7)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 35))
        self.frame_21.setMaximumSize(QSize(16777215, 35))
        self.frame_21.setStyleSheet(u"QFrame{\n"
"	border: 1px solid  rgb(91, 91, 91);\n"
"	background-color: rgb(55, 55, 55);\n"
"	border-bottom-left-radius:0px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-right-radius:0px;\n"
"	border-top-right-radius:2px;\n"
"	padding:5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QFrame::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(28, 0, 37, 0)
        self.country_channel = QLabel(self.frame_21)
        self.country_channel.setObjectName(u"country_channel")
        self.country_channel.setMinimumSize(QSize(51, 0))
        self.country_channel.setMaximumSize(QSize(58, 24))
        self.country_channel.setFont(font1)
        self.country_channel.setStyleSheet(u"\n"
"	color: rgb(181, 181, 181);\n"
"\n"
"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));\n"
"")

        self.horizontalLayout_26.addWidget(self.country_channel)

        self.label_4 = QLabel(self.frame_21)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(27, 27))
        self.label_4.setStyleSheet(u"image: url(:/flags/icons/flags/it.svg);\n"
"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));")

        self.horizontalLayout_26.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_21)

        self.totVideo_channel = QLineEdit(self.frame_7)
        self.totVideo_channel.setObjectName(u"totVideo_channel")
        self.totVideo_channel.setMinimumSize(QSize(0, 28))
        self.totVideo_channel.setFont(font1)
        self.totVideo_channel.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(55, 55, 55);\n"
"	color: rgb(181, 181, 181);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}\n"
"\n"
"")
        self.totVideo_channel.setFrame(True)
        self.totVideo_channel.setAlignment(Qt.AlignCenter)
        self.totVideo_channel.setDragEnabled(False)
        self.totVideo_channel.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.totVideo_channel)

        self.totViews_channel = QLineEdit(self.frame_7)
        self.totViews_channel.setObjectName(u"totViews_channel")
        self.totViews_channel.setMinimumSize(QSize(0, 28))
        self.totViews_channel.setFont(font1)
        self.totViews_channel.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(55, 55, 55);\n"
"	color: rgb(181, 181, 181);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}\n"
"\n"
"")
        self.totViews_channel.setFrame(True)
        self.totViews_channel.setAlignment(Qt.AlignCenter)
        self.totViews_channel.setDragEnabled(False)
        self.totViews_channel.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.totViews_channel)

        self.totSubs_channel = QLineEdit(self.frame_7)
        self.totSubs_channel.setObjectName(u"totSubs_channel")
        self.totSubs_channel.setMinimumSize(QSize(0, 28))
        self.totSubs_channel.setFont(font1)
        self.totSubs_channel.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(55, 55, 55);\n"
"	color: rgb(181, 181, 181);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}\n"
"\n"
"")
        self.totSubs_channel.setFrame(True)
        self.totSubs_channel.setAlignment(Qt.AlignCenter)
        self.totSubs_channel.setDragEnabled(False)
        self.totSubs_channel.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.totSubs_channel)

        self.joinedDate_channel = QLineEdit(self.frame_7)
        self.joinedDate_channel.setObjectName(u"joinedDate_channel")
        self.joinedDate_channel.setMinimumSize(QSize(0, 28))
        self.joinedDate_channel.setFont(font1)
        self.joinedDate_channel.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(55, 55, 55);\n"
"	color: rgb(181, 181, 181);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}\n"
"\n"
"")
        self.joinedDate_channel.setFrame(True)
        self.joinedDate_channel.setAlignment(Qt.AlignCenter)
        self.joinedDate_channel.setDragEnabled(False)
        self.joinedDate_channel.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.joinedDate_channel)

        self.social_comboBox = QComboBox(self.frame_7)
        self.social_comboBox.addItem("")
        self.social_comboBox.setObjectName(u"social_comboBox")
        self.social_comboBox.setMinimumSize(QSize(0, 28))
        self.social_comboBox.setMaximumSize(QSize(16777215, 28))
        self.social_comboBox.setFont(font1)
        self.social_comboBox.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid  rgb(91, 91, 91);\n"
"	background-color: rgb(55, 55, 55);\n"
"\n"
"	color: rgb(181, 181, 181);\n"
"padding-left:10px;\n"
"\n"
"		}\n"
"QComboBox::drop-down \n"
"{\n"
"    border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"}\n"
"\n"
"QComboBox::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"\n"
"}\n"
"/* Define a new custom arrow icon for the combo box */\n"
"QComboBox::down-arrow {\n"
"	image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"	padding-right:6px;\n"
"padding-bottom:2px;\n"
"}\n"
"\n"
"QComboBox::hover\n"
"{\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.social_comboBox)

        self.description_channel = QTextEdit(self.frame_7)
        self.description_channel.setObjectName(u"description_channel")
        self.description_channel.setMinimumSize(QSize(0, 95))
        self.description_channel.setMaximumSize(QSize(16777215, 110))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        self.description_channel.setFont(font2)
        self.description_channel.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(55, 55, 55);\n"
"	color: rgb(181, 181, 181);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QTextEdit::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"\n"
"QTextEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}\n"
"\n"
"")
        self.description_channel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.description_channel.setReadOnly(True)
        self.description_channel.setAcceptRichText(True)
        self.description_channel.setCursorWidth(0)
        self.description_channel.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_4.addWidget(self.description_channel)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.verticalLayout_3.setStretch(0, 2)

        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_left)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_center = QFrame(self.frame_3)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setMinimumSize(QSize(0, 590))
        self.frame_center.setMaximumSize(QSize(16777215, 16777215))
        self.frame_center.setStyleSheet(u"QFrame {\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(66, 66, 66, 255), stop:1 rgba(81, 81, 81, 255));\n"
"border-radius:4px;\n"
"\n"
"border:2px solid  rgb(55,55,55);\n"
"}\n"
"")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_center)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 26, -1, 9)
        self.frame_31 = QFrame(self.frame_center)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 130))
        self.frame_31.setMaximumSize(QSize(16777215, 130))
        self.frame_31.setStyleSheet(u"border:none;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.section_1 = QFrame(self.frame_31)
        self.section_1.setObjectName(u"section_1")
        self.section_1.setMinimumSize(QSize(800, 130))
        self.section_1.setMaximumSize(QSize(16777215, 130))
        self.section_1.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"border-radius:3px;\n"
"border:0px;")
        self.section_1.setFrameShape(QFrame.StyledPanel)
        self.section_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.section_1)
        self.verticalLayout_7.setSpacing(13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(4, 4, 4, 4)
        self.frame_10 = QFrame(self.section_1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(66, 66, 66);\n"
"border:2px solid rgb(90, 90, 90);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 17, -1, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 430))
        self.frame_11.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(8)
        self.frame_11.setFont(font3)
        self.frame_11.setStyleSheet(u"background-color: rgb(66, 66, 66);\n"
"border:0px solid rgb(90, 90, 90);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 13)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(10)
        self.frame_13.setFont(font4)
        self.frame_13.setStyleSheet(u"border:none")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.channel_radioBtn = QRadioButton(self.frame_13)
        self.channel_radioBtn.setObjectName(u"channel_radioBtn")
        self.channel_radioBtn.setMaximumSize(QSize(100, 16777215))
        font5 = QFont()
        font5.setFamily(u"Roboto Black")
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setWeight(50)
        self.channel_radioBtn.setFont(font5)
        self.channel_radioBtn.setStyleSheet(u"\n"
"QRadioButton{background-color: rgb(55, 55, 55);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-radius:2px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QRadioButton::hover{\n"
"	background-color: rgb(59, 59, 59);}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: rgb(195, 75, 75);\n"
"    border:                 2px solid white;\n"
"	border-radius:6px;\n"
"}")
        self.channel_radioBtn.setChecked(True)

        self.horizontalLayout_12.addWidget(self.channel_radioBtn)

        self.video_radioBtn = QRadioButton(self.frame_13)
        self.video_radioBtn.setObjectName(u"video_radioBtn")
        self.video_radioBtn.setMaximumSize(QSize(95, 16777215))
        self.video_radioBtn.setFont(font5)
        self.video_radioBtn.setStyleSheet(u"\n"
"QRadioButton{background-color: rgb(55, 55, 55);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-radius:2px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QRadioButton::hover{\n"
"	background-color: rgb(59, 59, 59);}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: rgb(195, 75, 75);\n"
"    border:                 2px solid white;\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_12.addWidget(self.video_radioBtn)

        self.url_Input = QLineEdit(self.frame_13)
        self.url_Input.setObjectName(u"url_Input")
        self.url_Input.setMaximumSize(QSize(16777215, 39))
        font6 = QFont()
        font6.setFamily(u"Roboto")
        font6.setPointSize(9)
        self.url_Input.setFont(font6)
        self.url_Input.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(55, 55, 55);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}")

        self.horizontalLayout_12.addWidget(self.url_Input)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 0))
        self.frame_18.setMaximumSize(QSize(140, 37))
        self.frame_18.setStyleSheet(u"background-color: rgb(55, 55, 55);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-radius:2px;\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 5, -1, 5)
        self.cluster_checkBox = QCheckBox(self.frame_18)
        self.cluster_checkBox.setObjectName(u"cluster_checkBox")
        self.cluster_checkBox.setMinimumSize(QSize(15, 0))
        self.cluster_checkBox.setMaximumSize(QSize(15, 16777215))
        self.cluster_checkBox.setStyleSheet(u"CheckBox{\n"
"	border:none;	\n"
"	margin-right:0px;\n"
"}\n"
"\n"
"CheckBox::hover{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}\n"
"\n"
"CheckBox::indicator:checked {\n"
"    background-color: rgb(195, 75, 75);\n"
"    border:                 2px solid white;\n"
"	border-radius:6px;\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.cluster_checkBox)

        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color:white;\n"
"border:none;\n"
"")

        self.horizontalLayout_17.addWidget(self.label_3)

        self.cluster_spinBox = QSpinBox(self.frame_18)
        self.cluster_spinBox.setObjectName(u"cluster_spinBox")
        self.cluster_spinBox.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cluster_spinBox.sizePolicy().hasHeightForWidth())
        self.cluster_spinBox.setSizePolicy(sizePolicy2)
        self.cluster_spinBox.setMinimumSize(QSize(0, 22))
        self.cluster_spinBox.setMaximumSize(QSize(16777215, 22))
        self.cluster_spinBox.setStyleSheet(u"QSpinBox{\n"
"		background-color: rgb(255, 255, 255); \n"
"		margin-left:10px;\n"
"\n"
"		width:25px;\n"
"		height:18px;\n"
"		padding-left:3px;\n"
"		}\n"
"\n"
"QSpinBox::down-button  {\n"
"	background-color: rgb(68, 68, 68);	\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"QSpinBox::up-button  {\n"
"	background-color: rgb(68, 68, 68);	\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"QSpinBox::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}\n"
"\n"
"QSpinBox::up-arrow:hover { 	\n"
"		background-color: rgb(75, 75, 75);	\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"\n"
"QSpinBox::down-arrow:hover { \n"
"		background-color: rgb(75, 75, 75);\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"QSpinBox::up-arrow::pressed{\n"
"		background-color: rgb(71, 71, 71);"
                        "\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"QSpinBox::down-arrow::pressed{\n"
"		background-color: rgb(71, 71, 71);\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"")
        self.cluster_spinBox.setMinimum(1)
        self.cluster_spinBox.setMaximum(5)

        self.horizontalLayout_17.addWidget(self.cluster_spinBox)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 3)
        self.horizontalLayout_17.setStretch(2, 3)

        self.horizontalLayout_12.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 19))
        self.frame_17.setMaximumSize(QSize(140, 37))
        self.frame_17.setStyleSheet(u"background-color: rgb(55, 55, 55);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-radius:2px;\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 5, -1, 5)
        self.label_2 = QLabel(self.frame_17)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color:white;\n"
"border:none;\n"
"")

        self.horizontalLayout_16.addWidget(self.label_2)

        self.threads_spinBox = QSpinBox(self.frame_17)
        self.threads_spinBox.setObjectName(u"threads_spinBox")
        self.threads_spinBox.setMaximumSize(QSize(16777215, 22))
        self.threads_spinBox.setStyleSheet(u"QSpinBox{\n"
"		background-color: rgb(255, 255, 255); \n"
"		margin-left:10px;\n"
"\n"
"		width:25px;\n"
"		height:18px;\n"
"		padding-left:3px;\n"
"		}\n"
"\n"
"QSpinBox::down-button  {\n"
"	background-color: rgb(68, 68, 68);	\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"QSpinBox::up-button  {\n"
"	background-color: rgb(68, 68, 68);	\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"QSpinBox::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}\n"
"\n"
"QSpinBox::up-arrow:hover { 	\n"
"		background-color: rgb(75, 75, 75);	\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"\n"
"QSpinBox::down-arrow:hover { \n"
"		background-color: rgb(75, 75, 75);\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"QSpinBox::up-arrow::pressed{\n"
"		background-color: rgb(71, 71, 71);"
                        "\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"QSpinBox::down-arrow::pressed{\n"
"		background-color: rgb(71, 71, 71);\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"")
        self.threads_spinBox.setMinimum(1)
        self.threads_spinBox.setMaximum(8)

        self.horizontalLayout_16.addWidget(self.threads_spinBox)

        self.horizontalLayout_16.setStretch(1, 1)

        self.horizontalLayout_12.addWidget(self.frame_17)

        self.horizontalLayout_12.setStretch(1, 2)

        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_22 = QFrame(self.frame_12)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"border:none")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.username_db = QLineEdit(self.frame_22)
        self.username_db.setObjectName(u"username_db")
        self.username_db.setEnabled(True)
        self.username_db.setMinimumSize(QSize(0, 28))
        self.username_db.setFont(font6)
        self.username_db.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(55, 55, 55);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}")
        self.username_db.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_9.addWidget(self.username_db)

        self.password_db = QLineEdit(self.frame_22)
        self.password_db.setObjectName(u"password_db")
        self.password_db.setEnabled(True)
        self.password_db.setMinimumSize(QSize(0, 28))
        self.password_db.setFont(font6)
        self.password_db.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(55, 55, 55);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color: rgb(59, 59, 59);}\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid rgb(195, 75, 75);\n"
"}")
        self.password_db.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_9.addWidget(self.password_db)

        self.loading_db = QHBoxLayout()
        self.loading_db.setSpacing(0)
        self.loading_db.setObjectName(u"loading_db")
        self.loading_db.setContentsMargins(0, -1, -1, -1)
        self.label_gif = QLabel(self.frame_22)
        self.label_gif.setObjectName(u"label_gif")

        self.loading_db.addWidget(self.label_gif)


        self.horizontalLayout_9.addLayout(self.loading_db)

        self.test_db_btn = QPushButton(self.frame_22)
        self.test_db_btn.setObjectName(u"test_db_btn")
        self.test_db_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.test_db_btn.sizePolicy().hasHeightForWidth())
        self.test_db_btn.setSizePolicy(sizePolicy)
        self.test_db_btn.setMinimumSize(QSize(62, 28))
        self.test_db_btn.setMaximumSize(QSize(16777215, 28))
        self.test_db_btn.setFont(font5)
        self.test_db_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.test_db_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(127, 127, 127);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:2px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-right-radius:2px;\n"
"border-top-right-radius:0px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(137, 137, 137);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(112, 112, 112);\n"
"}")

        self.horizontalLayout_9.addWidget(self.test_db_btn)

        self.frame_29 = QFrame(self.frame_22)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy3)
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setStyleSheet(u"")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.status_db_connection = QLabel(self.frame_29)
        self.status_db_connection.setObjectName(u"status_db_connection")
        self.status_db_connection.setMinimumSize(QSize(80, 28))
        self.status_db_connection.setMaximumSize(QSize(80, 28))
        font7 = QFont()
        font7.setFamily(u"Roboto Black")
        font7.setBold(False)
        font7.setWeight(50)
        self.status_db_connection.setFont(font7)
        self.status_db_connection.setStyleSheet(u"QLabel{\n"
"background-color: rgb(55, 55, 55);\n"
"	color: rgb(195, 75, 75);\n"
"border: 1px solid  rgb(91, 91, 91);\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:2px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:2px;\n"
"padding:5px;\n"
"}\n"
"")
        self.status_db_connection.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.status_db_connection)


        self.horizontalLayout_9.addWidget(self.frame_29)

        self.horizontalLayout_9.setStretch(0, 5)
        self.horizontalLayout_9.setStretch(1, 5)
        self.horizontalLayout_9.setStretch(3, 3)
        self.horizontalLayout_9.setStretch(4, 5)

        self.verticalLayout_9.addWidget(self.frame_22)


        self.verticalLayout_8.addWidget(self.frame_12)


        self.horizontalLayout_13.addWidget(self.frame_11)


        self.verticalLayout_7.addWidget(self.frame_10)


        self.horizontalLayout_15.addWidget(self.section_1)


        self.verticalLayout_13.addWidget(self.frame_31)

        self.frame_30 = QFrame(self.frame_center)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));\n"
"border:none")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.stop_scraping_btn = QPushButton(self.frame_30)
        self.stop_scraping_btn.setObjectName(u"stop_scraping_btn")
        self.stop_scraping_btn.setMinimumSize(QSize(200, 40))
        self.stop_scraping_btn.setMaximumSize(QSize(200, 40))
        font8 = QFont()
        font8.setFamily(u"Roboto Black")
        font8.setPointSize(10)
        self.stop_scraping_btn.setFont(font8)
        self.stop_scraping_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_scraping_btn.setStyleSheet(u"QPushButton{ \n"
"	border: 4px solid rgb(49, 49, 49);\n"
"	border-top:0px;\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-bottom-left-radius:5px;\n"
"	border-bottom-right-radius:5px;\n"
"	color: rgb(201, 201, 201);\n"
"}\n"
"\n"
"QPushButton::hover{ \n"
"	background-color: rgb(76, 76, 76);\n"
"	color: rgb(221, 221, 221);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(56, 56, 56);\n"
"}")

        self.horizontalLayout_8.addWidget(self.stop_scraping_btn)

        self.start_scraping_btn = QPushButton(self.frame_30)
        self.start_scraping_btn.setObjectName(u"start_scraping_btn")
        self.start_scraping_btn.setMinimumSize(QSize(200, 40))
        self.start_scraping_btn.setMaximumSize(QSize(200, 40))
        self.start_scraping_btn.setFont(font8)
        self.start_scraping_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_scraping_btn.setStyleSheet(u"QPushButton{ \n"
"	border: 4px solid rgb(49, 49, 49);\n"
"	border-top:0px;\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-bottom-left-radius:5px;\n"
"	border-bottom-right-radius:5px;\n"
"	color: rgb(201, 201, 201);\n"
"}\n"
"\n"
"QPushButton::hover{ \n"
"	background-color: rgb(76, 76, 76);\n"
"	color: rgb(221, 221, 221);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(56, 56, 56);\n"
"}")

        self.horizontalLayout_8.addWidget(self.start_scraping_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_13.addWidget(self.frame_30)

        self.selenium_layout = QVBoxLayout()
        self.selenium_layout.setObjectName(u"selenium_layout")

        self.verticalLayout_13.addLayout(self.selenium_layout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)


        self.horizontalLayout_6.addWidget(self.frame_center)

        self.horizontalLayout_6.setStretch(0, 10)
        self.horizontalLayout_6.setStretch(1, 120)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 18))
        self.frame_4.setMaximumSize(QSize(16777215, 18))
        self.frame_4.setStyleSheet(u"background-color: rgb(74, 74, 74);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom = QFrame(self.frame_4)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMaximumSize(QSize(16777215, 30))
        self.frame_bottom.setStyleSheet(u"background-color: rgb(85, 85, 85);")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.frame_bottom.setLineWidth(1)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(815, 3, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer)

        self.drag_btn = QPushButton(self.frame_bottom)
        self.drag_btn.setObjectName(u"drag_btn")
        self.drag_btn.setMaximumSize(QSize(20, 20))
        self.drag_btn.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.drag_btn.setStyleSheet(u"image: url(:/16x16/icons/16x16/cil-caret-bottom.png);\n"
"border:none;\n")

        self.horizontalLayout_22.addWidget(self.drag_btn)


        self.horizontalLayout_7.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"YouTub3r_Scrap3r", None))
        self.btn_minimize.setText("")
        self.btn_resize.setText("")
        self.btn_close.setText("")
        self.username_channel.setInputMask("")
        self.username_channel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username_channel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.country_channel.setText(QCoreApplication.translate("MainWindow", u"Country", None))
        self.label_4.setText("")
        self.totVideo_channel.setInputMask("")
        self.totVideo_channel.setText(QCoreApplication.translate("MainWindow", u"Total videos", None))
        self.totVideo_channel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Joined date", None))
        self.totViews_channel.setInputMask("")
        self.totViews_channel.setText(QCoreApplication.translate("MainWindow", u"Total views", None))
        self.totViews_channel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Total video", None))
        self.totSubs_channel.setInputMask("")
        self.totSubs_channel.setText(QCoreApplication.translate("MainWindow", u"Subscribers", None))
        self.totSubs_channel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Total visual", None))
        self.joinedDate_channel.setInputMask("")
        self.joinedDate_channel.setText(QCoreApplication.translate("MainWindow", u"Joined Date", None))
        self.joinedDate_channel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Subscribers", None))
        self.social_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Social", None))

        self.description_channel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Channel description", None))
        self.channel_radioBtn.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.video_radioBtn.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.url_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link url", None))
        self.cluster_checkBox.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cluster", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Threads", None))
        self.username_db.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_db.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_gif.setText("")
        self.test_db_btn.setText(QCoreApplication.translate("MainWindow", u"Test DB", None))
        self.status_db_connection.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.stop_scraping_btn.setText(QCoreApplication.translate("MainWindow", u"Start scraping", None))
        self.start_scraping_btn.setText(QCoreApplication.translate("MainWindow", u"Start scraping", None))
        self.drag_btn.setText("")
    # retranslateUi

