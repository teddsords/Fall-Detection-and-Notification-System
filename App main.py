# importing GUI
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from MainWindow import Ui_MainWindow
from CreditsDialog import Ui_credits_Dialog
from RegisterContactDialog import Ui_Register_Contact_Dialog

#importing libraries
import sys
import requests

class CreditsDialog(QDialog):
    def __init__(self):
        super(CreditsDialog, self).__init__()
        self.ui = Ui_credits_Dialog()
        self.ui.setupUi(self)

        # Defining function to be called when the close button is clicked
        self.ui.close_pushButton.clicked.connect(self.hideCreditsDialog)

    # Function to     
    def hideCreditsDialog(self):
        self.hide()

class RegisterContactDialog(QDialog):
    def __init__(self):
        super(RegisterContactDialog, self).__init__()
        self.ui = Ui_Register_Contact_Dialog()
        self.ui.setupUi(self)  

        # Defining function to be called when the close button is clicked
        self.ui.cancel_pushButton.clicked.connect(self.hideRegisterContactDialog)
        self.ui.test_pushButton.clicked.connect(self.testTelegramAlert) 

    # Function to hide Register Contact Dialog
    def hideRegisterContactDialog(self):
        self.hide()

    # Function to test the Chat ID
    def testTelegramAlert(self):
        message = 'Testing the Python script to send a private message'
        file = open('Telegram Token.txt', 'r')
        token = file.readline()
        telegramID = self.ui.telegramID_lineEdit.text()
        URL = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, telegramID, message)
        resp = requests.get(URL)
        print(resp.text)
        

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Defining functions to be called whenever a button is clicked
        self.ui.credits_pushButton.clicked.connect(self.openCreditsDialog)
        self.ui.registerPerson_pushButton.clicked.connect(self.openRegisterContactDialog)
        self.ui.close_pushButton.clicked.connect(self.closeMainwindow)

    # Functions to open other Dialogs
    def openCreditsDialog(self):
        credits = CreditsDialog()
        credits.show()

        if credits.exec_():
            sys.exit(credits.exec_())

    def openRegisterContactDialog(self):
        registerContact = RegisterContactDialog()

        if registerContact.exec_():
            sys.exit(registerContact.exec_())

    # Function to close Main Window
    def closeMainwindow(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
