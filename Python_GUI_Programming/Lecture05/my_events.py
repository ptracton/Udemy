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

        self.spinbox = QSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        # Use spinbox.setValue which is a predefined handler
        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)  # notice that no parenthesis for the setValue methods!

        self.dial.valueChanged.connect(self.print_value)

    # Docs will list parameters for a specific signal!
    def print_value(self, value):
        print ("The value is {0}".format(value))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
