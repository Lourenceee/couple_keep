import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi

class Create(QDialog):
    def __init__(self):
        super(Create, self).__init__()
        loadUi("ui/registerFrame.ui", self)
    
    def submitFunction(self):
        pass