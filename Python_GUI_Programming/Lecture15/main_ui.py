# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Jul 10 11:43:42 2014
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
        mainDialog.resize(434, 119)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pumpkin_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainDialog.setWindowIcon(icon)
        self.archButton = QtGui.QPushButton(mainDialog)
        self.archButton.setGeometry(QtCore.QRect(20, 20, 101, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cheshire_cat_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.archButton.setIcon(icon1)
        self.archButton.setIconSize(QtCore.QSize(32, 32))
        self.archButton.setObjectName(_fromUtf8("archButton"))
        self.fedoraButton = QtGui.QPushButton(mainDialog)
        self.fedoraButton.setGeometry(QtCore.QRect(140, 20, 111, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/geek_zombie_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fedoraButton.setIcon(icon2)
        self.fedoraButton.setIconSize(QtCore.QSize(32, 32))
        self.fedoraButton.setObjectName(_fromUtf8("fedoraButton"))
        self.windowsButton = QtGui.QPushButton(mainDialog)
        self.windowsButton.setGeometry(QtCore.QRect(280, 20, 131, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ninja_ghost_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.windowsButton.setIcon(icon3)
        self.windowsButton.setIconSize(QtCore.QSize(32, 32))
        self.windowsButton.setObjectName(_fromUtf8("windowsButton"))

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "Pick an OS", None, QtGui.QApplication.UnicodeUTF8))
        self.archButton.setText(QtGui.QApplication.translate("mainDialog", "Load ARCH", None, QtGui.QApplication.UnicodeUTF8))
        self.fedoraButton.setText(QtGui.QApplication.translate("mainDialog", "Load Fedora", None, QtGui.QApplication.UnicodeUTF8))
        self.windowsButton.setText(QtGui.QApplication.translate("mainDialog", "Load Windows", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
