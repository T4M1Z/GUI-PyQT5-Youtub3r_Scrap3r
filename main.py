###################################################################################
##                                                                               ##
## BY: ANDREA TAMI                                                               ##
## PROJECT MADE WITH: Qt Designer and PyQT5                                      ##
## V: 1.0.0                                                                      ##
##                                                                               ##
## This project can be used freely for all uses, as long as they maintain the    ##
## respective credits only in the Python scripts, any information in the visual  ##
## interface (GUI) can be modified without any implication.                      ##
##                                                                               ##
###################################################################################

import os
import sys
from modules import *
# from PyQt5.QtChart import QCandlestickSeries, QCandlestickSet, QChart, QChartView, QLineSeries
from PyQt5.QtWidgets import QFileDialog, QFrame, QGraphicsOpacityEffect, QHBoxLayout, QLabel, QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPainterPath, QPalette, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer, QEasingCurve, pyqtSignal

from PyQt5 import QtWebEngineWidgets
class MainWindow(QMainWindow):
    # Globals

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ----- MOVE WINDOW ----- #
        def moveWindow(event):
            if UIFunctions.returStatus() == 1:
                cursor = QtGui.QCursor()
                UIFunctions.maximize_restore(self, cursor.pos().x(), cursor.pos().y())


            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.title_frame.mouseMoveEvent = moveWindow
        
        # ----------------------- # 


        # ------ FUNCTIONS ------ #
        UIFunctions.uiDefinitions(self)
        # ----------------------- #
        self.show()

        # ------ Variables ------ #
        self.door = False
        # ----------------------- #

        # --- BTN Change pages --- #
        self.ui.drag_btn.pressed.connect(self.pressed_window)
        # ------------------------ #
        self.ui.frame.setContentsMargins(2, 2, 10, 10)

        
    ########################################################################
    ## ----- Grip window Move ----- ##
    

    def mouseMoveEvent(self, event): # Mouse coordinate when Btn_drag pressed
        if self.door:
            self.resize(event.x(), event.y())
    def mouseReleaseEvent(self, event): # Btn_drag released
        self.door = False
    def pressed_window(self): # Btn_drag pressed
        self.door = True
    def mousePressEvent(self, event): # Title_fram pressed for moving window
        self.dragPos = event.globalPos()
    ## ---------------------------- ##
    ########################################################################




    def resizeEvent(self, event):
        # self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    # def resizeFunction(self):
    #     print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    # QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()

    sys.exit(app.exec_())













