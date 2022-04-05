from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from widget.central_panel.central_panel_ui import Ui_Form
import sys

class CenterPanel(QWidget):
    # Globals
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)




# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     # QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
#     # QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
#     window = CenterPanel()

#     sys.exit(app.exec_())

