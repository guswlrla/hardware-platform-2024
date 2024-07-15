import RPi.GPIO as GPIO
import time

r_pin = 21
b_pin = 20
g_pin = 16
switch = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(r_pin, GPIO.OUT)
GPIO.setup(g_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

index = 0
old_state = GPIO.input(switch)

try:
	while True:
		new_state = GPIO.input(switch)
		if old_state == GPIO.HIGH and new_state == GPIO.LOW:
			if index == 0:
				GPIO.output(r_pin, False)
				GPIO.output(g_pin, True)
				GPIO.output(b_pin, True)
				index = 1
			elif index == 1:
				GPIO.output(r_pin, True)
				GPIO.output(g_pin, False)
				GPIO.output(b_pin, True)
				index = 2
			elif index == 2:
				GPIO.output(r_pin, True)
				GPIO.output(g_pin, True)
				GPIO.output(b_pin, False)
				index = 0

		old_state = new_state
		time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
