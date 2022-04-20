# from PyQt5.QtChart import (QBarCategoryAxis, QBarSeries, QBarSet, QBoxPlotSeries, QCategoryAxis, QBoxSet, QDateTimeAxis, QLegend,
#                             QLogValueAxis, QPercentBarSeries, QPieSeries, QScatterSeries, QSplineSeries, QStackedBarSeries, QValueAxis)
from PyQt5.QtCore import QLocale, QPointF, QRandomGenerator
from PyQt5.QtGui import QGradient, QImage, QPaintEngine, QPainter, QPen
import matplotlib
from main import *
from ui import stylesheet   
import random
import math

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True



class UIFunctions(MainWindow): 
    GLOBAL_TITLE_BAR = True
    GLOBAL_STATE = 0

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        global GLOBAL_TITLE_BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # else:
        #     self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            # self.ui.frame.setMinimumHeight(42)

        ## SHOW ==> DROP SHADOW
        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setOffset(5.0)
        # self.shadow.setColor(QColor(0, 0, 0, 100))
        # self.shadow.setBlurRadius(5.0)
        # self.setGraphicsEffect(self.shadow)

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self.ui.frame)
        self.shadow.setOffset(5.0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.shadow.setBlurRadius(5.0)
        self.setGraphicsEffect(self.shadow)

        # ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())
        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_resize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        
        
    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self,x=0 ,y=0):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.ui.frame.layout().setContentsMargins(0,0,0,0)
            self.ui.drag_btn.setDisabled(True)
            self.showMaximized()
            a,b,c,d,e,f = stylesheet.radius_maximize("0")
            self.ui.btn_close.setStyleSheet(a)
            self.ui.frame_btn.setStyleSheet(b)
            self.ui.window_btn.setStyleSheet(c)
            self.ui.frame_top.setStyleSheet(d)
            self.ui.page_1_title.setStyleSheet(e)
            self.ui.title_frame.setStyleSheet(f)
            GLOBAL_STATE = 1
        else:
            GLOBAL_STATE = 0
            self.ui.frame.layout().setContentsMargins(0,0,9,9)
            self.ui.drag_btn.setDisabled(False)
            self.showNormal()
            a,b,c,d,e,f = stylesheet.radius_maximize("10")
            self.ui.btn_close.setStyleSheet(a)
            self.ui.frame_btn.setStyleSheet(b)
            self.ui.window_btn.setStyleSheet(c)
            self.ui.frame_top.setStyleSheet(d)
            self.ui.page_1_title.setStyleSheet(e)
            self.ui.title_frame.setStyleSheet(f)
            self.resize(self.width(), self.height())
            self.move(x-500,y)

    ## ==> RETURN STATUS
    def returStatus():
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> END Maximize/Restore GUI ##
