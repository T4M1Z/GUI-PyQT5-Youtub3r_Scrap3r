# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'third_gui_stylecUKFVI.ui'
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
        MainWindow.resize(1000, 708)
        MainWindow.setMinimumSize(QSize(1000, 708))
        font = QFont()
        font.setFamily(u"Oswald ExtraLight")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR horiz:horizontal */\n"
"QScrollBar::handle:horizontal {	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border-radius: 4px;\n"
"\n"
"}\n"
"QScrollBar::handle:horizontal:hover{	\n"
"	background-color: rgb(54, 54, 54);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(60, 60, 60);\n"
"border-radius: 3px;\n"
"width:0px;\n"
"}\n"
"\n"
"\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"		background-color: rgb(60, 60, 60);\n"
"border-radius: 3px;\n"
"width:0px;\n"
"}\n"
"\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
""
                        "	background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR horiz:vertical */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(49, 49, 49);\n"
"	border-radius: 7px;\n"
"\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(54, 54, 54);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(60, 60, 60);\n"
"border-radius: 3px;\n"
"width:0px;\n"
"}\n"
"\n"
"\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"		background-color: rgb(60, 60, 60);\n"
"border-radius: 3px;\n"
"width:0px;\n"
"}\n"
"\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:verti"
                        "cal, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"border:none")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));")
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
        self.frame_top.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"border:0px;\n"
"border-top-left-radius: 10px;;\n"
"border-top-right-radius: 10px;")
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
        self.title_frame.setMaximumSize(QSize(16777215, 30))
        self.title_frame.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));\n"
"border-top-left-radius: 10px;\n"
"")
        self.title_frame.setFrameShape(QFrame.NoFrame)
        self.title_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.title_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.page_1_title = QFrame(self.title_frame)
        self.page_1_title.setObjectName(u"page_1_title")
        self.page_1_title.setMaximumSize(QSize(16777215, 30))
        self.page_1_title.setStyleSheet(u"background-color: rgb(195, 75, 75);\n"
"border-bottom-right-radius:26px;\n"
"border:0px;\n"
"border-top-left-radius: 10px;\n"
"\n"
"")
        self.page_1_title.setFrameShape(QFrame.StyledPanel)
        self.page_1_title.setFrameShadow(QFrame.Raised)
        self.page_1_title.setLineWidth(1)
        self.horizontalLayout_21 = QHBoxLayout(self.page_1_title)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_21.setContentsMargins(-1, 0, 9, 0)
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
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_11.setFont(font1)
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
"border-bottom-right-radius:3px;\n"
"border-top-right-radius: 10px;")
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
"border-top-right-radius: 10px;\n"
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
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        self.frame_3.setFont(font2)
        self.frame_3.setStyleSheet(u"QFrame #frame_3{\n"
"background-color: #3B3B3B;}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 15, 15, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, 0, -1)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(360, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"QFrame #frame_2{\n"
"background-color: #616161\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(330, 250))
        self.frame_4.setStyleSheet(u"QFrame #frame_4{\n"
"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:3px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 9)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(16)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color:White")

        self.horizontalLayout_9.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(10)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color:white")

        self.horizontalLayout_10.addWidget(self.label_5)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 80))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(8)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color:white")

        self.horizontalLayout_11.addWidget(self.label_6)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.start_scraping_btn_2 = QPushButton(self.frame_11)
        self.start_scraping_btn_2.setObjectName(u"start_scraping_btn_2")
        self.start_scraping_btn_2.setMinimumSize(QSize(140, 35))
        self.start_scraping_btn_2.setMaximumSize(QSize(140, 35))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setWeight(75)
        self.start_scraping_btn_2.setFont(font6)
        self.start_scraping_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_scraping_btn_2.setStyleSheet(u"QPushButton{ \n"
"border:2px solid #7E7E7E;\n"
"	border-top:0px;\n"
"	background-color:  #CECECE;\n"
"color: #545454;\n"
"	font-weight: bold;\n"
"	border-bottom-left-radius:5px;\n"
"	border-bottom-right-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{ \n"
"	background-color: rgb(220,220,220);\n"
"	color: rgb(57, 57, 57);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(210, 210, 210);\n"
"}")

        self.verticalLayout_5.addWidget(self.start_scraping_btn_2)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:3px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:3px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_6)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.frame_2)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(15, 0))
        self.pushButton.setMaximumSize(QSize(15, 16777215))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(81, 81, 81);\n"
"border-top-right-radius: 6px;\n"
"border-bottom-right-radius: 6px;\n"
"	image: url(:/16x16/icons/16x16/cil-caret-right.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(71, 71, 71);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(75, 75, 75);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)

        self.frame_center = QFrame(self.frame_3)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setMinimumSize(QSize(0, 590))
        self.frame_center.setMaximumSize(QSize(16777215, 16777215))
        self.frame_center.setStyleSheet(u"")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_center)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 9, -1, 9)
        self.scraping_setting_frame = QHBoxLayout()
        self.scraping_setting_frame.setObjectName(u"scraping_setting_frame")
        self.scraping_setting_frame.setContentsMargins(40, 0, 40, 0)
        self.frame_12 = QFrame(self.frame_center)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 80))
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.frame_12.setStyleSheet(u"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:4px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 0, 15, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setPointSize(10)
        self.frame_13.setFont(font7)
        self.frame_13.setStyleSheet(u"border:none;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.channel_radioBtn = QRadioButton(self.frame_13)
        self.channel_radioBtn.setObjectName(u"channel_radioBtn")
        self.channel_radioBtn.setMinimumSize(QSize(0, 42))
        self.channel_radioBtn.setMaximumSize(QSize(500, 42))
        font8 = QFont()
        font8.setFamily(u"Segoe UI Semibold")
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setWeight(50)
        self.channel_radioBtn.setFont(font8)
        self.channel_radioBtn.setStyleSheet(u"\n"
"QRadioButton{background-color:  rgb(214, 214, 214);\n"
"color: #545454;\n"
"border: 1px solid  #ffffff;\n"
"border-radius:2px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QRadioButton::hover{\n"
"background-color:  rgb(210, 210, 210);}\n"
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
        self.video_radioBtn.setMinimumSize(QSize(0, 42))
        self.video_radioBtn.setMaximumSize(QSize(95, 42))
        self.video_radioBtn.setFont(font8)
        self.video_radioBtn.setStyleSheet(u"\n"
"QRadioButton{background-color:  rgb(214, 214, 214);\n"
"color: #545454;\n"
"border: 1px solid  #ffffff;\n"
"border-radius:2px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QRadioButton::hover{\n"
"background-color:  rgb(210, 210, 210);\n"
"}\n"
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
        self.url_Input.setMinimumSize(QSize(160, 42))
        self.url_Input.setMaximumSize(QSize(16777215, 42))
        self.url_Input.setFont(font8)
        self.url_Input.setCursor(QCursor(Qt.IBeamCursor))
        self.url_Input.setStyleSheet(u"QLineEdit{\n"
"background-color:  rgb(214, 214, 214);\n"
"color: #545454;\n"
"border: 1px solid  #ffffff;\n"
"border-radius:2px;\n"
"padding:10px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color:  rgb(210, 210, 210);}\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid  rgb(121,121, 121);\n"
"}")

        self.horizontalLayout_12.addWidget(self.url_Input)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 42))
        self.frame_18.setMaximumSize(QSize(115, 42))
        self.frame_18.setStyleSheet(u"background-color:   rgb(214, 214, 214);\n"
"border: 1px solid  #ffffff;\n"
"border-radius:2px;\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 5, -1, 5)
        self.cluster_checkBox = QCheckBox(self.frame_18)
        self.cluster_checkBox.setObjectName(u"cluster_checkBox")
        self.cluster_checkBox.setMinimumSize(QSize(19, 0))
        self.cluster_checkBox.setMaximumSize(QSize(19, 16777215))
        self.cluster_checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.cluster_checkBox.setStyleSheet(u"QCheckBox{\n"
"	border:none;	\n"
"	margin-right:0px;\n"
"border: 1px solid rgb(190, 190, 190);\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(195, 75, 75);\n"
"    border:                 2px solid white;\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.cluster_checkBox)

        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QSize(55, 0))
        self.label_3.setFont(font8)
        self.label_3.setStyleSheet(u"color: #545454;\n"
"border:none;\n"
"")

        self.horizontalLayout_17.addWidget(self.label_3)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 3)

        self.horizontalLayout_12.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 42))
        self.frame_17.setMaximumSize(QSize(140, 42))
        self.frame_17.setStyleSheet(u"background-color:   rgb(214, 214, 214);\n"
"border: 1px solid  #ffffff;\n"
"border-radius:2px;\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 5, -1, 5)
        self.label_2 = QLabel(self.frame_17)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font8)
        self.label_2.setStyleSheet(u"color: #545454;\n"
"border:none;\n"
"")

        self.horizontalLayout_16.addWidget(self.label_2)

        self.threads_spinBox = QSpinBox(self.frame_17)
        self.threads_spinBox.setObjectName(u"threads_spinBox")
        self.threads_spinBox.setMaximumSize(QSize(16777215, 22))
        self.threads_spinBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.threads_spinBox.setStyleSheet(u"QSpinBox{\n"
"		background-color: #ececec; \n"
"		margin-left:10px;\n"
"\n"
"		width:25px;\n"
"		height:18px;\n"
"		padding-left:5px;\n"
"		border:1px solid gray\n"
"		}\n"
"\n"
"QSpinBox::down-button  {\n"
"	background-color: rgb(105, 105, 105);	\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"\n"
"QSpinBox::up-button  {\n"
"	background-color: rgb(105, 105, 105);	\n"
"		image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"		width:15px;\n"
"		height:10px;\n"
"		}\n"
"QSpinBox::focus{\n"
"	border:1px solid  rgb(121,121, 121);\n"
"}\n"
"\n"
"QSpinBox::up-arrow:hover { 	\n"
"		background-color: rgb(21,21,21);	\n"
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
"		background-"
                        "color: rgb(71, 71, 71);\n"
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


        self.scraping_setting_frame.addWidget(self.frame_12)


        self.verticalLayout_13.addLayout(self.scraping_setting_frame)

        self.frame_30 = QFrame(self.frame_center)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));\n"
"border:none")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_30)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.frame_19 = QFrame(self.frame_30)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, -1, 7)
        self.horizontalSpacer_5 = QSpacerItem(175, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.frame_24 = QFrame(self.frame_19)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy3)
        self.frame_24.setMaximumSize(QSize(16777215, 41))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, 9)
        self.stop_scraping_btn = QPushButton(self.frame_24)
        self.stop_scraping_btn.setObjectName(u"stop_scraping_btn")
        self.stop_scraping_btn.setMinimumSize(QSize(200, 40))
        self.stop_scraping_btn.setMaximumSize(QSize(200, 40))
        font9 = QFont()
        font9.setFamily(u"Segoe UI Semibold")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.stop_scraping_btn.setFont(font9)
        self.stop_scraping_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_scraping_btn.setStyleSheet(u"QPushButton{ \n"
"border:2px solid #7E7E7E;\n"
"	border-top:0px;\n"
"	background-color:  #CECECE;\n"
"color: #545454;\n"
"	font-weight: bold;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QPushButton::hover{ \n"
"	background-color: rgb(220,220,220);\n"
"	color: rgb(57, 57, 57);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(210, 210, 210);\n"
"}")

        self.horizontalLayout_23.addWidget(self.stop_scraping_btn)

        self.start_scraping_btn = QPushButton(self.frame_24)
        self.start_scraping_btn.setObjectName(u"start_scraping_btn")
        self.start_scraping_btn.setMinimumSize(QSize(200, 40))
        self.start_scraping_btn.setMaximumSize(QSize(200, 40))
        self.start_scraping_btn.setFont(font9)
        self.start_scraping_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_scraping_btn.setStyleSheet(u"QPushButton{ \n"
"border:2px solid #7E7E7E;\n"
"	border-top:0px;\n"
"	background-color:  #CECECE;\n"
"color: #545454;\n"
"	font-weight: bold;\n"
"	border-bottom-left-radius:5px;\n"
"	border-bottom-right-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{ \n"
"	background-color: rgb(220,220,220);\n"
"	color: rgb(57, 57, 57);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(210, 210, 210);\n"
"}")

        self.horizontalLayout_23.addWidget(self.start_scraping_btn)


        self.horizontalLayout_8.addWidget(self.frame_24)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addWidget(self.frame_19)


        self.verticalLayout_13.addWidget(self.frame_30)

        self.central_panel_layout = QHBoxLayout()
        self.central_panel_layout.setObjectName(u"central_panel_layout")

        self.verticalLayout_13.addLayout(self.central_panel_layout)

        self.verticalLayout_13.setStretch(2, 10)

        self.horizontalLayout_6.addWidget(self.frame_center)

        self.horizontalLayout_6.setStretch(1, 120)

        self.verticalLayout.addWidget(self.frame_3)

        self.bottom_slider = QFrame(self.frame)
        self.bottom_slider.setObjectName(u"bottom_slider")
        self.bottom_slider.setMinimumSize(QSize(0, 18))
        self.bottom_slider.setMaximumSize(QSize(16777215, 18))
        self.bottom_slider.setStyleSheet(u"background-color: rgb(74, 74, 74);")
        self.bottom_slider.setFrameShape(QFrame.StyledPanel)
        self.bottom_slider.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.bottom_slider)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom = QFrame(self.bottom_slider)
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
"border:none;\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.drag_btn)


        self.horizontalLayout_7.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.bottom_slider)


        self.verticalLayout_2.addWidget(self.frame)

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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Create new cluster", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"New to Scr4p3rTube and don\u2019t \n"
"have a database to collect data?", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><br/>If you don't already have a place where to<br/>\n"
"store data, you can create one for free using<br/>\n"
"<span style=\" color:#fd7676;\">MongoDB Atlas</span> or login with your account.<br/></p>\n"
"\n"
"</body></html>", None))
        self.start_scraping_btn_2.setText(QCoreApplication.translate("MainWindow", u"Create Database", None))
        self.pushButton.setText("")
        self.channel_radioBtn.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.video_radioBtn.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.url_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link url", None))
        self.cluster_checkBox.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cluster", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Threads", None))
        self.stop_scraping_btn.setText(QCoreApplication.translate("MainWindow", u"Stop Scraping", None))
        self.start_scraping_btn.setText(QCoreApplication.translate("MainWindow", u"Start scraping", None))
        self.drag_btn.setText("")
    # retranslateUi

