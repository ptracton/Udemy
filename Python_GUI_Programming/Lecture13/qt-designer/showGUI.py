# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created: Thu Jul 10 10:18:00 2014
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName(_fromUtf8("mainDialog"))
        mainDialog.resize(482, 122)
        self.nameEdit = QtGui.QLineEdit(mainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(50, 40, 241, 41))
        self.nameEdit.setText(_fromUtf8(""))
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.showButton = QtGui.QPushButton(mainDialog)
        self.showButton.setGeometry(QtCore.QRect(310, 50, 75, 23))
        self.showButton.setObjectName(_fromUtf8("showButton"))

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)
        mainDialog.setTabOrder(self.showButton, self.nameEdit)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "Main Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.nameEdit.setPlaceholderText(QtGui.QApplication.translate("mainDialog", "What is your name?", None, QtGui.QApplication.UnicodeUTF8))
        self.showButton.setText(QtGui.QApplication.translate("mainDialog", "Show!", None, QtGui.QApplication.UnicodeUTF8))

