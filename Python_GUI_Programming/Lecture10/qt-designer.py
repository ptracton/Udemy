from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import showGUI

class MainDialog(QDialog, showGUI.Ui_mainDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        #self.connect(self.showButton, SIGNAL("clicked()"), self.showMessageBox)
        self.showButton.clicked.connect(self.showMessageBox)

    def showMessageBox(self):
        QMessageBox.warning(self, "APP","Hello " + self.nameEdit.text())
        #QMessageBox.information(self, "Hello " + self.nameEdit.text())


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
