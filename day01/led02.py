import RPi.GPIO as GPIO
import time

r_pin = 21
b_pin = 20
g_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(r_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(g_pin, GPIO.OUT)

try:
	while True:
		GPIO.output(r_pin, False)
		GPIO.output(g_pin, True)
		GPIO.output(b_pin, True)
		time.sleep(1)

		GPIO.output(r_pin, True)
		GPIO.output(g_pin, False)
		GPIO.output(b_pin, True)
		time.sleep(1)

		GPIO.output(r_pin, True)
		GPIO.output(g_pin, True)
		GPIO.output(b_pin, False)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup() # 초기화
