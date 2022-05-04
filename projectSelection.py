#region Imports >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import win32gui, win32con # Provides access to much of the Win32 API
import sys                # More system commands
import time
import random
import json               # Low-grade local storage
import os                 # File access
import math

# For PYQT5 GUI
from PyQt5.QtWidgets import *        
from PyQt5 import QtCore, QtGui, uic, QtTest
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout

#endregion Imports <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#region General functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def MatrixDimensionsSolver(totalCells, layoutWidth, cols):

    paddingPercentage = 5 # 5%
    
    colSize = int(layoutWidth/cols)

    cellWidth = colSize/(100+paddingPercentage)*100
    cellWidth = int(cellWidth-(colSize-cellWidth)/cols*2)
    rowSize = int((colSize/16*9)+(colSize/16*9)/2)
    cellHeight = int((cellWidth/16*9)+(cellWidth/16*9)/2)
    imgHeight = int(cellWidth/16*9)

    rows = int(math.ceil(totalCells/cols))
    
    return cellWidth, cellHeight, colSize, rowSize, cols, rows, imgHeight

def RoundImgCorners(self, imgdata, imgtype ='png', size = 64):
  
    factor = 3

    image = QImage.fromData(imgdata, imgtype)
  
    image.convertToFormat(QImage.Format_ARGB32)

    out_img = QImage(image.width(), image.height(), QImage.Format_ARGB32)
    out_img.fill(Qt.transparent)

    brush = QBrush(image)

    painter = QPainter(out_img)
    painter.setBrush(brush)

    painter.setPen(Qt.NoPen)

    path = QPainterPath()
    path.moveTo(0, image.height())

    painter.drawRoundedRect(0, 0, out_img.width(), out_img.height(), out_img.width()/factor, out_img.width()/factor)
    
    painter.drawPath(path)

    painter.end()
  
    pixmap = QPixmap.fromImage(out_img)
  
    return pixmap

#endregion General functions <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#region Classes >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class SplashScreen(QMainWindow): # Main scene class that can be repurposed into any menu
    
    def __init__(self):
        super(SplashScreen, self).__init__()

        # For splash-screen type windows
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setFixedSize(400, 500)
        
        uic.loadUi("Resources/Ui/splashScreen.ui", self) # Loads "" scene

        self.show() # Sends GUI data to window

class BlankThumbnailWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0) 
        self.layout.setSpacing(0)   
        self.setLayout(self.layout)

        self.wid_img = QWidget()
        self.wid_img.setStyleSheet(f"""
        background-color: rgba(85, 85, 127, 255);
        border-color:rgba(0, 0, 0, 100);
        border-width:2px; border-style: solid;
        padding: 0px; border-top-left-radius: {self.wid_img.width()/20};
        border-top-right-radius: {self.wid_img.width()/20};
        """)
        
        self.wid_info = QWidget()
        self.wid_info.setStyleSheet(f"""
        background-color: rgba(50, 50, 110, 255);
        border-color:rgba(0, 0, 0, 100); 
        border-width:2px;
        border-style: solid;
        padding: 0px;
        border-bottom-left-radius: {self.wid_info.width()/50};
        border-bottom-right-radius: {self.wid_info.width()/50};
        """)

        self.wid_imgLayout = QVBoxLayout()
        self.wid_img.setLayout(self.wid_imgLayout)
        self.wid_imgLayout.setContentsMargins(0,0,0,0) 

        self.img = QLabel(self)

        self.wid_infoLayout = QVBoxLayout()
        self.wid_info.setLayout(self.wid_infoLayout)

        self.titleLabel = QLabel()
        self.titleLabel.setFixedHeight(30)
        self.titleLabel.setStyleSheet("""
        border-radius:10px;
        background-color: rgba(0,0,0,50);
        color: rgb(200,200,200);
        """)
        self.wid_infoLayout.addWidget(self.titleLabel)

        self.descriptionLabel = QTextEdit()
        self.descriptionLabel.setFixedHeight(70)
        self.descriptionLabel.setStyleSheet("""
        border-radius:10px;
        background-color: rgba(0,0,0,50);
        color: rgb(200,200,200);
        """)

        self.layout.addWidget(self.wid_img)
        self.layout.addWidget(self.wid_info)

    def InjectData(self, isProject, data=0):

        if isProject:
            self.wid_imgLayout.addWidget(self.img)
            self.wid_infoLayout.addWidget(self.descriptionLabel)
            self.titleLabel.setText(data["title"])
            self.descriptionLabel.setText(data["description"])

        else:
            self.titleLabel.setText("Add New Project")
            self.titleLabel.setAlignment(Qt.AlignCenter)
            self.img.setText(" ")

            plusIcon = QLabel()
            plusIcon.setStyleSheet("color: rgba(200,200,200,100);")
            plusIcon.setText("+")
            plusIcon.setFont(QFont('Arial', 100))
            plusIcon.setAlignment(Qt.AlignCenter)
            self.wid_imgLayout.addWidget(plusIcon)

    def mousePressEvent(self, event):

        if self == ProjectSelection.projectList[-1:][0]:

            with open("Resources/Data/thumbnailData.json","r") as file:
                data = json.load(file)
            
            data["stoat"] = {"title": "Stoat", "description": "Total misplay", "imageNames": ["img.png"], "rating": 5, "languageProportions": [["Python", 89.4], ["HTML", 10.6]]}

            with open("Resources/Data/thumbnailData.json","w") as file:
                json.dump(data, file)

            ProjectSelection.RestartProgram()

        else:
            self.TestWin = TestWindow()

class ProjectSelection(QMainWindow):                  
    def __init__(self, settings):
        super(ProjectSelection, self).__init__()

        time.sleep(0.1) # gives time for teminal to catch up

        self.windowInitilisationComplete = False

        uic.loadUi("Resources/Ui/projectSelection.ui", self) # Loads "" scene

        if settings["startup_isFullscreen"] == True:
            self.WindowParams_fullscreen()
        else:
            self.WindowParams_windowed()

        self.thumbnailLayout = QGridLayout()
        self.thumbnailLayout.setContentsMargins(0,0,0,0)
        self.thumbnailLayout.setSpacing(0)
        self.thumbnailLayout_container.setLayout(self.thumbnailLayout)

        self.scaleSlider.valueChanged.connect(self.scaleSliderFunc)

        self.projectCount = 0
        self.projectList = []
        self.colNum = 4

        with open("Resources/Data/thumbnailData.json", "r") as file:
            data = json.load(file)

        for chunk in data:
            self.widget = BlankThumbnailWidget(self)
            self.widget.InjectData(True, data[chunk])

            self.projectList.append(self.widget)
            self.projectCount += 1

        self.widget = BlankThumbnailWidget(self)
        self.widget.InjectData(False)

        self.projectList.append(self.widget)
        self.projectCount += 1

        self.hSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.vSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.windowInitilisationComplete = True
        self.UpdateLayout()

        self.btnCloseProgram.clicked.connect(self.CloseProgram)
        self.btnMinimise.clicked.connect(self.showMinimized)
        self.btnMaximiseToggle.clicked.connect(self.MaximisedToggle)
        
        self.show()

    def MaximisedToggle(self):

        if int(self.windowState()) == 0:
            self.WindowParams_fullscreen()
        elif int(self.windowState()) == 2:
            self.WindowParams_windowed()

    def CloseProgram(self):
        
        print(">Exit")
        QtCore.QCoreApplication.quit()
    
    def RestartProgram(self):
        
        print(">Restart")
        QtCore.QCoreApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)

    def WindowParams_windowed(self):

        print(">Window Mode")
        self.WindowParams_general()

        fixedWindowWidth = 800
        fixedWindowHeight = 642
        fixedWindowSidebarWidth = 200

        self.setFixedSize(fixedWindowWidth, fixedWindowHeight)
        self.sideBar.setFixedWidth(fixedWindowSidebarWidth)

        self.showNormal()
        self.center()

        self.thumbnailLayout_container.setMinimumSize(fixedWindowWidth-fixedWindowSidebarWidth-40, fixedWindowHeight)
        self.thumbnailLayout_container.setMaximumSize(fixedWindowWidth-fixedWindowSidebarWidth-40, fixedWindowHeight)

        self.UpdateLayout()

    def WindowParams_fullscreen(self):

        print(">Fullscreen Mode")
        self.WindowParams_general()

        sideBarWidth = 300
        fixedWindowWidth = 800

        screenSize = app.primaryScreen().size()
        self.setFixedSize(screenSize.width(), screenSize.height())
        self.sideBar.setFixedWidth(sideBarWidth)

        topLeftPoint = QDesktopWidget().availableGeometry().topLeft()
        self.move(topLeftPoint)

        self.thumbnailLayout_container.setMinimumSize(screenSize.width()-sideBarWidth-40, fixedWindowWidth)

        self.showMaximized()

        self.UpdateLayout()

    def WindowParams_general(self):

        self.setWindowTitle("Project Selection")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def UpdateLayout(self):
        
        print(">Updating")
        if self.windowInitilisationComplete == False:
            return
                
        layoutWidth = self.thumbnailLayout_container.width()

        cellWidth, cellHeight, colSize, rowSize, cols, rows, imgHeight = MatrixDimensionsSolver(self.projectCount, layoutWidth, self.colNum)
        
        spacing = colSize-cellWidth
        
        for column, widget in enumerate(self.projectList):

            widget.setFixedSize(cellWidth, cellHeight)
            widget.wid_img.setFixedHeight(imgHeight)
            widget.wid_img.setStyleSheet(f"""
            background-color: rgba(85, 85, 127, 255);
            border-color:rgba(0, 0, 0, 100);
            border-width:2px;
            border-style: solid;
            padding: 0px;
            border-top-left-radius: {widget.wid_img.width()/20};
            border-top-right-radius: {widget.wid_img.width()/20};
            """)
            widget.wid_info.setStyleSheet(f"""
            background-color: rgba(50, 50, 110, 255);
            border-color:rgba(0, 0, 0, 100);
            border-width:2px;
            border-style: solid;
            padding: 0px;
            border-bottom-left-radius: {widget.wid_info.width()/50};
            border-bottom-right-radius: {widget.wid_info.width()/50};
            """)
            
            imgdata = open('Resources/Img/img.png', 'rb').read()
            pixmap = RoundImgCorners(self, imgdata)
            pixmap = pixmap.scaled(widget.width()-4, widget.height()) # , QtCore.Qt.KeepAspectRatio
            widget.img.setPixmap(pixmap)
            print(widget.height())
            print(widget.wid_info.height())

            self.thumbnailLayout.setSpacing(spacing)

            row = math.floor(column/cols)
            
            self.thumbnailLayout.addWidget(widget, row, column+1-row*(cols))

        if self.projectCount < cols:
            self.thumbnailLayout.addItem(self.hSpacer, row, cols)
        else:
            self.thumbnailLayout.removeItem(self.hSpacer)

        self.thumbnailLayout.addItem(self.vSpacer, row+2, 1)

        self.thumbnailLayout_container.setFixedHeight((rowSize)*(rows+1))
        
    def center(self):

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def scaleSliderFunc(self):

        self.colNum = self.scaleSlider.value()
        self.scaleSlider_label.setText(f"x{self.colNum}-cols")

        self.UpdateLayout()

class TestWindow(QMainWindow):                  
    
    def __init__(self):
        super(TestWindow, self).__init__()

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        time.sleep(0.1) # gives time for teminal to catch up

        uic.loadUi("Resources/Ui/projectWindow.ui", self) # Loads "" scene

        self.setMouseTracking(True)

        val = self.hasMouseTracking()

        self.show()

#endregion Classes <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def MAIN():

    global app
    global ProjectSelection

    with open("Resources/Data/settings.json", "r") as file:
        settings = json.load(file)

    with open("Resources/Data/thumbnailData.json", "r") as file:
        data = json.load(file)

    app = QApplication(sys.argv)
    # SplashScreen = SplashScreen()
    ProjectSelection = ProjectSelection(settings)
    # TestWindow = TestWindow()

    app.exec_()

    return 1

if __name__ == "__main__": # Runs only if current file was executed (Not freferenced)

    MAIN()