# from PyQt5.QtGui import QPainter, QPen,QBrush,QColor
from PyQt5.QtGui import QPainter, QPen,QBrush,QColor, QFont
# from PyQt5.QtCore import Qt
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QGroupBox
import sys

class BatteryStatusWidget(QWidget):
    def __init__(self):
        super(BatteryStatusWidget, self).__init__()
        #Voltage widgets
        self.voltage_text = QLineEdit()
        self.voltage_text.setReadOnly(True)
        self.voltage_label = QLabel("V")
        self.voltage_label.setStyleSheet("QLabel {color : white}")

        #Status widgets
        self.status_text = QLineEdit()
        self.status_text.setReadOnly(True)
        self.status_label = QLabel("STATUS")
        self.status_label_font = QFont()
        self.status_label_font.setPointSize(12)
        self.status_label.setFont(self.status_label_font)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("QLabel {color : white}")

        #Serial number
        self.serial_number_text = QLineEdit()
        self.serial_number_label = QLabel("S/N")

        #LED widgets
        self.yellow_led_label = QLabel()
        self.yellow_led_label.setStyleSheet("QLabel {background-color : yellow; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.green_led_label = QLabel()
        self.green_led_label.setStyleSheet("QLabel {background-color : green; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.red_led_label = QLabel()
        self.red_led_label.setStyleSheet("QLabel {background-color : red; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")

        #Number Identifier Label
        #This label is for tagging the widget with the same label as on the PCB
        self.number_label = QLabel("Test")
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label_font = QFont()
        self.number_label_font.setPointSize(12)
        self.number_label_font.setBold(True)
        self.number_label.setFont(self.number_label_font)

        #Layouts
        #voltage layout
        self.voltage_layout = QHBoxLayout()
        self.voltage_layout.addWidget(self.voltage_text)
        self.voltage_layout.addWidget(self.voltage_label)

        #Serial number layout
        self.serial_num_layout = QHBoxLayout()
        self.serial_num_layout.addWidget(self.serial_number_label)
        self.serial_num_layout.addWidget(self.serial_number_text)

        #Voltage and status box layouts
        self.blue_container = QWidget()
        self.blue_container.setStyleSheet("background-color:rgb(77, 122, 194);")
        self.blue_box_layout = QVBoxLayout()
        self.blue_box_layout.addLayout(self.voltage_layout)
        self.blue_box_layout.addWidget(self.status_text)
        self.blue_box_layout.addWidget(self.status_label)
        self.blue_container.setLayout(self.blue_box_layout)


        #Blue box+ serial num layout
        self.non_led_layout = QVBoxLayout()
        #self.non_led_layout.addWidget(self.number_label)
        self.non_led_layout.addWidget(self.blue_container)
        self.non_led_layout.addLayout(self.serial_num_layout)

        #LED layout
        self.led_layout = QVBoxLayout()
        self.led_layout.addWidget(self.yellow_led_label)
        self.led_layout.addWidget(self.green_led_label)
        self.led_layout.addWidget(self.red_led_label)
        self.led_layout.addStretch(1)

        #Main Layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.non_led_layout)
        self.main_layout.addLayout(self.led_layout)

        #Main group box
        self.main_group_box = QGroupBox()
        self.main_group_box.setStyleSheet("QGroupBox{font-size: 10px}")
        self.main_group_box.setTitle("Chan 0")
        self.main_group_box.setLayout(self.main_layout)


        #LED widgets 1
        self.yellow_led_label1 = QLabel()
        self.yellow_led_label1.setStyleSheet("QLabel {background-color : yellow; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.green_led_label1 = QLabel()
        self.green_led_label1.setStyleSheet("QLabel {background-color : green; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.red_led_label1 = QLabel()
        self.red_led_label1.setStyleSheet("QLabel {background-color : red; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")


        #LED layout 1
        self.led_layout1 = QVBoxLayout()
        self.led_layout1.addWidget(self.yellow_led_label1)
        self.led_layout1.addWidget(self.green_led_label1)
        self.led_layout1.addWidget(self.red_led_label1)
        self.led_layout1.addStretch(1)

        #Main Layout 1
        self.main_layout1 = QHBoxLayout()
        # self.main_layout1.addLayout(self.non_led_layout)
        self.main_layout1.addLayout(self.led_layout1)

        #Main group box 1
        self.main_group_box1 = QGroupBox()
        self.main_group_box1.setStyleSheet("QGroupBox{font-size: 10px}")
        self.main_group_box1.setTitle("Chan 1")
        self.main_group_box1.setLayout(self.main_layout1)



        #Outer main layout to accomodate the group box
        self.outer_main_layout = QVBoxLayout()
        self.outer_main_layout.addWidget(self.main_group_box1)



        self.outer_main_layout.addWidget(self.main_group_box)




        #Set the main layout
        self.setLayout(self.outer_main_layout)
        self.setWindowTitle("Battery Widget")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = BatteryStatusWidget()
    main_window.show()
    app.exec_()