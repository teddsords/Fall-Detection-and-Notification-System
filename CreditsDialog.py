from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_credits_Dialog(object):
    def setupUi(self, credits_Dialog):
        credits_Dialog.setObjectName("credits_Dialog")
        credits_Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(credits_Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(credits_Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 401, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(credits_Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 401, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(credits_Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 120, 401, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(credits_Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 220, 401, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(credits_Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 160, 401, 41))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.close_pushButton = QtWidgets.QPushButton(credits_Dialog)
        self.close_pushButton.setGeometry(QtCore.QRect(160, 260, 75, 23))
        self.close_pushButton.setObjectName("close_pushButton")

        self.retranslateUi(credits_Dialog)
        QtCore.QMetaObject.connectSlotsByName(credits_Dialog)

    def retranslateUi(self, credits_Dialog):
        _translate = QtCore.QCoreApplication.translate
        credits_Dialog.setWindowTitle(_translate("credits_Dialog", "Credits"))
        self.label.setText(_translate("credits_Dialog", "Fall Alert"))
        self.label_2.setText(_translate("credits_Dialog", "Developed by:"))
        self.label_3.setText(_translate("credits_Dialog", "Teddy Ordoñez Nuñez"))
        self.label_4.setText(_translate("credits_Dialog", "Version 1.0"))
        self.label_5.setText(_translate("credits_Dialog", "UNIVALI"))
        self.label_6.setText(_translate("credits_Dialog", "https://github.com/teddsords/TCC-iii"))
        self.close_pushButton.setText(_translate("credits_Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    credits_Dialog = QtWidgets.QDialog()
    ui = Ui_credits_Dialog()
    ui.setupUi(credits_Dialog)
    credits_Dialog.show()
    sys.exit(app.exec_())
