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
        Form.resize(517, 373)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_27 = QFrame(Form)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"border-radius:3px;\n"
"\n"
"border:0px;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(4, 4, 4, 4)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: rgb(66, 66, 66);\n"
"border:2px solid rgb(90, 90, 90);")
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


        self.verticalLayout.addWidget(self.frame_27)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Link url", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Title", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Views", None));
    # retranslateUi

