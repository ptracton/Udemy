from PySide.QtCore import *
from PySide.QtGui import *
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

        # Line edit is a window that allows inputting a single line of text
        # Text edit is a window that allows inputting multiple lines of text

        self.resultsList = QTextBrowser()
        self.resultsInput = QLineEdit("Enter an expression and press return "
                                      "key")


        # All GUI elements inherit from QWidget gives them all certain
        # properties

        # Layouts are how widgets are arranged
        # Using a vertical box
        layout = QVBoxLayout()
        layout.addWidget(self.resultsList)
        layout.addWidget(self.resultsInput)
        self.setLayout(layout)
        self.resultsInput.selectAll()
        self.resultsInput.setFocus()

        # Signals is a way to connect actions and methods to handle them
        # This is a signal watching for a return key being pressed.  When it
        # happens it will call self.compute method

        # This is the old style and is deprecated
        #self.connect(self.resultsInput, SIGNAL('returnPressed()'),
        # self.compute())

        # This is the new style of doing this,
        self.resultsInput.returnPressed.connect(self.compute)


        pass

    def compute(self):
        try:
            text = self.resultsInput.text()
            self.resultsList.append('{0}=<b>{1}</b>'.format(text, eval(text)))
        except:
            self.resultsList.append('<font color=red><b>Expression '
                                    'Invalid</b></font>')
        pass

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()