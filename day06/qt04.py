import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

# 핀번호 설정
r_led = 21
b_led = 20
g_led = 16

form_class = uic.loadUiType("./sensor.ui")[0]

# windowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		# GPIO 설정
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(r_led, GPIO.OUT)
		GPIO.setup(b_led, GPIO.OUT)
		GPIO.setup(g_led, GPIO.OUT)

		# 이벤트 설정
		# led_event
		self.ledBtn1.clicked.connect(self.led_on) # led on
		self.ledBtn2.clicked.connect(self.led_off) # led off
		self.radBtn1.clicked.connect(self.red_on) # Red LED

	def led_on(self):
		GPIO.output(r_led, False)
		GPIO.output(g_led, True)
		GPIO.output(b_led, True)
		#print("led on!!")
	def led_off(self):
		GPIO.output(r_led, True)
		GPIO.output(g_led, True)
		GPIO.output(b_led, True)
		#print("led off!!")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
