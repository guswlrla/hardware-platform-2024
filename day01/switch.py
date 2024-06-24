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
last_state = GPIO.input(switch)

try:
	while True:
		if GPIO.input(switch) == True:
			if i == 1:
				GPIO.output(r_pin, False)
				GPIO.output(g_pin, True)
				GPIO.output(b_pin, True)
				i = 2
			elif i == 2:
				GPIO.output(r_pin, True)
				GPIO.output(g_pin, False)
				GPIO.output(b_pin, True)
				i = 3
			elif i == 3:
				GPIO.output(r_pin, True)
				GPIO.output(g_pin, True)
				GPIO.output(b_pin, False)
				i = 0

except KeyboardInterrupt:
	GPIO.cleanup()
