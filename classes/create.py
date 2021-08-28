import sys
import mysql.connector
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi

#imports
from database.database import mydb 

class Create(QDialog):
    def __init__(self):
        super(Create, self).__init__()
        loadUi("ui/registerFrame.ui", self)
        self.registerFrame_submitButton.clicked.connect(self.checkingDuplicateAccounts)  
    
    def submitAccount(self):
        mycursor = mydb.cursor()
        sql = f"INSERT INTO users_accounts (db_username, db_password, db_email) VALUES ('{self.registerFrame_usernameLineEdit.text()}', '{self.registerFrame_passwordLineEdit.text()}', '{self.registerFrame_emailLineEdit.text()}')"      
        try:
            mycursor.execute(sql)
            mydb.commit()
        except:
            mydb.rollback()

        print("Data inserted")
        print(sql)
        mycursor.close()

    def checkingDuplicateAccounts(self):
        createmsg = QMessageBox()
        mycursor = mydb.cursor()
        sql = f"SELECT * from users_accounts WHERE db_username = '{self.registerFrame_usernameLineEdit.text()}' OR db_email = '{self.registerFrame_emailLineEdit.text()}'"
        mycursor.execute(sql)
        if mycursor.fetchall():
            createmsg.setWindowTitle("Warning")
            createmsg.setText("Username already exists")
            createmsg.setIcon(QMessageBox.Critical)
            x = createmsg.exec_()
        else:
            if self.registerFrame_confirmpasswordLineEdit.text() != self.registerFrame_passwordLineEdit.text():
                createmsg.setWindowTitle("Warning")
                createmsg.setText("Your password does not match")
                createmsg.setIcon(QMessageBox.Critical)
                x = createmsg.exec_()
            else:
                self.submitAccount()