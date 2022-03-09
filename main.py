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

class SplashScreen(QMainWindow): # Main scene class that can be repurposed into any menu
    
    def __init__(self):
        super(SplashScreen, self).__init__()

        # For splash-screen type windows
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setFixedSize(400, 500)

        self.show() # Sends GUI data to window

        self.fileLocationPath = os.path.dirname(os.path.realpath(__file__)) # Gets files current full directory
        
        uic.loadUi("splashScreen.ui", self) # Loads "" scene

class SetupScene(QMainWindow):                  
    
    def __init__(self):
        super(SetupScene, self).__init__()

        self.show()
        uic.loadUi("loadPack.ui", self) # Loads "" scene
        self.WindowParams()

        # button = QPushButton("butt")

        for i in range(1):
            button = QPushButton(str(i))
            verticalSpacer = QSpacerItem(4, 4, QSizePolicy.Maximum)
            # self.verticalLayout.addItem(verticalSpacer)
            # button.setGeometry(10, 20, 200, 100)
            # button.setFixedHeight(20)
            btnHeight = 60
            button.setFixedSize(300, btnHeight)
            self.verticalLayout.addWidget(button)

            # self.layoutContainer.setFixedHeight(i*(btnHeight+15))
            self.layoutContainer.setFixedHeight(1000)
            # self.widget.addWidget(button)
        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(verticalSpacer)


    # method for widgets
    def WindowParams(self):

        self.setWindowTitle("LoadPack")
        self.setFixedSize(800, 500)
        

        self.center()
  
        # self.showMaximized()

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

class ProjectSelection(QMainWindow):                  
    
    def __init__(self):
        super(ProjectSelection, self).__init__()

        self.show()
        uic.loadUi("projectSelection.ui", self) # Loads "" scene
        self.WindowParams()

        # button = QPushButton("butt")

        # for i in range(1):
        #     button = QPushButton(str(i))
        #     verticalSpacer = QSpacerItem(4, 4, QSizePolicy.Maximum)
        #     # self.verticalLayout.addItem(verticalSpacer)
        #     # button.setGeometry(10, 20, 200, 100)
        #     # button.setFixedHeight(20)
        #     btnHeight = 60
        #     button.setFixedSize(300, btnHeight)
        #     self.verticalLayout.addWidget(button)

        #     # self.layoutContainer.setFixedHeight(i*(btnHeight+15))
        #     self.layoutContainer.setFixedHeight(1000)
        #     # self.widget.addWidget(button)
        # verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.verticalLayout.addItem(verticalSpacer)

        self.blurSlider.valueChanged.connect(self.blurSliderFunc)
        self.scaleSlider.valueChanged.connect(self.scaleSliderFunc)

        self.blur_radius = 0
        self.scaleFactor = 1/2.4

        for i in range(1):
            # btn = QPushButton("OK")
            

            layout = QGridLayout()

            # layout.addWidget(Panel(), 0)
            layout.addWidget(Color('red'))

            # self.frame_7.setLayout(layout)
            self.widget_p = QWidget()
            self.widget_p.setLayout(layout)
            # self.frame_7.setCentralWidget(widget)
            self.widget_p.setParent(self.frame_7)
            


    # method for widgets
    def WindowParams(self):

        self.setWindowTitle("Project Selection")
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(800, 500)
        # hWin = self.widget_blur.winId()
        # print(hWin)
        # blur(hWin)

        
        # self.frame_2.setBlurRadius(1)

        
        

        self.center()
  
        # self.showMaximized()


    def Update(self):

        self.blurEffect = QGraphicsBlurEffect()
        self.blurEffect.setBlurRadius(self.blur_radius)
        # self.widget_blur.setGraphicsEffect(self.blur_effect)
        self.frame.setGraphicsEffect(self.blurEffect)
        # self.blurEffect = QGraphicsBlurEffect()
        # self.frame_2.setGraphicsEffect(self.blurEffect)
        # self.blurEffect.setBlurRadius(self.blur_radius)

        self.frame.setFixedSize(380*self.scaleFactor, 220*self.scaleFactor)
        # self.frame_2.setFixedSize(380*self.scaleFactor, 220*self.scaleFactor)
        # self.frame_3.setFixedSize(380*self.scaleFactor, 220*self.scaleFactor)

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def blurSliderFunc(self):
        self.blur_radius = self.blurSlider.value()/2
        self.Update()

    def scaleSliderFunc(self):
        self.scaleFactor = self.scaleSlider.value()/100+0.25
        self.Update()
    
    def createWid(self):

        frame = QFrame(self)
        frame.setFixedSize(380, 220)

        return frame

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

#endregion Library classes

#endregion Classes

if __name__ == "__main__": # Runs only if current file was executed (Not freferenced)

    app = QApplication(sys.argv)
    # SplashScreen = SplashScreen()
    # SetupScene = SetupScene()
    ProjectSelection = ProjectSelection()
    app.exec_()