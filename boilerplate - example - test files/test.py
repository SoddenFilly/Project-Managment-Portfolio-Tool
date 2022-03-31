import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

from PIL import Image, ImageOps

class App(QWidget):

    def __init__(self):
        super(App, self).__init__()

        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 50
        self.top = 50
        self.width = 16*60
        self.height = 9*60
        self.initUI()
    
    def initUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create widget
        self.FixAspectRatio()
        label = QLabel(self)
        pixmap = QPixmap('imgFA.png').scaled(self.width, self.height)
        label.setPixmap(pixmap)
        # self.resize(pixmap.width(),pixmap.height())
        self.resize(self.width, self.height)
        # pixmap.setScaledContents(True)
        self.setStyleSheet("background-color: red;")

        
        
        self.show()

    def FixAspectRatio(self):

        old_im = Image.open('img.png')
        old_size = old_im.size

        new_size = (16*60, 9*60)
        new_im = Image.new("RGBA", new_size, (0,0,0,0))   ## luckily, this is already black!
        new_im.paste(old_im, ((new_size[0]-old_size[0])//2, (new_size[1]-old_size[1])//2))

        # new_im.show()
        new_im.save('imgFA.png')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())