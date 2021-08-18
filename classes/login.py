import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi
from classes.create import Create

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("ui/loginFrame.ui", self)
        self.loginFrame_passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginFrame_loginButton.clicked.connect(self.loginFunction)        
        self.loginFrame_createButton.clicked.connect(self.createFunction)  

    def loginFunction(self):
        Loginmsg = QMessageBox()

        if self.loginFrame_usernameLineEdit.text() == "" and self.loginFrame_passwordLineEdit.text() == "":
            Loginmsg.setWindowTitle("Information")
            Loginmsg.setText("Please fill the blanks!")
            Loginmsg.setIcon(QMessageBox.Information)
            x = Loginmsg.exec_()
        elif self.loginFrame_usernameLineEdit.text() == "":
            Loginmsg.setWindowTitle("Information")
            Loginmsg.setText("Username is Empty")
            Loginmsg.setIcon(QMessageBox.Information)
            x = Loginmsg.exec_()
        elif self.loginFrame_passwordLineEdit.text() == "":
            Loginmsg.setWindowTitle("Information")
            Loginmsg.setText("Password is Empty")
            Loginmsg.setIcon(QMessageBox.Information)
            x = Loginmsg.exec_()
        elif self.loginFrame_usernameLineEdit.text() == "masie" and self.loginFrame_passwordLineEdit.text() == "jake":            
            print('Successfully logged In!!')
        elif self.loginFrame_usernameLineEdit.text() != "masie" or self.loginFrame_passwordLineEdit.text() != "jake":
            Loginmsg.setWindowTitle("Warning")
            Loginmsg.setText("Incorrect Credentials")
            Loginmsg.setIcon(QMessageBox.Critical)
            x = Loginmsg.exec_()   

    def createFunction(self):
        createL = Create()
        createFrame.addWidget(createL)
        createFrame.setCurrentIndex(createFrame.setCurrentIndex() + 1)
        pass


app = QApplication(sys.argv)
loginWindow = Login()
loginFrame = QtWidgets.QStackedWidget()
loginFrame.addWidget(loginWindow)
loginFrame.setFixedWidth(400)
loginFrame.setFixedHeight(600)
# loginFrame.setWindowFlags(QtCore.Qt.FramelessWindowHint)
# loginFrame.setAttribute(QtCore.Qt.WA_TranslucentBackground)
loginFrame.show()
app.exec()