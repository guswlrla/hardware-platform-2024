import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time
from PyQt5.QtCore import QTimer

# 핀번호 설정
r_led = 29
b_led = 20
g_led = 16

pirPin = 12

piezo = 26
melody = [130, 146, 164, 174, 195, 220, 246, 261]

trigPin = 19
echoPin = 13

digits = [18, 22, 27, 17]
segs = [5, 6, 23, 24, 25, 4, 21] # 맨마지막 핀 21로 바꾸기...
nums = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]
count = 0

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
		GPIO.output(r_led, 1)
		GPIO.output(g_led, 1)
		GPIO.output(b_led, 1)

		GPIO.setup(pirPin, GPIO.IN)

		GPIO.setup(piezo, GPIO.OUT)

		GPIO.setup(trigPin, GPIO.OUT)
		GPIO.setup(echoPin, GPIO.IN)

		for seg in segs:
			GPIO.setup(seg, GPIO.OUT)
			GPIO.output(seg, 0)

		for digit in digits:
			GPIO.setup(digit, GPIO.OUT)
			GPIO.output(digit, 1)

		# 이벤트 설정
		# led_event
		self.ledBtn1.clicked.connect(self.led_on) # LED ON
		self.ledBtn2.clicked.connect(self.led_off) # LED OFF
		self.radBtn1.clicked.connect(self.red_on) # Red Color
		self.radBtn2.clicked.connect(self.green_on) # Green Color
		self.radBtn3.clicked.connect(self.blue_on) # Blue Color

		# pir_event
		self.pirBtn1.clicked.connect(self.pir_on) # PIR ON
		self.pirBtn2.clicked.connect(self.pir_off) # PIR OFF

		# piezo_event
		self.buzzBtn1.clicked.connect(self.buzz_on) # BUZZ ON

		# ultraSonic_event
		self.sonicBtn1.clicked.connect(self.sonic_on) # UltSonic ON
		self.sonicBtn2.clicked.connect(self.sonic_off) # UltSonic OFF

		# fnd_event
		self.fndBtn1.clicked.connect(self.fnd_on) # FND ON
		self.fndBtn2.clicked.connect(self.fnd_off) # FND OFF

		# timer setting
		self.pir_timer = QTimer()
		self.pir_timer.timeout.connect(self.check_pir)

		self.sonic_timer = QTimer()
		self.sonic_timer.timeout.connect(self.sonic_on)

		self.fnd_timer = QTimer()
		self.fnd_timer.timeout.connect(self.fnd_on)

	# mesure setting
	def measure(self):
		GPIO.output(trigPin, True)
		time.sleep(0.00001)
		GPIO.output(trigPin, False)
		start = time.time()

		while GPIO.input(echoPin) == False:
			start = time.time()
		while GPIO.input(echoPin) == True:
			stop = time.time()
		elapsed = stop - start
		distance = (elapsed * 19000) / 2

		return distance

	# fnd setting
	def display(self, data, sel):
		for i in range(0, 7):
			GPIO.output(segs[i], nums[data] & (0x01 << i))
			for j in range(0, 4):
				if j == sel:
					GPIO.output(digits[j], 0)
				else:
					GPIO.output(digits[j], 1)

	# led control
	def led_on(self):
		GPIO.output(r_led, 0)
		GPIO.output(g_led, 0)
		GPIO.output(b_led, 0)
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

	# pir control
	def pir_on(self):
		self.pir_timer.start(500)

	def pir_off(self):
		self.pir_timer.stop()
		self.txtBro1.clear()

	def check_pir(self):
		if GPIO.input(pirPin) == 1:
			self.txtBro1.append("Detected!!")

	# buzz control
	def buzz_on(self):
		Buzz = GPIO.PWM(piezo, 440)
		Buzz.start(20)
		for i in range(0, len(melody)):
			Buzz.ChangeFrequency(melody[i])
			time.sleep(0.3)
		time.sleep(0.5)

	# sonic control
	def sonic_on(self):
		self.sonic_timer.start(500)
		distance = self.measure()
		self.txtBro2.append("Distance : %.2f cm" %distance)

	def sonic_off(self):
		self.sonic_timer.stop()
		self.txtBro2.clear()

	# fnd control
	def fnd_on(self):
		self.fnd_timer.start(3)
		global count
		count += 1
		if count == 10000:
			count = 0

		thousand = count // 1000
		hundred = (count % 1000) // 100
		ten = (count % 100) // 10
		one = count % 10

		fnd = [one, ten, hundred, thousand]

		self.lcdNum.display(count)

		for h in range(10):
			for i in range(3, -1, -1):
				self.display(int(fnd[i]), i)
				time.sleep(0.003)

	def fnd_off(self):
		self.fnd_timer.stop()
		for digit in digits:
			GPIO.output(digit, 1)
		for seg in segs:
			GPIO.output(seg, 0)
		global count
		count = 0

		self.lcdNum.display(count)

	def closeEvent(self, event):
		GPIO.cleanup()
		event.accept()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
