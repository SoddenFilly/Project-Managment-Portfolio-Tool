import win32gui, win32con # Provides access to much of the Win32 API
import sys    # More system commands
import time
import random
import json   # Low-grade local storage
import os     # File access
import math

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


def MatrixDimensionsSolver(totalCells, layoutWidth, cols=False):

    paddingPercentage = 10 # 10%
    
    colSize = int(layoutWidth/cols)

    cellWidth = int(colSize/(100+paddingPercentage)*100)
    cellWidth = cellWidth-(colSize-cellWidth)/cols*2
    rowSize = int(colSize/16*9)
    cellHeight = int(cellWidth/16*9)

    rows = math.ceil(totalCells/cols)
    # print(cellWidth, paddedcellWidth, maxCellsWidth, fittingPaddedCellsWidth, newcellWidth, newCellHeight)

    # print(cellWidth, cellHeight, colSize, rowSize, cols, rows)
    
    return cellWidth, cellHeight, colSize, rowSize, cols, rows


class BlankWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.wid = QWidget()
        
        self.wid.setStyleSheet("background-color: rgba(85, 85, 127, 255); border-color:rgba(0, 0, 0, 100); border-width:2px; border-style: solid;")
        # self.wid.setContentsMargins(0,0,0,0)
        self.layout.setContentsMargins(0,0,0,0) 
        self.layout.setSpacing(0)    
        self.layout.addWidget(self.wid)
        

        self.width = 0
        self.height = 0

class ProjectSelection(QMainWindow):                  
    
    def __init__(self):
        super(ProjectSelection, self).__init__()

        self.show()
        uic.loadUi("projectSelection.ui", self) # Loads "" scene
        self.WindowParams()

        self.thumbnailLayout = QGridLayout()
        self.thumbnailLayout.setContentsMargins(0,0,0,0)
        self.thumbnailLayout.setSpacing(0)
        self.thumbnailLayout_container.setLayout(self.thumbnailLayout)

        # self.blurSlider.valu/eChanged.connect(self.blurSliderFunc)
        self.scaleSlider.valueChanged.connect(self.scaleSliderFunc)

        self.blur_radius = 0
        self.scaleFactor = 1/2.4

        self.projectCount = 0
        self.projectList = []

        self.widgetSize = {"x":100, "y":0}
        
        for i in range(24):
            self.addNewBlank(self.projectCount) 
            self.projectCount += 1
        
        self.Update()

    # method for widgets
    def WindowParams(self):

        self.setWindowTitle("Project Selection")
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(800, 500)

        self.center()

    def Update(self):

        # self.blurEffect = QGraphicsBlurEffect()
        # self.blurEffect.setBlurRadius(self.blur_radius)
        # self.widget_blur.setGraphicsEffect(self.blur_effect)
        # self.frame.setGraphicsEffect(self.blurEffect)
        # self.blurEffect = QGraphicsBlurEffect()
        # self.frame_2.setGraphicsEffect(self.blurEffect)
        # self.blurEffect.setBlurRadius(self.blur_radius)

        # self.frame.setFixedSize(380*self.scaleFactor, 220*self.scaleFactor)
        # self.frame_2.setFixedSize(380*self.scaleFactor, 220*self.scaleFactor)
        # self.frame_3.setFixedSize(380*self.scaleFactor, 220*self.scaleFactor)
        
        print(self.thumbnailLayout_container.width())
        layoutWidth = self.thumbnailLayout_container.width()

        cellWidth, cellHeight, colSize, rowSize, cols, rows = MatrixDimensionsSolver(self.projectCount, self.widgetSize, layoutWidth)
        
        spacing = colSize-cellWidth
        # vSpacer = QSpacerItem(spacing, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)
        
        # self.thumbnailLayout.addItem(vSpacer, 0, 0)

        for column, widget in enumerate(self.projectList):
            widget.setFixedSize(cellWidth, cellHeight)
            
            self.thumbnailLayout.setSpacing(spacing)
            # widget.layout.setContentsMargins((layoutWidth-colSize*cols)/2, 0,0,0) \

            row = math.floor(column/cols)
            print("Row", row)

            self.thumbnailLayout.addWidget(widget, row, column-row*(cols))
            print("Column", column+1-row*(cols))
        
        vSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.thumbnailLayout.addItem(vSpacer, row, cols)
        self.thumbnailLayout.addItem(hSpacer, row+1, 0)

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def addNewBlank(self, projectCount):

        self.widget = BlankWidget(self)

        self.projectList.append(self.widget)
        # print(self.projectList)

    def blurSliderFunc(self):
        self.blur_radius = self.blurSlider.value()/2
        self.Update()

    def scaleSliderFunc(self):
        self.scaleFactor = self.scaleSlider.value()/100+0.25
        self.Update()

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

    # MatrixDimensionsSolver(7, 100, 500, 2)
    

    app = QApplication(sys.argv)
    # SplashScreen = SplashScreen()
    # SetupScene = SetupScene()
    ProjectSelection = ProjectSelection()
    app.exec_()
    # print(math.floor(10/5))