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
        self.registerFrame_submitButton.clicked.connect(self.submitFunction)  
    
    def submitFunction(self):
        mycursor = mydb.cursor()
        sql = f"INSERT INTO accounts (db_username, db_password) VALUES ('{self.registerFrame_usernameLineEdit.text()}', '{self.registerFrame_passwordLineEdit.text()}')"      
        mycursor.execute(sql)
        mydb.commit()

        print(mycursor.execute(sql))