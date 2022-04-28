from matplotlib.widgets import Widget
from modules import *
# from PyQt5.QtChart import QCandlestickSeries, QCandlestickSet, QChart, QChartView, QLineSeries
from PyQt5.QtWidgets import QFileDialog, QFrame, QGraphicsOpacityEffect, QHBoxLayout, QLabel, QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPainterPath, QPalette,QMovie, QPixmap,QPainter, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer, QEasingCurve, pyqtSignal
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QPoint, QTimeLine

class Animation:
    def __init__(self, ui, c_panel=None):
        self.ui = ui
        self.c_panel = c_panel

    def animation_top_panel(self):
        self.top_panel = QtCore.QPropertyAnimation(self.ui.scraping_setting_frame, b"maximumHeight")                
        if self.ui.scraping_setting_frame.height() > 0:
            h1, h2 = 80,0
        else:
            h1, h2 = 0,80
        self.top_panel.setDuration(500)
        self.top_panel.setStartValue(h1)
        self.top_panel.setEndValue(h2)
        self.top_panel.start()

    def animation_bottom_panel(self, param = None):
        self.bottom_panel = QtCore.QPropertyAnimation(self.c_panel.ui.scraping_monitoring_frame, b"maximumHeight")
        if param: pass
        else:
            if self.c_panel.ui.scraping_monitoring_frame.height() > 0:
                h1, h2 = 800,0
            else:
                h1, h2 = 0,800
            self.bottom_panel.setDuration(400)
            self.bottom_panel.setStartValue(h1)
            self.bottom_panel.setEndValue(h2)
            self.bottom_panel.start()

    def animation_central_panel(self, param = None):
        self.central_panel = QtCore.QPropertyAnimation(self.c_panel.ui.central_panel_frame, b"maximumHeight")
        if param:
            self.c_panel.ui.central_panel_frame.setMinimumHeight(300)
            h1, h2 = 0,10000
        else:
            self.c_panel.ui.central_panel_frame.setMinimumHeight(0)
            h1, h2 = self.c_panel.ui.central_panel_frame.height(),0

        self.central_panel.setDuration(400)
        self.central_panel.setStartValue(h1)
        self.central_panel.setEndValue(h2)
        self.central_panel.start()

    def animation_bottom_left_panel(self, param = None):
        print(self.c_panel.ui.splitter_2.height())
        print(self.c_panel.ui.splitter_2.width())
        self.bottom_left_panel = QtCore.QPropertyAnimation(self.c_panel.ui.left_bottom_frame, b"maximumWidth")
        
        if param:
            self.c_panel.ui.left_bottom_frame.setMinimumWidth(400)
            h1, h2 = 0,10000
        else:
            if self.c_panel.ui.left_bottom_frame.width() > 0:
                self.c_panel.ui.left_bottom_frame.setMinimumWidth(0)
                h1, h2 = self.c_panel.ui.left_bottom_frame.width(),0
            else:
                self.c_panel.ui.left_bottom_frame.setMinimumWidth(400)
                h1, h2 = 0,800
        self.bottom_left_panel.setStartValue(h1)
        self.bottom_left_panel.setEndValue(h2)
        self.bottom_left_panel.start()

    def show_left_panel(self):
        if self.ui.left_panel.width() > 0:
            self.left_panel_animation = QtCore.QPropertyAnimation(self.ui.left_panel, b"maximumWidth")
            self.ui.left_panel_btn.setStyleSheet(stylesheet.left_panel_btn("right"))
            h1, h2 = 340,0
            self.left_panel_animation.setDuration(300)
            self.left_panel_animation.setStartValue(h1)
            self.left_panel_animation.setEndValue(h2)
            self.left_panel_animation.start()
        else:
            self.left_panel_animation = QtCore.QPropertyAnimation(self.ui.left_panel, b"maximumWidth")
            h1, h2 = 0,340
            self.ui.left_panel_btn.setStyleSheet(stylesheet.left_panel_btn("left"))
            self.left_panel_animation.setDuration(300)
            self.left_panel_animation.setStartValue(h1)
            self.left_panel_animation.setEndValue(h2)
            self.left_panel_animation.start()

    def animation_db_settings_frame(self):
        if self.ui.db_settings_frame.height() > 0:
            self.left_panel_animation = QtCore.QPropertyAnimation(self.ui.db_settings_frame, b"maximumHeight")
            h1, h2 = self.ui.db_settings_frame.height(),0
            self.left_panel_animation.setDuration(750)
            self.left_panel_animation.setStartValue(h1)
            self.left_panel_animation.setEndValue(h2)
            self.left_panel_animation.start()
        else:
            self.left_panel_animation = QtCore.QPropertyAnimation(self.ui.db_settings_frame, b"maximumHeight")
            h1, h2 = 0,450
            self.left_panel_animation.setDuration(750)
            self.left_panel_animation.setStartValue(h1)
            self.left_panel_animation.setEndValue(h2)
            self.left_panel_animation.start()

    def animation_channel_data_frame(self):
        if self.ui.channel_data_frame.width() > 0:
            self.channel_data_frame_animation = QtCore.QPropertyAnimation(self.ui.channel_data_frame, b"maximumWidth")
            h1, h2 = 237,0
            self.channel_data_frame_animation.setDuration(300)
            self.channel_data_frame_animation.setStartValue(h1)
            self.channel_data_frame_animation.setEndValue(h2)
            self.channel_data_frame_animation.start()
        else:
            self.channel_data_frame_animation = QtCore.QPropertyAnimation(self.ui.channel_data_frame, b"maximumWidth")
            h1, h2 = 0,237
            self.channel_data_frame_animation.setDuration(300)
            self.channel_data_frame_animation.setStartValue(h1)
            self.channel_data_frame_animation.setEndValue(h2)
            self.channel_data_frame_animation.start()


# Fading bewtween stackedwidget page
class FaderWidget(QWidget):

    def __init__(self, old_widget, new_widget):
        QWidget.__init__(self, new_widget)
        
        self.old_pixmap = QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)
        self.pixmap_opacity = 1.0
        
        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(833)
        self.timeline.start()
        
        self.resize(new_widget.size())
        self.show()
    
    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()
    
    def animate(self, value):
        self.pixmap_opacity = 1.0 - value
        self.repaint()


        

