import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi

class Create(QDialog):
    def __init__(self):
        super(Create, self).__init__()
        loadUi("ui/registerFrame.ui", self)

app = QApplication(sys.argv)
createWindow = Create()
createFrame = QtWidgets.QStackedWidget()
createFrame.addWidget(createWindow)
createFrame.setFixedWidth(400)
createFrame.setFixedHeight(600)
# createFrame.setWindowFlags(QtCore.Qt.FramelessWindowHint)
# createFrame.setAttribute(QtCore.Qt.WA_TranslucentBackground)
createFrame.show()
app.exec()