
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

__appname__ = "Video 9"
class Program(QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        btn = QPushButton("Open Dialog")
        self.label1 = QLabel("Label 1 Result")
        self.label2 = QLabel("Label 2 Result")

        self.setWindowTitle(__appname__)

        layout = QVBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

        btn.clicked.connect(self.dialogOpen)

    def dialogOpen(self):
        dialog = Dialog()
        if dialog.exec_(): # Only goes into IF, if you click OK, not cancel
            self.label1.setText("Spin Box Value " + str(dialog.spinBox.value()))
            self.label2.setText("Check Box Value " + str(dialog.checkBox.isChecked()))
        else:
            QMessageBox.warning(self, __appname__, "Dialog Canceled")

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setWindowTitle("Dialog")

        self.checkBox = QCheckBox()
        self.spinBox = QSpinBox()
        buttonOK= QPushButton("OK")
        buttonCancel = QPushButton("Cancel")

        layout = QGridLayout()
        layout.addWidget(self.spinBox, 0,0)
        layout.addWidget(self.checkBox, 0,1)
        layout.addWidget(buttonOK)
        layout.addWidget(buttonCancel)
        self.setLayout(layout)

        #
        # accept, reject and done are virtual functions
        #
        #self.connect(buttonOK, SIGNAL("clicked()"), self, SLOT("accept()"))
        #self.connect(buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
        buttonOK.clicked.connect(self.accept)
        buttonCancel.clicked.connect(self.reject)




app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()
