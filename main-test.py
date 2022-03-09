import win32gui, win32con # Provides access to much of the Win32 API
import sys    # More system commands
import time
import random
import json   # Low-grade local storage
import os     # File access

# For PYQT5 GUI
from PyQt5.QtWidgets import *        
from PyQt5 import QtCore, QtGui, uic, QtTest
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
# from PyQt5.QLayout import *
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

from BlurWindow.blurWindow import blur

#region Classes

#region GUI classes

class ProjectSelection(QMainWindow):                  
    
    def __init__(self):
        super(ProjectSelection, self).__init__()

        self.show()
        # uic.loadUi("projectSelection.ui", self) # Loads "" scene
        uic.loadUi("arraytest.ui", self) # Loads "" scene
        self.WindowParams()

        for i in range(1):

            btn = QPushButton("OK")
            widget = QFrame()
            widget.setStyleSheet("background-color: rgb(0,255, 0);")
            widget.setFixedSize(200, 200)
            
            # layout = QGridLayout()
            layout = QVBoxLayout()

            # layout.addWidget(Panel(), 0)
            # layout.addWidget(Color('blue'))
            layout.addChildWidget(widget)
            layout.addWidget(btn)

            self.wid = QWidget()
            self.wid.setLayout(layout)

            self.wid.setParent(self.frame)

    # method for widgets
    def WindowParams(self):

        self.setWindowTitle("Project Selection")
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(800, 500)

        self.center()

    def center(self):

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class Panel(QWidget):

    def __init__(self):
        super(Panel, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("black"))
        self.setPalette(palette)
        # self.setStyleSheet("background-color: black;")
        self.setFixedSize(200, 200)
        print("s")


#endregion GUI classes

#region Library classes

#endregion Library classes

#endregion Classes

if __name__ == "__main__": # Runs only if current file was executed (Not freferenced)

    app = QApplication(sys.argv)
    ProjectSelection = ProjectSelection()
    app.exec_()