import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time
from PyQt5.QtCore import QTimer

# 핀번호 설정
r_led = 21
b_led = 20
g_led = 16

pirPin = 12

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

		GPIO.setup(pirPin, GPIO.IN)

		# 이벤트 설정
		# led_event
		self.ledBtn1.clicked.connect(self.led_on) # led on
		self.ledBtn2.clicked.connect(self.led_off) # led off
		self.radBtn1.clicked.connect(self.red_on) # Red Color
		self.radBtn2.clicked.connect(self.green_on) # Green Color
		self.radBtn3.clicked.connect(self.blue_on) # Blue Color

		# pir_event
		self.pirBtn1.clicked.connect(self.pir_on) # pir_on
		self.pirBtn2.clicked.connect(self.pir_off) # pir_off

	def led_on(self):
		GPIO.output(r_led, 0)
		GPIO.output(g_led, 1)
		GPIO.output(b_led, 1)
	def led_off(self):
		GPIO.output(r_led, 1)
		GPIO.output(g_led, 1)
		GPIO.output(b_led, 1)
	def red_on(self):
		GPIO.output(r_led, 0)
		GPIO.output(g_led, 1)
		GPIO.output(b_led, 1)
	def green_on(self):
		GPIO.output(r_led, 1)
		GPIO.output(g_led, 0)
		GPIO.output(b_led, 1)
	def blue_on(self):
		GPIO.output(r_led, 1)
		GPIO.output(g_led, 1)
		GPIO.output(b_led, 0)

	def pir_on(self):
		if GPIO.input(pirPin) == 1:
			print("Detected!!")
			time.sleep(0.5)
	def pir_off(self):
		GPIO.input(pirPin, 0)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
