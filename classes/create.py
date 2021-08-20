import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi

class Create(QDialog):
    def __init__(self):
        super(Create, self).__init__()
        loadUi("ui/registerFrame.ui", self)
        self.loginFrame_createButton.clicked.connect(self.createFunction)
    
    def submitFunction(self):
        pass