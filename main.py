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
        
        uic.loadUi("Resources/Ui/splashScreen.ui", self) # Loads "" scene

class SetupScene(QMainWindow):                  
    
    def __init__(self):
        super(SetupScene, self).__init__()

        self.show()
        uic.loadUi("Resources/Ui/loadPack.ui", self) # Loads "" scene
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

    paddingPercentage = 5 # 10%
    
    colSize = int(layoutWidth/cols)

    cellWidth = colSize/(100+paddingPercentage)*100
    cellWidth = int(cellWidth-(colSize-cellWidth)/cols*2)
    rowSize = int((colSize/16*9)+(colSize/16*9)/2)
    cellHeight = int((cellWidth/16*9)+(cellWidth/16*9)/2)
    imgHeight = int(cellWidth/16*9)

    rows = int(math.ceil(totalCells/cols))
    # print(cellWidth, paddedcellWidth, maxCellsWidth, fittingPaddedCellsWidth, newcellWidth, newCellHeight)

    # print(cellWidth, cellHeight, colSize, rowSize, cols, rows)
    
    return cellWidth, cellHeight, colSize, rowSize, cols, rows, imgHeight

class BlankWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.wid = QWidget()
        self.wid.setStyleSheet("background-color: rgba(85, 85, 127, 255); border-color:rgba(0, 0, 0, 100); border-width:2px; border-style: solid; padding: 20px;")
        
        # self.widLayout = QVBoxLayout()
        # self.temp = QPushButton("tex")
        # self.temp.setStyleSheet("background-color: rgba(85, 255, 127, 255);")
        # self.widLayout.addWidget(self.temp)
        
        # self.wid.setLayout(self.widLayout)
        

        self.layout.setContentsMargins(0,0,0,0) 
        self.layout.setSpacing(0)    
        self.layout.addWidget(self.wid)

def RoundImgCorners(imgdata, imgtype ='png', size = 64):
  
    # Load image
    image = QImage.fromData(imgdata, imgtype)
  
    image.convertToFormat(QImage.Format_ARGB32)

    out_img = QImage(image.width()*4, image.height()*4, QImage.Format_ARGB32)
    out_img.fill(Qt.transparent)

    brush = QBrush(image)

    painter = QPainter(out_img)
    painter.setBrush(brush)

    painter.setPen(Qt.NoPen)

    # painter.drawEllipse(0, 0, image.width()*4, image.height()*4)
    path = QPainterPath()
    path.moveTo(0, image.height())

    # path.cubicTo(0, image.height(), image.height()/10, image.height()/10, image.height(), 0)
    # path.drawLine(image.height(), 0, image.width()*4-image.height(), 0)
    painter.drawRoundedRect(0, 0, out_img.width(), out_img.height(), out_img.width()/4, out_img.width()/4)
    
    painter.drawPath(path)

  
    painter.end()
  
    pm = QPixmap.fromImage(out_img)
  
    # return back the pixmap data
    return pm

class BlankThumbnailWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


        self.wid_img = QWidget()
        self.dynamicStyleSheet = f"background-color: rgba(85, 85, 127, 255); border-color:rgba(0, 0, 0, 100); border-width:2px; border-style: solid; padding: 0px; border-top-left-radius: {self.wid_img.width()/20}; border-top-right-radius: {self.wid_img.width()/20};"

        self.wid_img.setStyleSheet(self.dynamicStyleSheet)
        
        self.wid_info = QWidget()
        self.wid_info.setStyleSheet(f"background-color: rgba(50, 50, 110, 255); border-color:rgba(0, 0, 0, 100); border-width:2px; border-style: solid; padding: 0px; border-bottom-left-radius: {self.wid_info.width()/50}; border-bottom-right-radius: {self.wid_info.width()/50};")
        

        


        self.wid_imgLayout = QVBoxLayout()
        self.wid_img.setLayout(self.wid_imgLayout)
        self.wid_imgLayout.setContentsMargins(0,0,0,0) 
        # self.wid_imgLayout.setSpacing(0)

        self.img = QLabel(self)

        imgdata = open('Resources/Img/img.png', 'rb').read()
        pixmap = RoundImgCorners(imgdata).scaled(self.wid_img.width(), self.wid_img.height())

        self.img.setPixmap(pixmap)

        # self.img.setStyleSheet(f"border-top-left-radius: {self.wid_img.width()/20}; border-top-right-radius: {self.wid_img.width()/20};")

        # self.wid_imgLayout.addWidget(self.img)



        self.wid_infoLayout = QVBoxLayout()
        self.wid_info.setLayout(self.wid_infoLayout)
        # self.wid_infoLayout.setContentsMargins(0,0,0,0) 
        # self.wid_imgLayout.setSpacing(0)

        self.titleLabel = QLabel()
        # self.titleLabel = QLabel(self).setText("text")
        self.titleLabel.setFixedHeight(30)

        self.titleLabel.setStyleSheet("border-radius:10px; background-color: rgba(0,0,0,50); color: rgb(200,200,200);")

        
        
        # self.img.setStyleSheet(f"border-top-left-radius: {self.wid_img.width()/20}; border-top-right-radius: {self.wid_img.width()/20};")

        self.wid_infoLayout.addWidget(self.titleLabel)


        self.descriptionLabel = QTextEdit()
        # self.titleLabel = QLabel(self).setText("text")
        # self.descriptionLabel.setText("tetkfcekd")
        self.descriptionLabel.setFixedHeight(70)

        self.descriptionLabel.setStyleSheet("border-radius:10px; background-color: rgba(0,0,0,50); color: rgb(200,200,200);")

        



        self.layout.setContentsMargins(0,0,0,0) 
        self.layout.setSpacing(0)    
        self.layout.addWidget(self.wid_img)
        self.layout.addWidget(self.wid_info)

    def InjectData(self, data, isProject):
        # print(data["title"])
        if isProject:
            self.wid_imgLayout.addWidget(self.img)
            self.wid_infoLayout.addWidget(self.descriptionLabel)
            self.titleLabel.setText(data["title"])
            self.descriptionLabel.setText(data["description"])
            # self.wid_imgLayout.addWidget(self.titleLabel)
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

        print("clicked", self, event)
        # print(ProjectSelection.projectList[-1:])

        # ProjectSelection = ProjectSelection(settings)
        if self == ProjectSelection.projectList[-1:][0]:
            print("ADD")
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

        self.windowInitilisationComplete = False

        time.sleep(0.1) # gives time for teminal to catch up

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
            # print(data)
            # print()

        for i in data:
            
            self.widget = BlankThumbnailWidget(self)
            self.widget.InjectData(data[i], True)

            self.projectList.append(self.widget)
            self.projectCount += 1

        self.widget = BlankThumbnailWidget(self)
        self.widget.InjectData(data[i], False)

        self.projectList.append(self.widget)
        self.projectCount += 1


        
        # for i in range(7):
        #     self.widget = BlankThumbnailWidget(self)
        #     self.projectList.append(self.widget)
        #     print(self.projectList)

        #     self.projectCount += 1

        self.hSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.vSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.windowInitilisationComplete = True
        self.UpdateLayout()

        self.btnCloseProgram.clicked.connect(self.CloseProgram)
        self.btnMinimise.clicked.connect(self.showMinimized)
        self.btnMaximiseToggle.clicked.connect(self.MaximisedToggle)
        
        self.show()

    def myfunction(self):
        print("\nSUCCESS\n")

    def MaximisedToggle(self):

        if int(self.windowState()) == 0:
            self.WindowParams_fullscreen()
        elif int(self.windowState()) == 2:
            # time.sleep(1)
            self.WindowParams_windowed()

    def CloseProgram(self):
        
        print(">Exit")
        Animate.opacity(self, self.btnCloseProgram)
        QtCore.QCoreApplication.quit()
    
    def RestartProgram(self):
        
        print(">Restart")
        QtCore.QCoreApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)

    def WindowParams_windowed(self):

        print(">Window Mode")

        self.WindowParams_general()
        # time.sleep(1)

        fixedWindowWidth = 800
        fixedWindowHeight = 642
        fixedWindowSidebarWidth = 200
        self.setFixedSize(fixedWindowWidth, fixedWindowHeight)
        self.sideBar.setFixedWidth(fixedWindowSidebarWidth)
        # time.sleep(1)
        self.showNormal()
        self.center()

        # time.sleep(1)
        self.thumbnailLayout_container.setMinimumSize(fixedWindowWidth-fixedWindowSidebarWidth-40, fixedWindowHeight)
        self.thumbnailLayout_container.setMaximumSize(fixedWindowWidth-fixedWindowSidebarWidth-40, fixedWindowHeight)

        # time.sleep(1)
        self.UpdateLayout()

    def WindowParams_fullscreen(self):

        print(">Fullscreen Mode")

        self.WindowParams_general()

        screenSize = app.primaryScreen().size()
        self.setFixedSize(screenSize.width(), screenSize.height())
        sideBarWidth = 300
        self.sideBar.setFixedWidth(sideBarWidth)
        # time.sleep(0.1)

        topLeftPoint = QDesktopWidget().availableGeometry().topLeft()
        self.move(topLeftPoint)

        self.thumbnailLayout_container.setMinimumSize(screenSize.width()-sideBarWidth-40, 800)
        # time.sleep(1)
        self.showMaximized()

        self.UpdateLayout()

    def WindowParams_general(self):

        pass
        self.setWindowTitle("Project Selection")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def UpdateLayout(self):
        
        print(">Updating")

        if self.windowInitilisationComplete == False:
            return
                
        layoutWidth = self.thumbnailLayout_container.width()
        # print(layoutWidth)

        # print()
        # print(self.projectCount, layoutWidth, self.colNum)
        cellWidth, cellHeight, colSize, rowSize, cols, rows, imgHeight = MatrixDimensionsSolver(self.projectCount, layoutWidth, self.colNum)
        # print(cellWidth, cellHeight, colSize, rowSize, cols, rows)
        
        spacing = colSize-cellWidth
        # vSpacer = QSpacerItem(spacing, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)
        
        # self.thumbnailLayout.addItem(vSpacer, 0, 0)
        
        for column, widget in enumerate(self.projectList):
            widget.setFixedSize(cellWidth, cellHeight)
            widget.wid_img.setFixedHeight(imgHeight)
            widget.wid_img.setStyleSheet(f"background-color: rgba(85, 85, 127, 255); border-color:rgba(0, 0, 0, 100); border-width:2px; border-style: solid; padding: 0px; border-top-left-radius: {widget.wid_img.width()/20}; border-top-right-radius: {widget.wid_img.width()/20};")
            # widget.wid_img.setStyleSheet(widget.dynamicStyleSheet)
            widget.wid_info.setStyleSheet(f"background-color: rgba(50, 50, 110, 255); border-color:rgba(0, 0, 0, 100); border-width:2px; border-style: solid; padding: 0px; border-bottom-left-radius: {widget.wid_info.width()/50}; border-bottom-right-radius: {widget.wid_info.width()/50};")
        

            
            # widget.layout.wid.setStyleSheet("background-color: blue; padding: 15px;")
            
            self.thumbnailLayout.setSpacing(spacing)
            # widget.layout.setContentsMargins((layoutWidth-colSize*cols)/2, 0,0,0) \

            row = math.floor(column/cols)
            
            # print(column, cols, row)
            

            self.thumbnailLayout.addWidget(widget, row, column+1-row*(cols))
            
            # self.widget.mouseReleaseEvent = lambda a: print("dd")
            # ss = "ss"
            # exec(f'self.widget.mouseReleaseEvent = lambda e{self.projectCount}: print("{self.projectCount}")')
        
        # hSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # vSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        if self.projectCount < cols:
            self.thumbnailLayout.addItem(self.hSpacer, row, cols)
        else:
            self.thumbnailLayout.removeItem(self.hSpacer)

        # print(row)
        self.thumbnailLayout.addItem(self.vSpacer, row+2, 1)
        # self.thumbnailLayout.addWidget(widget, row+6, 2)

        self.thumbnailLayout_container.setFixedHeight((rowSize)*(rows+1))


        # print(self.thumbnailLayout.children())
        # print(self.projectList)
        # for i in self.projectList:
        #     self.thumbnailLayout.removeWidget(i)
        
 

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

        # uic.loadUi("Resources/Ui/projectWindow.ui", self) # Loads "" scene
        uic.loadUi("Resources/Ui/projectWindow.ui", self) # Loads "" scene

        self.setMouseTracking(True)

        val = self.hasMouseTracking()

        # print(val)

        # widget = BlankThumbnailWidget(self)
        # # self.projectList.append(self.widget)

        # widget.setFixedSize(160*4, 90*4+90*2)
        # widget.wid_img.setFixedHeight(90*4)

        # # self.layoutWid.rem

        # self.layout = QGridLayout()
        # self.layoutWid.setLayout(self.layout)

        # # widget.layout.wid.setStyleSheet("background-color: blue; padding: 15px;")
        
        # # self.layoutWid.layout.setSpacing(10)
        # # widget.layout.setContentsMargins((layoutWidth-colSize*cols)/2, 0,0,0) \
        
        # # print(column, cols, row)

        # self.layout.addWidget(widget, 1, 1)


        # self.WindowParams_general()
        self.show()

        def WindowParams_general(self):

            self.setWindowTitle("--")
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        def mouseMoveEvent(self, event):
            pass

            # print("eventX", event.x())


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

def MAIN():

    global app
    global ProjectSelection

    with open("Resources/Data/settings.json", "r") as file:
        settings = json.load(file)

    with open("Resources/Data/thumbnailData.json", "r") as file:
        data = json.load(file)
        # print(data)
        # print()
        # for i in data:
        #     print(data[i])
    
    # with open("Resources/Data/thumbnailData.json", "w") as file:
    #     # print(json.load(file))
    #     json.dump(dic, file)

    app = QApplication(sys.argv)
    # SplashScreen = SplashScreen()
    # SetupScene = SetupScene()
    ProjectSelection = ProjectSelection(settings)
    # Test = TestWindow()

    app.exec_()

    return 1


if __name__ == "__main__": # Runs only if current file was executed (Not freferenced)

    # with open("Resources/Data/settings.json", "r") as file:
    #     settings = json.load(file)

    # with open("Resources/Data/thumbnailData.json", "r") as file:
    #     data = json.load(file)
    #     # print(data)
    #     # print()
    #     # for i in data:
    #     #     print(data[i])
    
    # # with open("Resources/Data/thumbnailData.json", "w") as file:
    # #     # print(json.load(file))
    # #     json.dump(dic, file)

    # app = QApplication(sys.argv)
    # # SplashScreen = SplashScreen()
    # # SetupScene = SetupScene()
    # ProjectSelection = ProjectSelection(settings)
    # # Test = TestWindow()

    # app.exec_()

    MAIN()