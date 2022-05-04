import win32gui, win32con # Provides access to much of the Win32 API
import sys    # More system commands
import time
import random
import json   # Low-grade local storage
import os     # File access

# For PYQT5 GUI
from PyQt5.QtWidgets import *              
from PyQt5 import QtCore, QtGui, uic, QtTest, QtWidgets, QtWebEngineWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

class Scene(QMainWindow): # Main scene class that can be repurposed into any menu
    
    def __init__(self):
        super(Scene, self).__init__()

        # For splash-screen type windows
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show() # Sends GUI data to window

        self.fileLocationPath = os.path.dirname(os.path.realpath(__file__)) # Gets files current full directory
        
        uic.loadUi("Resources/Ui/HTML_window.ui", self) # Loads "" scene

        self.InjectPage()

    def InjectPage(self):

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0) 
        self.layout.setSpacing(0)   
        self.pageContainer.setLayout(self.layout)

        self.page = QWidget()
        self.centralwidget.setObjectName("page")

        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.page)

        self.webEngineView.load(QtCore.QUrl("C:/Users/aidan/Dev_Files/Python/Projects/Project-Management-Portfolio-Tool/boilerplate - example - test files/diag.html"))
        self.layout.addWidget(self.webEngineView)

if __name__ == "__main__": # Runs only if current file was executed (Not freferenced)

    app = QApplication(sys.argv)
    GUIWindow = Scene()
    app.exec_()