#
# QFileDialog is a built in dialog.  makes for standard way to open files
#

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

__appname__ = "Eight Video"


class Program(QDialog):
    def __init__(self, parent = None):
        super(Program, self).__init__(parent)

        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close ...")

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)

        self.setLayout(layout)

        openButton.clicked.connect(self.open)


    def open(self):
        '''
        Called when open button emits clicked
        '''
        dir = "."

        ##PySide returns a tuple, PyQT returns a QString
        fileObj = QFileDialog.getOpenFileName(parent=self, caption="CAPTION", directory = dir, filter="Text Files (*.txt)")
        print (fileObj)
        print (type(fileObj))




app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()


