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

class Scene(QMainWindow): # Main scene class that can be repurposed into any menu
    
    def __init__(self):
        super(Scene, self).__init__()

        # For splash-screen type windows
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show() # Sends GUI data to window

        self.fileLocationPath = os.path.dirname(os.path.realpath(__file__)) # Gets files current full directory
        
        # uic.loadUi(".ui", self) # Loads "" scene

class Animate: # General Animation mini-library for PYQT5 widgets

    def animate(self, target, duration): # General function that handles animation of all other  Animate functions
        
        self.anim.setEndValue(target)
        self.anim.setDuration(duration)
        self.anim.start()
        QtTest.QTest.qWait(duration)

    def value(self, target, duration, widget): # Anim setup for values (eg. text on a loading bar)
        
        self.anim = QPropertyAnimation(widget, b"value")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)

        Animate.animate(self, target, duration)

    def position(self, target, duration, widget): # Anim setup for widget position (eg. sliding button from a-b)

        self.anim = QPropertyAnimation(widget, b"pos")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        
        Animate.animate(self, target, duration)

    def opacity(self, widget, start=1, target=0.7, duration=70, reverse=True): # Anim setup for widget transparency (eg. fades, hiding/showing elemets)

        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.anim = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.anim.setStartValue(start)
        
        Animate.animate(self, target, duration)

        if reverse == True:
            self.anim = QtCore.QPropertyAnimation(self.effect, b"opacity")
            self.anim.setStartValue(target)
            Animate.animate(self, start, duration)

if __name__ == "__main__": # Runs only if current file was executed (Not freferenced)

    app = QApplication(sys.argv)
    GUIWindow = Scene()
    app.exec_()