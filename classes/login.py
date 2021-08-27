import sys
import mysql.connector
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi

#imports
from classes.create import Create
from database.database import mydb 

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("ui/loginFrame.ui", self)
        self.loginFrame_passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginFrame_loginButton.clicked.connect(self.dbLogin)        
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
    
    def dbLogin(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM accounts WHERE BINARY db_username = '%s' AND BINARY db_password = '%s'" % (self.loginFrame_usernameLineEdit.text(), self.loginFrame_passwordLineEdit.text())

        mycursor.execute(sql)

        if mycursor.fetchone():
            print('Successfully logged In!!')
        else:
            print('Nanik!')

    def createFunction(self):
        create = Create()
        window.addWidget(create)
        window.setFixedWidth(504)
        window.setFixedHeight(604)
        window.setCurrentIndex(window.currentIndex() + 1)


app = QApplication(sys.argv)
loginWindow = Login()
window = QtWidgets.QStackedWidget()
window.addWidget(loginWindow)
window.setFixedWidth(404)
window.setFixedHeight(604)
# window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
# window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
window.show()
app.exec()