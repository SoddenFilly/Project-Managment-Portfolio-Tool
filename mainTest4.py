import sys
from PyQt5.QtWidgets import ( QWidget, QApplication, QHBoxLayout, QVBoxLayout,
                              QGridLayout, QLineEdit, QLabel, QFrame)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        self.setLayout(layout)

        # self.edits = [QLineEdit(self) for _ in range(3)]
        # for edit in self.edits:
        #     edit.setStyleSheet("background-color: rgb(255, 0, 0);")
        #     layout.addWidget(edit)

        self.wid = QWidget()

        self.wid.setFixedSize(200, 200)
        
        self.wid.setStyleSheet("background-color: rgb(85, 85, 127);")
        # self.wid.setContentsMargins(0,0,0,0)
        layout.setContentsMargins(0,0,0,0) 
        layout.setSpacing(0)    
        layout.addWidget(self.wid)
        


class PyQtWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Layouttest")

        self.layout = QVBoxLayout() 
        self.layout.setContentsMargins(0,0,0,0) 
        self.layout.setSpacing(0)    
        # self.layout.setStyleSheet("background-color: rgb(255,0,0);")                      # + self.layout
        self.setLayout(self.layout)
        
        self._insert_mywidget(0) 
        self._insert_mywidget(1)    
        self._insert_mywidget(2) 
        self._insert_mywidget(3)                                 # - (layout)

        # self.labels = [QLabel("Label " + str(i+1)) for i in range(5)]
        # for i, label in enumerate(self.labels):
        #     self.layout.addWidget(label, 1, i)

        # self.edits = [QLineEdit(self) for _ in range(10)]
        # for i, edit in enumerate(self.edits):
        #     self.layout.addWidget(edit, 2, i)

    def _insert_mywidget(self, row):                                        # - , layout):
        self.widget = MyWidget(self)

        # add my widget
#        self.layout.addWidget(self.widget, 0, 0, 0, 10)   
        self.layout.addWidget(self.widget)  
        # self.layout.addWidget(self.widget, row, 0, 1, 10)  
        # self.layout.addWidget(a0, row, column, rowSpan, columnSpan)              # + 1

#        layout.addLayout(self.widget.layout(), 0, 0, 0, 10)


app = QApplication(sys.argv)

window = PyQtWindow()
window.show()

sys.exit(app.exec_())