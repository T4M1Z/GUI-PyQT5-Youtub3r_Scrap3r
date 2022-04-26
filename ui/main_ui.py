# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'third_gui_style_upxEvUaO.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(1209, 820)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 820))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Oswald ExtraLight")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"border-radius: 3px;\n"
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
"	background: none;\n"
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
"	background: none;\n"
""
                        "}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: rgb(77, 77, 77);\n"
"	width:10px;\n"
" }\n"
"\n"
"/*  HANDLE BAR horiz:vertical */\n"
"QScrollBar::handle:vertical {	\n"
"	background: rgb(49, 49, 49);\n"
"	border-radius: 6px;\n"
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
"	background: none;\n"
"border-radius: 3px;\n"
"width:0px;\n"
"}\n"
"\n"
"\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background: none;\n"
"border-radius: 3px;\n"
"width:0px;\n"
"}\n"
"\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QMenu{\n"
" background: blue;\n"
""
                        "                border: 2px solid red;\n"
"                border-radius: 6px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightgray;\n"
"\n"
"}\n"
"\n"
"QMenu::item {\n"
"	background-color: rgb(181, 181, 181);\n"
"	color: rgb(71, 71, 71);\n"
"}\n"
"\n"
" QMenu::item:selected{\n"
"	background-color: rgb(81, 81, 81);\n"
"	color: rgb(211, 211, 211);\n"
" } \n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"border:none")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame #Frame{\n"
"border:none;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));\n"
"border-bottom-left-radius:3px;\n"
"}")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 9, 9)
        self.frame_top = QFrame(self.frame)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 30))
        self.frame_top.setMaximumSize(QSize(16777215, 30))
        self.frame_top.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"border:0px;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"")
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
        self.window_btn.setMinimumSize(QSize(120, 33))
        self.window_btn.setMaximumSize(QSize(120, 30))
        self.window_btn.setStyleSheet(u"	background-color: rgb(59, 59, 59);\n"
"border:0px;\n"
"border-top-right-radius: 10px;")
        self.window_btn.setFrameShape(QFrame.StyledPanel)
        self.window_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.window_btn)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_btn = QFrame(self.window_btn)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(0, 32))
        self.frame_btn.setMaximumSize(QSize(16777215, 32))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.btn_resize.sizePolicy().hasHeightForWidth())
        self.btn_resize.setSizePolicy(sizePolicy1)
        self.btn_resize.setMinimumSize(QSize(0, 0))
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
        self.btn_resize.setIconSize(QSize(14, 14))

        self.horizontalLayout_4.addWidget(self.btn_resize)

        self.btn_close = QPushButton(self.frame_btn)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(0, 0))
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
"	background-color: rgb(195, 92, 92);\n"
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
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 15, 15, 15)
        self.frame_25 = QFrame(self.frame_3)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 740))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, -1, 0, -1)
        self.frame_23 = QFrame(self.frame_25)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 725))
        self.frame_23.setStyleSheet(u"QFrame #frame_23{\n"
"border-right: 4px solid black;\n"
"border-bottom: 10px solid black;\n"
"border-right-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(40,40,40), stop: 1 rgba(0, 0, 0,0));\n"
"border-bottom-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(40,40,40), stop: 1 rgba(0, 0, 0,0));\n"
"\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.left_panel = QFrame(self.frame_23)
        self.left_panel.setObjectName(u"left_panel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.left_panel.sizePolicy().hasHeightForWidth())
        self.left_panel.setSizePolicy(sizePolicy3)
        self.left_panel.setMinimumSize(QSize(0, 0))
        self.left_panel.setMaximumSize(QSize(330, 16777215))
        self.left_panel.setStyleSheet(u"QFrame #left_panel{\n"
"background-color: #616161\n"
"}")
        self.left_panel.setFrameShape(QFrame.StyledPanel)
        self.left_panel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_panel)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.frame_4 = QFrame(self.left_panel)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 230))
        self.frame_4.setMaximumSize(QSize(330, 230))
        self.frame_4.setStyleSheet(u"QFrame #frame_4{\n"
"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:3px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 4)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 3)
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
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(8)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color:white")

        self.horizontalLayout_11.addWidget(self.label_6)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 2, -1, -1)
        self.start_scraping_btn_2 = QPushButton(self.frame_11)
        self.start_scraping_btn_2.setObjectName(u"start_scraping_btn_2")
        self.start_scraping_btn_2.setMinimumSize(QSize(170, 38))
        self.start_scraping_btn_2.setMaximumSize(QSize(170, 38))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setWeight(75)
        self.start_scraping_btn_2.setFont(font6)
        self.start_scraping_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_scraping_btn_2.setStyleSheet(u"QPushButton{ \n"
"border:2px solid #7E7E7E;\n"
"\n"
"	background-color:  #CECECE;\n"
"color: #545454;\n"
"	font-weight: bold;\n"
"	border-radius:5px;\n"
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

        self.frame_5 = QFrame(self.left_panel)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(330, 200))
        self.frame_5.setStyleSheet(u"QFrame #frame_5{\n"
"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:3px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 5, -1, -1)
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color:White")

        self.horizontalLayout_14.addWidget(self.label_7)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 0, 0, 4)
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamily(u"Segoe UI Semibold")
        font7.setPointSize(9)
        font7.setBold(False)
        font7.setUnderline(False)
        font7.setWeight(50)
        self.label_8.setFont(font7)
        self.label_8.setStyleSheet(u"color:white")

        self.horizontalLayout_13.addWidget(self.label_8)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 17))
        self.frame_15.setMaximumSize(QSize(16777215, 17))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 4, 9, -1)
        self.pushButton_2 = QPushButton(self.frame_15)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)
        self.pushButton_2.setMinimumSize(QSize(10, 10))
        self.pushButton_2.setMaximumSize(QSize(10, 10))
        font8 = QFont()
        font8.setFamily(u"Constantia")
        font8.setPointSize(7)
        self.pushButton_2.setFont(font8)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(90, 90, 90);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"padding-left:1px;\n"
"padding-bottom:1px;\n"
"}\n"
"\n"
"\n"
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

        self.verticalLayout_7.addWidget(self.pushButton_2)


        self.horizontalLayout_13.addWidget(self.frame_15)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.frame_20 = QFrame(self.frame_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, 15, 0)
        self.url_Input_2 = QLineEdit(self.frame_20)
        self.url_Input_2.setObjectName(u"url_Input_2")
        self.url_Input_2.setMinimumSize(QSize(160, 30))
        self.url_Input_2.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(9)
        font9.setBold(False)
        font9.setWeight(50)
        self.url_Input_2.setFont(font9)
        self.url_Input_2.setCursor(QCursor(Qt.IBeamCursor))
        self.url_Input_2.setStyleSheet(u"QLineEdit{\n"
"background-color:  rgb(214, 214, 214);\n"
"color: #545454;\n"
"border: 1px solid  #ffffff;\n"
"border-radius:2px;\n"
"padding-left:7px;\n"
"}\n"
"\n"
"QLineEdit::hover{background-color:  rgb(210, 210, 210);}\n"
"\n"
"QLineEdit::focus{\n"
"	border:1px solid  rgb(121,121, 121);\n"
"}")

        self.horizontalLayout_15.addWidget(self.url_Input_2)


        self.verticalLayout_6.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_21)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(13, 4, -1, 0)
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        font10 = QFont()
        font10.setFamily(u"Segoe UI Symbol")
        font10.setPointSize(7)
        self.label_9.setFont(font10)
        self.label_9.setStyleSheet(u"color:white")

        self.verticalLayout_8.addWidget(self.label_9)


        self.verticalLayout_6.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_22)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 14, -1, -1)
        self.start_scraping_btn_3 = QPushButton(self.frame_22)
        self.start_scraping_btn_3.setObjectName(u"start_scraping_btn_3")
        self.start_scraping_btn_3.setMinimumSize(QSize(110, 35))
        self.start_scraping_btn_3.setMaximumSize(QSize(110, 35))
        font11 = QFont()
        font11.setFamily(u"Segoe UI Semibold")
        font11.setPointSize(10)
        font11.setBold(True)
        font11.setWeight(75)
        self.start_scraping_btn_3.setFont(font11)
        self.start_scraping_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_scraping_btn_3.setStyleSheet(u"QPushButton{ \n"
"border:2px solid #7E7E7E;\n"
"\n"
"	background-color:  #CECECE;\n"
"color: #545454;\n"
"	font-weight: bold;\n"
"	border-radius:5px;\n"
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

        self.verticalLayout_11.addWidget(self.start_scraping_btn_3)


        self.verticalLayout_6.addWidget(self.frame_22)

        self.verticalLayout_6.setStretch(0, 4)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.left_panel)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 242))
        self.frame_6.setStyleSheet(u"QFrame #frame_6{\n"
"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:3px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.db_channel_history = QFrame(self.frame_6)
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
        font12 = QFont()
        font12.setFamily(u"Segoe UI Semibold")
        font12.setPointSize(12)
        self.label_15.setFont(font12)
        self.label_15.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout.addWidget(self.label_15)

        self.refresh_db_btn = QPushButton(self.frame_35)
        self.refresh_db_btn.setObjectName(u"refresh_db_btn")
        self.refresh_db_btn.setMinimumSize(QSize(15, 15))
        self.refresh_db_btn.setMaximumSize(QSize(15, 15))
        self.refresh_db_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.refresh_db_btn.setStyleSheet(u"QPushButton{\n"
"image: url(:/database/icons/db/reload_db.png);\n"
"border-radius:4px;\n"
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

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)

        self.verticalLayout_18.addWidget(self.frame_35)

        self.scrollArea1 = QScrollArea(self.db_channel_history)
        self.scrollArea1.setObjectName(u"scrollArea1")
        self.scrollArea1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));")
        self.scrollArea1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea1.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.scroll_widget.setGeometry(QRect(0, 0, 296, 41))
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

        self.verticalLayout_18.addWidget(self.scrollArea1)


        self.verticalLayout_12.addWidget(self.db_channel_history)

        self.db_status_offline = QFrame(self.frame_6)
        self.db_status_offline.setObjectName(u"db_status_offline")
        self.db_status_offline.setFrameShape(QFrame.StyledPanel)
        self.db_status_offline.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.db_status_offline)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.db_status_offline)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy5)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_2)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 9, -1, 9)
        self.label_10 = QLabel(self.frame_26)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(242, 124))
        self.label_10.setMaximumSize(QSize(16777215, 150))
        self.label_10.setStyleSheet(u"QLabel{\n"
"	\n"
"	image: url(:/database/icons/db/db_s.svg);\n"
"}")

        self.horizontalLayout_20.addWidget(self.label_10)


        self.verticalLayout_14.addWidget(self.frame_26)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(260, 0))
        self.label_12.setFont(font12)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)
        self.label_13.setMinimumSize(QSize(260, 0))
        font13 = QFont()
        font13.setFamily(u"Segoe UI Semibold")
        font13.setBold(False)
        font13.setWeight(50)
        self.label_13.setFont(font13)
        self.label_13.setStyleSheet(u"color: rgb(207, 207, 207);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_13)


        self.verticalLayout_15.addWidget(self.frame_2)


        self.verticalLayout_12.addWidget(self.db_status_offline)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_18.addWidget(self.left_panel)

        self.left_panel_btn = QPushButton(self.frame_23)
        self.left_panel_btn.setObjectName(u"left_panel_btn")
        sizePolicy.setHeightForWidth(self.left_panel_btn.sizePolicy().hasHeightForWidth())
        self.left_panel_btn.setSizePolicy(sizePolicy)
        self.left_panel_btn.setMinimumSize(QSize(20, 0))
        self.left_panel_btn.setMaximumSize(QSize(20, 16777215))
        self.left_panel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.left_panel_btn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_18.addWidget(self.left_panel_btn)


        self.horizontalLayout_24.addWidget(self.frame_23)


        self.horizontalLayout_6.addWidget(self.frame_25)

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
        self.verticalLayout_13.setContentsMargins(9, 9, 0, 9)
        self.scraping_setting_frame = QFrame(self.frame_center)
        self.scraping_setting_frame.setObjectName(u"scraping_setting_frame")
        self.scraping_setting_frame.setMinimumSize(QSize(39, 0))
        self.scraping_setting_frame.setMaximumSize(QSize(16777215, 80))
        self.scraping_setting_frame.setStyleSheet(u"")
        self.scraping_setting_frame.setFrameShape(QFrame.StyledPanel)
        self.scraping_setting_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.scraping_setting_frame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, -1, -1, 0)
        self.border_scrap_setting = QFrame(self.scraping_setting_frame)
        self.border_scrap_setting.setObjectName(u"border_scrap_setting")
        self.border_scrap_setting.setMinimumSize(QSize(0, 67))
        self.border_scrap_setting.setMaximumSize(QSize(16777215, 16777215))
        self.border_scrap_setting.setStyleSheet(u"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:4px;")
        self.border_scrap_setting.setFrameShape(QFrame.StyledPanel)
        self.border_scrap_setting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.border_scrap_setting)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 0, 15, 0)
        self.frame_13 = QFrame(self.border_scrap_setting)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        font14 = QFont()
        font14.setPointSize(10)
        self.frame_13.setFont(font14)
        self.frame_13.setStyleSheet(u"border:none;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_13)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(45, 23))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(85, 255, 127);\n"
" }\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(150, 255, 134);\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(68, 162, 74);\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton)

        self.channel_radioBtn = QRadioButton(self.frame_13)
        self.channel_radioBtn.setObjectName(u"channel_radioBtn")
        self.channel_radioBtn.setMinimumSize(QSize(0, 35))
        self.channel_radioBtn.setMaximumSize(QSize(100, 35))
        font15 = QFont()
        font15.setFamily(u"Segoe UI Semibold")
        font15.setPointSize(9)
        font15.setBold(False)
        font15.setWeight(50)
        self.channel_radioBtn.setFont(font15)
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
        self.video_radioBtn.setMinimumSize(QSize(0, 35))
        self.video_radioBtn.setMaximumSize(QSize(100, 35))
        self.video_radioBtn.setFont(font15)
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
        self.url_Input.setMinimumSize(QSize(160, 35))
        self.url_Input.setMaximumSize(QSize(16777215, 35))
        self.url_Input.setFont(font9)
        self.url_Input.setCursor(QCursor(Qt.IBeamCursor))
        self.url_Input.setStyleSheet(u"QLineEdit{\n"
"background-color:  rgb(214, 214, 214);\n"
"color: #545454;\n"
"border: 1px solid  #ffffff;\n"
"border-radius:2px;\n"
"padding-left:7px;\n"
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
        self.frame_18.setMinimumSize(QSize(0, 35))
        self.frame_18.setMaximumSize(QSize(115, 35))
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
        self.cluster_checkBox.setMinimumSize(QSize(15, 15))
        self.cluster_checkBox.setMaximumSize(QSize(15, 15))
        self.cluster_checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.cluster_checkBox.setStyleSheet(u"QCheckBox{\n"
"	border:none;	\n"
"	margin-right:0px;\n"
"	border:1px solid gray;\n"
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
        self.label_3.setFont(font15)
        self.label_3.setStyleSheet(u"color: #545454;\n"
"border:none;\n"
"")

        self.horizontalLayout_17.addWidget(self.label_3)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 3)

        self.horizontalLayout_12.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 35))
        self.frame_17.setMaximumSize(QSize(115, 35))
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
        self.label_2.setMinimumSize(QSize(65, 0))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setFont(font15)
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

        self.horizontalLayout_12.setStretch(2, 2)

        self.verticalLayout_9.addWidget(self.frame_13)


        self.horizontalLayout_29.addWidget(self.border_scrap_setting)


        self.verticalLayout_13.addWidget(self.scraping_setting_frame)

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
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setMaximumSize(QSize(16777215, 41))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, 9)
        self.stop_scraping_btn = QPushButton(self.frame_24)
        self.stop_scraping_btn.setObjectName(u"stop_scraping_btn")
        self.stop_scraping_btn.setMinimumSize(QSize(180, 35))
        self.stop_scraping_btn.setMaximumSize(QSize(180, 35))
        self.stop_scraping_btn.setFont(font11)
        self.stop_scraping_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_scraping_btn.setStyleSheet(u"QPushButton{ \n"
"border:2px solid #7E7E7E;\n"
"\n"
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
        self.start_scraping_btn.setMinimumSize(QSize(180, 35))
        self.start_scraping_btn.setMaximumSize(QSize(180, 35))
        self.start_scraping_btn.setFont(font11)
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
        self.central_panel_layout.setSpacing(3)
        self.central_panel_layout.setObjectName(u"central_panel_layout")
        self.central_panel_layout.setContentsMargins(-1, 0, -1, -1)
        self.frame_12 = QFrame(self.frame_center)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy6)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 9, -1, 9)
        self.frame_left = QFrame(self.frame_12)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setMinimumSize(QSize(220, 550))
        self.frame_left.setMaximumSize(QSize(220, 550))
        self.frame_left.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(66, 66, 66, 255), stop:1 rgba(81, 81, 81, 255));\n"
"\n"
"border:2px solid #7E7E7E;\n"
"\n"
"border-radius:4px;\n"
"\n"
"}\n"
"")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_left)
        self.horizontalLayout_26.setSpacing(8)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_left)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 300))
        self.frame_29.setStyleSheet(u"border:none")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_29)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(12, 5, 9, 10)
        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 0))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_31)
        self.verticalLayout_17.setSpacing(8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 0, 2, 1)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(9, 7, 9, -1)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(140, 140))
        self.frame_33.setMaximumSize(QSize(140, 140))
        self.frame_33.setStyleSheet(u"\n"
"\n"
"background-color:  rgb(91, 91, 91);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_27.setSpacing(6)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(3, 3, 3, 3)
        self.profile_image = QLabel(self.frame_33)
        self.profile_image.setObjectName(u"profile_image")
        self.profile_image.setStyleSheet(u"    QLabel{\n"
"        border:2px solid rgb(90, 90, 90);\n"
"        background-color: rgb(89, 89, 89);\n"
"        border-image: url(:/channel/icons/channel/profile.jpg);\n"
"    }")

        self.horizontalLayout_27.addWidget(self.profile_image)


        self.horizontalLayout_25.addWidget(self.frame_33)


        self.verticalLayout_17.addWidget(self.frame_32)

        self.username_channel = QLineEdit(self.frame_31)
        self.username_channel.setObjectName(u"username_channel")
        self.username_channel.setMinimumSize(QSize(0, 28))
        font16 = QFont()
        font16.setFamily(u"Roboto")
        font16.setBold(False)
        font16.setWeight(50)
        self.username_channel.setFont(font16)
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
"	border:1px solid  rgb(121,121, 121);\n"
"}\n"
"\n"
"")
        self.username_channel.setFrame(True)
        self.username_channel.setAlignment(Qt.AlignCenter)
        self.username_channel.setDragEnabled(False)
        self.username_channel.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.username_channel)

        self.country_channel = QLineEdit(self.frame_31)
        self.country_channel.setObjectName(u"country_channel")
        self.country_channel.setMinimumSize(QSize(0, 28))
        self.country_channel.setFont(font16)
        self.country_channel.setStyleSheet(u"QLineEdit{\n"
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
"	border:1px solid  rgb(121,121, 121);\n"
"}\n"
"\n"
"")
        self.country_channel.setFrame(True)
        self.country_channel.setAlignment(Qt.AlignCenter)
        self.country_channel.setDragEnabled(False)
        self.country_channel.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.country_channel)

        self.totVideo_channel = QLineEdit(self.frame_31)
        self.totVideo_channel.setObjectName(u"totVideo_channel")
        self.totVideo_channel.setMinimumSize(QSize(0, 28))
        self.totVideo_channel.setFont(font16)
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
"	border:1px solid  rgb(121,121, 121);\n"
"}\n"
"\n"
"")
        self.totVideo_channel.setFrame(True)
        self.totVideo_channel.setAlignment(Qt.AlignCenter)
        self.totVideo_channel.setDragEnabled(False)
        self.totVideo_channel.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.totVideo_channel)

        self.totViews_channel = QLineEdit(self.frame_31)
        self.totViews_channel.setObjectName(u"totViews_channel")
        self.totViews_channel.setMinimumSize(QSize(0, 28))
        self.totViews_channel.setFont(font16)
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
"	border:1px solid  rgb(121,121, 121);\n"
"}\n"
"\n"
"")
        self.totViews_channel.setFrame(True)
        self.totViews_channel.setAlignment(Qt.AlignCenter)
        self.totViews_channel.setDragEnabled(False)
        self.totViews_channel.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.totViews_channel)

        self.totSubs_channel = QLineEdit(self.frame_31)
        self.totSubs_channel.setObjectName(u"totSubs_channel")
        self.totSubs_channel.setMinimumSize(QSize(0, 28))
        self.totSubs_channel.setFont(font16)
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
"	border:1px solid  rgb(121,121, 121);\n"
"}\n"
"\n"
"")
        self.totSubs_channel.setFrame(True)
        self.totSubs_channel.setAlignment(Qt.AlignCenter)
        self.totSubs_channel.setDragEnabled(False)
        self.totSubs_channel.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.totSubs_channel)

        self.joinedDate_channel = QLineEdit(self.frame_31)
        self.joinedDate_channel.setObjectName(u"joinedDate_channel")
        self.joinedDate_channel.setMinimumSize(QSize(0, 28))
        self.joinedDate_channel.setFont(font16)
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
"	border:1px solid  rgb(121,121, 121);\n"
"}\n"
"\n"
"")
        self.joinedDate_channel.setFrame(True)
        self.joinedDate_channel.setAlignment(Qt.AlignCenter)
        self.joinedDate_channel.setDragEnabled(False)
        self.joinedDate_channel.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.joinedDate_channel)

        self.frame_28 = QFrame(self.frame_31)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_31.setSpacing(4)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.social_comboBox = QComboBox(self.frame_28)
        self.social_comboBox.addItem("")
        self.social_comboBox.setObjectName(u"social_comboBox")
        self.social_comboBox.setMinimumSize(QSize(0, 28))
        self.social_comboBox.setMaximumSize(QSize(16777215, 28))
        self.social_comboBox.setFont(font16)
        self.social_comboBox.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid  rgb(91, 91, 91);\n"
"	background-color: rgb(55, 55, 55);\n"
"padding-right:10px;\n"
"	color: rgb(181, 181, 181);\n"
"padding-left:10px;\n"
"\n"
"		}\n"
"QComboBox::drop-down \n"
"{\n"
"\n"
"    border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"}\n"
"\n"
"QComboBox::focus{\n"
"	border:1px solid  rgb(121,121, 121);\n"
"\n"
"}\n"
"/* Define a new custom arrow icon for the combo box */\n"
"QComboBox::down-arrow {\n"
"	image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"\n"
"padding-right:5px;\n"
"\n"
"padding-bottom:2px;\n"
"}\n"
"\n"
"QComboBox::hover\n"
"{\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"")

        self.horizontalLayout_31.addWidget(self.social_comboBox)

        self.btn_combo_box = QPushButton(self.frame_28)
        self.btn_combo_box.setObjectName(u"btn_combo_box")
        self.btn_combo_box.setMinimumSize(QSize(28, 28))
        self.btn_combo_box.setMaximumSize(QSize(28, 28))
        font17 = QFont()
        font17.setFamily(u"Segoe UI Semibold")
        font17.setPointSize(9)
        font17.setBold(True)
        font17.setWeight(75)
        self.btn_combo_box.setFont(font17)
        self.btn_combo_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_combo_box.setStyleSheet(u"QPushButton{ \n"
"	border: 1px solid  rgb(91, 91, 91);\n"
"	background-color: rgb(58, 58, 58);\n"
"	\n"
"	image: url(:/16x16/icons/16x16/cil-hand-point-left.png);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{ \n"
"	background-color: rgb(47, 47, 47);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(50, 50, 50);\n"
"border: 1px solid  rgb(121, 121, 121);\n"
"}")

        self.horizontalLayout_31.addWidget(self.btn_combo_box)


        self.verticalLayout_17.addWidget(self.frame_28)

        self.description_channel = QTextEdit(self.frame_31)
        self.description_channel.setObjectName(u"description_channel")
        self.description_channel.setMinimumSize(QSize(0, 105))
        self.description_channel.setMaximumSize(QSize(16777215, 105))
        font18 = QFont()
        font18.setFamily(u"Roboto")
        self.description_channel.setFont(font18)
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
"	border:1px solid  rgb(121,121, 121);\n"
"}\n"
"\n"
"")
        self.description_channel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.description_channel.setReadOnly(True)
        self.description_channel.setAcceptRichText(True)
        self.description_channel.setCursorWidth(0)
        self.description_channel.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_17.addWidget(self.description_channel)


        self.verticalLayout_16.addWidget(self.frame_31)


        self.horizontalLayout_26.addWidget(self.frame_29)


        self.horizontalLayout_30.addWidget(self.frame_left)


        self.central_panel_layout.addWidget(self.frame_12)


        self.verticalLayout_13.addLayout(self.central_panel_layout)


        self.horizontalLayout_6.addWidget(self.frame_center)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_3)

        self.bottom_slider = QFrame(self.frame)
        self.bottom_slider.setObjectName(u"bottom_slider")
        self.bottom_slider.setMinimumSize(QSize(0, 18))
        self.bottom_slider.setMaximumSize(QSize(16777215, 18))
        self.bottom_slider.setStyleSheet(u"background-color: rgb(74, 74, 74);\n"
"border-bottom-left-radius:3px;\n"
"border-bottom-right-radius:3px;")
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"New to Scr4p3rTube and don\u2019t have a \n"
"database to collect data?", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body>If you don't already have a place where to store<br/>data, you can create one for free using <br><span style=\" text-decoration: underline; color:#fd7676;\">MongoDB Atlas</span> or login with your account.<br/></body></html>", None))
        self.start_scraping_btn_2.setText(QCoreApplication.translate("MainWindow", u"Create Database", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"New connection", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Paster your connection string</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.url_Input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Connection string", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ex. mongodb+srv://username:password@cluster.mongoDB...", None))
        self.start_scraping_btn_3.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Channels History</span></p></body></html>", None))
        self.refresh_db_btn.setText("")
        self.label_10.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">MongoDB cluster is offline</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"The data will not be saved after \n"
"the scraping process", None))
        self.left_panel_btn.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"clicca", None))
        self.channel_radioBtn.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.video_radioBtn.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.url_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link url", None))
        self.cluster_checkBox.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cluster", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Threads", None))
        self.stop_scraping_btn.setText(QCoreApplication.translate("MainWindow", u"Stop Scraping", None))
        self.start_scraping_btn.setText(QCoreApplication.translate("MainWindow", u"Start scraping", None))
        self.profile_image.setText("")
        self.username_channel.setInputMask("")
        self.username_channel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username_channel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.country_channel.setInputMask("")
        self.country_channel.setText(QCoreApplication.translate("MainWindow", u"Country", None))
        self.country_channel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Joined date", None))
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
        self.social_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Socials", None))

        self.btn_combo_box.setText("")
        self.description_channel.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">Channel description</span></p></body></html>", None))
        self.description_channel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Channel description", None))
        self.drag_btn.setText("")
    # retranslateUi

