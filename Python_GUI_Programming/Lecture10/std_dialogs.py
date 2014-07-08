
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

__appname__ = "Video 10"
class Program(QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        btn = QPushButton("Open Dialog")
        self.mainSpinBox = QSpinBox()
        self.mainCheckBox = QCheckBox("Main Check Box")

        self.setWindowTitle(__appname__)

        layout = QVBoxLayout()
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckBox)
        layout.addWidget(btn)
        self.setLayout(layout)

        btn.clicked.connect(self.dialogOpen)

    def dialogOpen(self):
        initValues = {"mainSpinBox":self.mainSpinBox.value(), "mainCheckBox":self.mainCheckBox.isChecked()}
        dialog = Dialog(initValues)
        if dialog.exec_(): # Only goes into IF, if you click OK, not cancel
            self.mainSpinBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkBox.isChecked())




class Dialog(QDialog):
    def __init__(self, initValues, parent=None):
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

        self.spinBox.setValue(initValues["mainSpinBox"])
        self.checkBox.setChecked(initValues["mainCheckBox"])

        #
        # accept, reject and done are virtual functions
        #
        #self.connect(buttonOK, SIGNAL("clicked()"), self, SLOT("accept()"))
        #self.connect(buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
        buttonOK.clicked.connect(self.accept)
        buttonCancel.clicked.connect(self.reject)

    def accept(self):
        class GreaterThanFive(Exception): pass
        class IsZero(Exception): pass

        try:
            if self.spinBox.value() > 5:
                raise GreaterThanFive("Spinbox can not be greater than 5")
            elif self.spinBox.value() == 0:
                raise IsZero("Spin Box can not be 0")
            else:
                QDialog.accept(self)

        except GreaterThanFive as exc:
            QMessageBox.warning(self, __appname__,str(exc))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return False
        except IsZero as exc:
            QMessageBox.warning(self, __appname__,str(exc))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return False

        return True



app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()
