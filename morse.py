from time import sleep
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)

class MyWindow(QMainWindow):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(810, 390, 300, 300)
        self.setWindowTitle("TASK 5.2C")
        self.initUI()
        
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Enter the word you want to display.")
        self.label.setGeometry(50, 100, 100,100)
        self.label.adjustSize()
        
        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.move(60, 120)
        self.textbox.resize(160, 30)
        
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.move(80, 155)
        self.pushButton.clicked.connect(self.morsecode)
        
    def morsecode(self):
        textboxValue = self.textbox.text()
        
        for x in textboxValue.upper():
            if x == "A":
                self.dot()
                self.line()
                
            if x == "B":
                self.line()
                self.dot()
                self.dot()
                self.dot()
                
            if x == "C":
                self.line()
                self.dot()
                self.line()
                self.dot()
                
            if x == "D":
                self.line()
                self.dot()
                self.dot()
                
            if x == "E":
                self.dot()
                
            if x == "F":
                self.dot()
                self.dot()
                self.line()
                self.dot()
                
            if x == "G":
                self.line()
                self.line()
                self.dot()
                
            if x == "H":
                self.dot()
                self.dot()
                self.dot()
                self.dot()
                
            if x == "I":
                self.dot()
                self.dot()
                
            if x == "J":
                self.dot()
                self.line()
                self.line()
                self.line()
                
            if x == "K":
                self.line()
                self.dot()
                self.line()
                
            if x == "L":
                self.dot()
                self.line()
                self.dot()
                self.dot()
                
            if x == "M":
                self.line()
                self.line()
                
            if x == "N":
                self.line()
                self.dot()
                
            if x == "O":
                self.line()
                self.line()
                self.line()
                
            if x == "P":
                self.dot()
                self.line()
                self.line()
                self.dot()
                
            if x == "Q":
                self.line()
                self.line()
                self.dot()
                self.line()
                
            if x == "R":
                self.dot()
                self.line()
                self.dot()
            
            if x == "S":
                self.dot()
                self.dot()
                self.dot()
                
            if x == "T":
                self.line()
                
            if x == "U":
                self.dot()
                self.dot()
                self.line()
                
            if x == "V":
                self.dot()
                self.dot()
                self.dot()
                self.line()
                
            if x == "W":
                self.dot()
                self.line()
                self.line()
                
            if x == "X":
                self.line()
                self.dot()
                self.dot()
                self.line()
                
            if x == "Y":
                self.line()
                self.dot()
                self.line()
                self.line()
                
            if x == "Z":
                self.line()
                self.line()
                self.dot()
                self.dot()
                
            sleep(1)
                
        
    def line():
        GPIO.output(10, True)             # turn the LED on
        sleep(1.5)                          # wait for 3 second to represent a line with longer blink
        GPIO.output(10, False)            # turn the LED off by making the voltage false
        sleep(0.5)
        
    def dot():
        GPIO.output(10, True)             # turn the LED on
        sleep(0.5)                          # wait for 3 second to represent a line with longer blink
        GPIO.output(10, False)            # turn the LED off by making the voltage false
        sleep(0.5)
        
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()