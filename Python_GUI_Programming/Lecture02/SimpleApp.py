
##
## Usage: python3 SimpleApp.py hh:mm <optional string>
##

##
## This is a BAD way to import modules!
##
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import time


##
## Always pass in sys.argv
##
app = QApplication(sys.argv)

##
## Time the clock should pop up, could use Time but we want to learn QT
##
due = QTime.currentTime()

##
## Optional parameter
##
message = "Alert"

try:
    if (len(sys.argv) < 2):
        raise ValueError

    hours, minutes = sys.argv[1].split(':')  ## hours and minutes are strings
    due = QTime(int(hours), int(minutes))
    if not due.isValid():
        raise ValueError

    if (len(sys.argv) > 2):
        message = ' '.join(sys.argv[2:])

except:
    print ("Usage: python3 SimpleApp.py hh:mm optional message")
    sys.exit(0)

while QTime.currentTime() < due:
    time.sleep(5)

##
## Label is simple static text
##
label = QLabel('<font color=red size=72>'+message+'</font>')
label.setWindowFlags(Qt.SplashScreen)
label.show()

##
## Ticking clock, set up things for regular intervals
## First parameter is in milliseconds
QTimer.singleShot(10000, app.quit)
app.exec_()