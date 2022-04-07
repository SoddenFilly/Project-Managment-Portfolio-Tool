import win32gui, win32con # Provides access to much of the Win32 API
import sys    # More system commands
import time
import random
import json   # Low-grade local storage
import os     # File access
import math
import threading

# For PYQT5 GUI
from PyQt5.QtWidgets import *        
from PyQt5 import QtCore, QtGui, uic, QtTest
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
# from PyQt5.QLayout import *
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout


from pynput import mouse



class SpotWindow(QMainWindow):                  
    
    def __init__(self):
        super(SpotWindow, self).__init__()

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        time.sleep(0.1) # gives time for teminal to catch up

        # uic.loadUi("Resources/Ui/projectWindow.ui", self) # Loads "" scene
        uic.loadUi("Resources/Ui/spot.ui", self) # Loads "" scene

        # self.calculate(0)

        listener = mouse.Listener(on_move=self.CalculatePos)
        listener.start()

        self.show()

    def CalculatePos(self, mPosX, mPosY):

        # print(f"\nWinX: {self.x()}, WinY: {self.y()}")
        # print(f"MseX: {mPosX}, MseY: {mPosY}")
        # print(self.width())

        pointPosX = int(self.x()+self.width()/2)
        pointPosY = int(self.y()+self.height()/2+38)

        # print(f"\nWinX: {spotPosX}, WinY: {spotPosY}")
        print(f"MseX: {mPosX}, MseY: {mPosY}")

        mseToPnt_relDistX = mPosX-pointPosX
        mseToPnt_relDistY = mPosY-pointPosY

        # a** + b** = c**
        mseToPnt_relDistH = int((mseToPnt_relDistX**2 + mseToPnt_relDistY**2)**0.5)

        # print(mseToPnt_relDistH)

        opacityScaleFactor = mseToPnt_relDistH/500
        if opacityScaleFactor > 1:
            opacityScaleFactor = 1
        elif opacityScaleFactor < 0.01:
            opacityScaleFactor = 0.01

        # print(int(255*opacityScaleFactor))

        self.point.setStyleSheet(f"background-color: rgba(85, 0, 127, {int(255*opacityScaleFactor)}); border-radius: 21px;")

        print(self.point.x())

        # print(mouseToPoint_relativeLinearDistX, mouseToPoint_relativeLinearDistY)
        pass



if __name__ == "__main__": # Runs only if current file was executed (Not freferenced)

    app = QApplication(sys.argv)
    SpotWindow = SpotWindow()
    app.exec_()