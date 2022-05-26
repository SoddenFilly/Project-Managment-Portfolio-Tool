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

class Scene(QWidget): # Main scene class that can be repurposed into any menu
    
    def __init__(self):
        super(Scene, self).__init__()

        # For splash-screen type windows
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.show() # Sends GUI data to window

        # self.fileLocationPath = os.path.dirname(os.path.realpath(__file__)) # Get s files current full directory
        
        # uic.loadUi("Resources/Ui/HTML_window.ui", self) # Loads "" scene

        # self.layout = QVBoxLayout(self)

        self.setFixedSize(800, 642)

        self.topBar = QWidget(self)
        self.topBar.setMaximumHeight(42)
        self.topBar.setStyleSheet("""
        .QWidget{
        background-color: rgb(56, 56, 84);
        border-top-left-radius: 6px;
        border-top-right-radius: 6px;
        border-bottom-width:2px;
        border-color:rgb(46, 46, 74);
        border-style:solid;
        }
        """)
        self.topBarLayout = QHBoxLayout(self.topBar)
        self.topBarLayout.setSpacing(0)
        self.btnCloseProgram = QPushButton("X")
        self.btnCloseProgram.setFixedSize(40, 22)
        self.btnCloseProgram.setStyleSheet("""
        background-color: rgb(202, 82, 82);
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
        border:1px solid rgba(0,0,0,100);
        """)

        self.btnMaximiseToggle = QPushButton("[]")
        self.btnMaximiseToggle.setFixedSize(40, 22)
        self.btnMaximiseToggle.setStyleSheet("""
        background-color: rgb(85, 85, 127);
        border:1px solid rgba(0,0,0,100);
        
        """)

        self.btnMinimise = QPushButton("-")
        self.btnMinimise.setFixedSize(40, 22)
        self.btnMinimise.setStyleSheet("""
        background-color: rgb(85, 85, 127);
        border:1px solid rgba(0,0,0,100);
        border-top-left-radius: 10px;
        border-bottom-left-radius: 10px;
        """)


        self.pageContainer = QWidget(self)
        self.pageContainer.setStyleSheet("""
        background-color: rgb(85, 85, 127);
        """)

        self.pageContainerLayout = QVBoxLayout(self.pageContainer)
        self.pageContainerLayout.setContentsMargins(0,0,0,0)

        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self)
        # self.webEngineView.load(QtCore.QUrl().fromLocalFile('test.html'))
        # self.webEngineView.load(QUrl.fromLocalFile("/full/path/of/index.html"))
        self.webEngineView.load(QtCore.QUrl("C:/Users/aidan/Dev_Files/Python/Projects/Project-Management-Portfolio-Tool/boilerplate - example - test files/projectSelection.html"))
        # self.webEngineView.load(QtCore.QUrl("https://www.w3schools.com/html/html5_video.asp"))
        # self.webEngineView.load(QtCore.QUrl("https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_video "))
        # self.webEngineView.load(QtCore.QUrl("C:/Users/aidan/Dev_Files/Python/Projects/Project-Management-Portfolio-Tool/boilerplate - example - test files/videotest.html"))
  
        self.pageContainerLayout.addWidget(self.webEngineView)
        

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.topBar)
        self.layout.addWidget(self.pageContainer)

        self.topBarLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.topBarLayout.addWidget(self.btnMinimise)
        self.topBarLayout.addWidget(self.btnMaximiseToggle)
        self.topBarLayout.addWidget(self.btnCloseProgram)

        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        

        # self.centralWidget = QWidget(self)
        # self.centralWidget.addla
        
        # self.layout.addWidget(self.topBar)
        # self.btnMaximiseToggle = QPushButton("[]")
        # self.btnMinimise = QPushButton("-")

        # self.pageContainer = QWidget()

        # self.topBarLayout.addWidget(self.btnCloseProgram)
        # self.topBarLayout.addWidget(self.btnMaximiseToggle)
        # self.topBarLayout.addWidget(self.btnMinimise)



        self.btnCloseProgram.clicked.connect(self.CloseProgram)
        self.btnMinimise.clicked.connect(self.showMinimized)
        self.btnMaximiseToggle.clicked.connect(self.MaximisedToggle)
        # self.topBar.clicked.connect(self.MousePressEvent(a0))

        # self.InjectPage()

        self.show() # Sends GUI data to window

    # def MousePressEvent(self, a0):
    #     print(a0)


    def CloseProgram(self):
        
        print(">Exit")
        QtCore.QCoreApplication.quit()
    
    def MaximisedToggle(self):

        if int(self.windowState()) == 0:
            self.WindowParams_fullscreen()
        elif int(self.windowState()) == 2:
            self.WindowParams_windowed()

    def WindowParams_windowed(self):

        print(">Window Mode")
        self.WindowParams_general()

        fixedWindowWidth = 800
        fixedWindowHeight = 642
        fixedWindowSidebarWidth = 200

        self.setFixedSize(fixedWindowWidth, fixedWindowHeight)
        # self.sideBar.setFixedWidth(fixedWindowSidebarWidth)

        self.showNormal()
        self.Center()

        # self.thumbnailLayout_container.setMinimumSize(fixedWindowWidth-fixedWindowSidebarWidth-40, fixedWindowHeight)
        # self.thumbnailLayout_container.setMaximumSize(fixedWindowWidth-fixedWindowSidebarWidth-40, fixedWindowHeight)

        # self.UpdateLayout()

    def WindowParams_fullscreen(self):

        print(">Fullscreen Mode")
        self.WindowParams_general()

        sideBarWidth = 300
        fixedWindowWidth = 800

        screenSize = app.primaryScreen().size()
        self.setFixedSize(screenSize.width(), screenSize.height())
        # self.sideBar.setFixedWidth(sideBarWidth)

        topLeftPoint = QDesktopWidget().availableGeometry().topLeft()
        self.move(topLeftPoint)

        # self.thumbnailLayout_container.setMinimumSize(screenSize.width()-sideBarWidth-40, fixedWindowWidth)

        self.showMaximized()

        # self.UpdateLayout()

    def WindowParams_general(self):

        self.setWindowTitle("Project Selection")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def Center(self):

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def InjectPage(self):

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0) 
        self.layout.setSpacing(0)   
        self.pageContainer.setLayout(self.layout)

        self.page = QWidget()
        self.page.setObjectName("page")

        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.page)

        self.webEngineView.load(QtCore.QUrl("C:/Users/aidan/Dev_Files/Python/Projects/Project-Management-Portfolio-Tool/boilerplate - example - test files/diag.html"))
        self.layout.addWidget(self.webEngineView)

if __name__ == "__main__": # Runs only if current file was executed (Not freferenced)

    app = QApplication(sys.argv)
    GUIWindow = Scene()
    app.exec_()