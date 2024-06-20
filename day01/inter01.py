import RPi.GPIO as GPIO
import time

#핀설정
r_pin = 21
g_pin = 16
b_pin = 20
switch = 6

#인터럽트 변수
intFlag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(r_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(g_pin, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

def ledBlink(channel):
	global intFlag
	if intFlag  == False:
		GPIO.output(r_pin, True)
		intFlag = True
	else:
		GPIO.output(r_pin, False)
		intFlag = False

#인터럽트 설정(switch핀에 rising 신호가 잡히면 callback함수를 실행)
GPIO.add_event_detect(switch, GPIO.RISING, callback=ledBlink)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
