# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerdhlvbC.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView{\n"
"	border-radius:8px;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView, QHeaderView::section, QTableView QTableCornerButton:section\n"
"{\n"
"	background-color: rgb(77, 77, 77);\n"
"    color: #fff;\n"
"    gridline-color:  rgb(48, 48, 48);\n"
"\n"
"}\n"
"\n"
"QTableView::item:selected\n"
"{\n"
"	background-color: rgb(56, 56, 56);\n"
"}\n"
"\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
"QHeaderView{\n"
"font: 13px ;\n"
"color:rgb(240, 240, 240);\n"
"background-color: rgb(80, 80, 80);\n"
"}\n"
"QHeaderView::section:horizontal{\n"
"min-height:30px;\n"
"border:0;\n"
"border-bottom:1px solid rgb(195, 75, 75);\n"
"background-color: rgb(60,60,60);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"font: 13px ;\n"
"text-align:center;\n"
"}\n"
"QHeaderView::section:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"QHeaderView::section:checked{/*"
                        "\u4e0d\u53d6\u6d88\u9ad8\u4eae*/\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"QHeaderView::section:selected{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(75, 75, 75);\n"
"}\n"
"QHeaderView::section:checked:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(75, 75, 75);\n"
"}")

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Table View Pandas Dataframe", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Insert Data Frame", None))
    # retranslateUi

