# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views\ui\turf_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgTurf(object):
    def setupUi(self, dlgTurf):
        dlgTurf.setObjectName("dlgTurf")
        dlgTurf.resize(462, 479)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/small_donkey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgTurf.setWindowIcon(icon)
        self.lstTurf = QtWidgets.QListWidget(dlgTurf)
        self.lstTurf.setGeometry(QtCore.QRect(20, 90, 411, 361))
        self.lstTurf.setObjectName("lstTurf")
        self.frame = QtWidgets.QFrame(dlgTurf)
        self.frame.setGeometry(QtCore.QRect(10, 20, 431, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 20, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 68, 19))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 20, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 20, 112, 34))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(dlgTurf)
        QtCore.QMetaObject.connectSlotsByName(dlgTurf)

    def retranslateUi(self, dlgTurf):
        _translate = QtCore.QCoreApplication.translate
        dlgTurf.setWindowTitle(_translate("dlgTurf", "Bluestreets Turf"))
        self.pushButton.setText(_translate("dlgTurf", "Add"))
        self.label.setText(_translate("dlgTurf", "Turf"))
        self.pushButton_2.setText(_translate("dlgTurf", "Drop"))
        self.pushButton_3.setText(_translate("dlgTurf", "Close"))

import bst_rc
