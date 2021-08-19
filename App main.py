# importing GUI
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from MainWindow import Ui_MainWindow
from CreditsDialog import Ui_credits_Dialog
from RegisterContactDialog import Ui_Register_Contact_Dialog

#importing libraries
import sys

class CreditsDialog(QDialog):
    def __init__(self):
        super(CreditsDialog, self).__init__()
        self.ui = Ui_credits_Dialog()
        self.ui.setupUi(self)

        # Defining function to be called when the close button is clicked
        self.ui.close_pushButton.clicked.connect(self.reject)
        

class RegisterContactDialog(QDialog):
    def __init__(self):
        super(RegisterContactDialog, self).__init__()
        self.ui = Ui_Register_Contact_Dialog()
        self.ui.setupUi(self)  

        # Defining function to be called when the close button is clicked
        self.ui.cancel_pushButton.clicked.connect(self.reject)     

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Defining functions to be called whenever a button is clicked
        self.ui.credits_pushButton.clicked.connect(self.openCreditsDialog)
        self.ui.registerPerson_pushButton.clicked.connect(self.openRegisterContactDialog)


    def openCreditsDialog(self):
        credits = CreditsDialog()
        credits.show()

        if credits.exec_():
            sys.exit(credits.exec_())

    def openRegisterContactDialog(self):
        registerContact = RegisterContactDialog()
        registerContact.show()

        if registerContact.exec_():
            sys.exit(registerContact.exec_())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
