# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uSingle.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(423, 300)
        self.labelQuestion = QtWidgets.QLabel(Dialog)
        self.labelQuestion.setGeometry(QtCore.QRect(80, 60, 341, 101))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.labelQuestion.setFont(font)
        self.labelQuestion.setObjectName("labelQuestion")
        self.buttonYes = QtWidgets.QPushButton(Dialog)
        self.buttonYes.setGeometry(QtCore.QRect(60, 220, 75, 31))
        self.buttonYes.setObjectName("buttonYes")
        self.buttonNo = QtWidgets.QPushButton(Dialog)
        self.buttonNo.setEnabled(True)
        self.buttonNo.setGeometry(QtCore.QRect(290, 220, 75, 31))
        self.buttonNo.setObjectName("buttonNo")
        self.labelAnswer = QtWidgets.QLabel(Dialog)
        self.labelAnswer.setEnabled(True)
        self.labelAnswer.setGeometry(QtCore.QRect(100, 80, 211, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.labelAnswer.setFont(font)
        self.labelAnswer.setObjectName("labelAnswer")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Single - YesOrNo"))
        self.labelQuestion.setText(_translate("Dialog", "Are you single?"))
        self.buttonYes.setText(_translate("Dialog", "Yes"))
        self.buttonNo.setText(_translate("Dialog", "No"))
        self.labelAnswer.setText(_translate("Dialog", "I knew it! :-D"))
