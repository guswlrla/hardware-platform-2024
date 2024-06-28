import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

led = 21

form_class = uic.loadUiType("./sensor.ui")[0]

# windowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(led, GPIO.OUT)

		self.ledBtn1.clicked.connect(self.ledBtn1Func)
		self.ledBtn2.clicked.connect(self.ledBtn2Func)

	def ledBtn1Func(self):
		GPIO.output(led, False)
		#print("led on!!")
	def ledBtn2Func(self):
		#print("led off!!")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
