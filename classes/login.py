import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("ui/loginForm.ui", self)
        self.loginForm_passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginForm_loginButton.clicked.connect(self.loginFunction)        
    
    def loginFunction(self):
        Loginmsg = QMessageBox()

        if self.loginForm_usernameLineEdit.text() == "" and self.loginForm_passwordLineEdit.text() == "":
            Loginmsg.setWindowTitle("Information")
            Loginmsg.setText("Please fill the blanks!")
            Loginmsg.setIcon(QMessageBox.Information)
            x = Loginmsg.exec_()
        elif self.loginForm_usernameLineEdit.text() == "":
            Loginmsg.setWindowTitle("Information")
            Loginmsg.setText("Username is Empty")
            Loginmsg.setIcon(QMessageBox.Information)
            x = Loginmsg.exec_()
        elif self.loginForm_passwordLineEdit.text() == "":
            Loginmsg.setWindowTitle("Information")
            Loginmsg.setText("Password is Empty")
            Loginmsg.setIcon(QMessageBox.Information)
            x = Loginmsg.exec_()
        elif self.loginForm_usernameLineEdit.text() == "masie" and self.loginForm_passwordLineEdit.text() == "jake":            
            print('Successfully logged In!!')
        elif self.loginForm_usernameLineEdit.text() != "masie" or self.loginForm_passwordLineEdit.text() != "jake":
            Loginmsg.setWindowTitle("Warning")
            Loginmsg.setText("Incorrect Credentials")
            Loginmsg.setIcon(QMessageBox.Critical)
            x = Loginmsg.exec_()        


app = QApplication(sys.argv)
loginWindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(loginWindow)
widget.setFixedWidth(400)
widget.setFixedHeight(600)
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()
app.exec()