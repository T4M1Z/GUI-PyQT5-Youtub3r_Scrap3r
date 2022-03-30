
from PyQt5.QtWidgets import QWidget
from widget.ui_left_panel import Ui_Form
import sys

class Left_Panel(QWidget):
    def __init__(self, parent):        
        super(Left_Panel, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
