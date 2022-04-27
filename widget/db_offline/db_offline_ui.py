# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db_offline_uivPmjYw.ui'
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
        Form.resize(400, 214)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.db_status_offline = QFrame(Form)
        self.db_status_offline.setObjectName(u"db_status_offline")
        self.db_status_offline.setFrameShape(QFrame.StyledPanel)
        self.db_status_offline.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.db_status_offline)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.db_status_offline)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
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
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(260, 0))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setBold(False)
        font1.setWeight(50)
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(207, 207, 207);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_13)


        self.verticalLayout_15.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.db_status_offline)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_10.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" text-decoration: underline;\">MongoDB cluster is offline</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"The data will not be saved after \n"
"the scraping process", None))
    # retranslateUi

