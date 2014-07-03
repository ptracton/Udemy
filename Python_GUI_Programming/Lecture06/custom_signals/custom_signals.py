#
# QWidget emits Signals
# Lots of different reasons for signals, textChanged(), valueChanged(), etc...
# Unhandled signals are lost, nothing occurs
#

#
# Slots -- connect signals to slots
# A slot is any callable function/method
#
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import math


# Extend QSpinBox and add our own signals
class ZeroSpinBox(QSpinBox):
    zeros = 0

    atZero = pyqtSignal(int, int) ## This is creating a NEW signal, this is PyQT not PySide.  Does not need to have any signals

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.valueChanged.connect(self.check_zero)

    def check_zero(self, value):
        if (value == 0):
            self.zeros +=1
            self.constant = 5
            self.atZero.emit(self.zeros, self.constant)  ## Emit signal


#
# QDialog is in charge of displaying a dialog.  Used all the time!
# parent not always needed but good habit to have
#
class Form (QDialog):
    def __init__(self, parent = None):
        # super statement constructor, this is the old way
        super(Form, self).__init__(parent)

        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = ZeroSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        # Use spinbox.setValue which is a predefined handler
        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)  # notice that no parenthesis for the setValue methods!
        self.spinbox.atZero.connect(self.print_value)  ## Connect our new signal to a handler!

        #self.dial.valueChanged.connect(self.print_value)

    # Docs will list parameters for a specific signal!
    def print_value(self, zeros, constant):
        print ("The SpinBox has been 0 {0} times".format(zeros))
        print ("The Constant is {0}".format(constant))


# Signals are the way to communicate between classes and for threading

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

