from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import main_ui

class MainDialog(QDialog, main_ui.Ui_mainDialog):
    def __init__(self, parent = None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)



app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
