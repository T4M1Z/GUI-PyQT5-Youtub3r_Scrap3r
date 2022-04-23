# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'central_panelZCWMBS.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1184, 1042)
        Form.setStyleSheet(u"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setHandleWidth(2)
        self.splitter_2.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.central_panel_frame = QFrame(self.layoutWidget)
        self.central_panel_frame.setObjectName(u"central_panel_frame")
        self.central_panel_frame.setMinimumSize(QSize(0, 300))
        self.central_panel_frame.setMaximumSize(QSize(16777215, 16777215))
        self.central_panel_frame.setStyleSheet(u"border:none;\n"
"")
        self.central_panel_frame.setFrameShape(QFrame.StyledPanel)
        self.central_panel_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.central_panel_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.central_panel_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"\n"
"\n"
"border:0px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:4px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.selenium_layout = QHBoxLayout()
        self.selenium_layout.setObjectName(u"selenium_layout")
        self.selenium_layout.setContentsMargins(-1, 4, -1, -1)

        self.horizontalLayout_11.addLayout(self.selenium_layout)


        self.horizontalLayout_14.addWidget(self.frame_2)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.gridLayout_3.addWidget(self.central_panel_frame, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.layoutWidget)
        self.horizontalLayoutWidget_2 = QWidget(self.splitter_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.layout_monitoring = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_monitoring.setObjectName(u"layout_monitoring")
        self.layout_monitoring.setContentsMargins(0, 0, 0, 0)
        self.scraping_monitoring_frame = QFrame(self.horizontalLayoutWidget_2)
        self.scraping_monitoring_frame.setObjectName(u"scraping_monitoring_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scraping_monitoring_frame.sizePolicy().hasHeightForWidth())
        self.scraping_monitoring_frame.setSizePolicy(sizePolicy)
        self.scraping_monitoring_frame.setMinimumSize(QSize(0, 0))
        self.scraping_monitoring_frame.setStyleSheet(u"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));")
        self.scraping_monitoring_frame.setFrameShape(QFrame.StyledPanel)
        self.scraping_monitoring_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.scraping_monitoring_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.scraping_monitoring_frame)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(2)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_18 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.left_bottom_frame = QFrame(self.layoutWidget1)
        self.left_bottom_frame.setObjectName(u"left_bottom_frame")
        self.left_bottom_frame.setMinimumSize(QSize(230, 0))
        self.left_bottom_frame.setStyleSheet(u"\n"
"border:0px;")
        self.left_bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.left_bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.left_bottom_frame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(2, 2, 2, 2)
        self.frame_23 = QFrame(self.left_bottom_frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:4px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.frame_23)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"QTextBrowser{\n"
"	border:none;\n"
"		color: rgb(181, 181, 181);\n"
"	border-radius:8px;\n"
"	background-color: rgb(77, 77, 77);\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"	padding-bottom:5px;\n"
"	padding-right:10px;\n"
"}")

        self.horizontalLayout_25.addWidget(self.textBrowser)


        self.horizontalLayout_24.addWidget(self.frame_23)


        self.horizontalLayout_18.addWidget(self.left_bottom_frame)

        self.splitter.addWidget(self.layoutWidget1)
        self.horizontalLayoutWidget = QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.right_bottom_frame = QFrame(self.horizontalLayoutWidget)
        self.right_bottom_frame.setObjectName(u"right_bottom_frame")
        sizePolicy1.setHeightForWidth(self.right_bottom_frame.sizePolicy().hasHeightForWidth())
        self.right_bottom_frame.setSizePolicy(sizePolicy1)
        self.right_bottom_frame.setMinimumSize(QSize(230, 0))
        self.right_bottom_frame.setStyleSheet(u"\n"
"border:0px;")
        self.right_bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.right_bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.right_bottom_frame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(2, 2, 2, 2)
        self.frame_28 = QFrame(self.right_bottom_frame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"QFrame #frame_28{\n"
"background-color: #4A4A4A;\n"
"border:2px solid #7E7E7E;\n"
"border-radius:4px;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_28)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        font = QFont()
        font.setFamily(u"Roboto")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	border-radius:8px;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget, QHeaderView::section, QTableWidget QTableCornerButton:section\n"
"{\n"
"	background-color: rgb(77, 77, 77);\n"
"    color: #fff;\n"
"    gridline-color:  rgb(48, 48, 48);\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected\n"
"{\n"
"	background-color: rgb(56, 56, 56);\n"
"}\n"
"\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
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
"QHeaderView::section:"
                        "checked{/*\u4e0d\u53d6\u6d88\u9ad8\u4eae*/\n"
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
"}\n"
"")
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_30.addWidget(self.tableWidget)


        self.horizontalLayout_29.addWidget(self.frame_28)


        self.horizontalLayout.addWidget(self.right_bottom_frame)

        self.splitter.addWidget(self.horizontalLayoutWidget)

        self.horizontalLayout_3.addWidget(self.splitter)


        self.layout_monitoring.addWidget(self.scraping_monitoring_frame)

        self.splitter_2.addWidget(self.horizontalLayoutWidget_2)

        self.horizontalLayout_2.addWidget(self.splitter_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-"
                        "bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-- START SCRAPING --	</p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Link url", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Title", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Views", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

