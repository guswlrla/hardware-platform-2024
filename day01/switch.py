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

try:
	while True:
		for(i = 0; i < 3; i++):
			if GPIO.input(switch) == 1 and i == 0:
				GPIO.output(r_pin, False)
				GPIO.output(g_pin, True)
				GPIO.output(b_pin, True)
				i += 1
			if GPIO.input(switch) == 1 and i == 1:
				GPIO.output(r_pin, True)
				GPIO.output(g_pin, False)
				GPIO.output(b_pin, True)
				i += 1
			if GPIO.input(switch) == 1 and i == 2:
				GPIO.output(r_pin, True)
				GPIO.output(g_pin, True)
				GPIO.output(b_pin, False)
				i += 1

except KeyboardInterrupt:
	GPIO.cleanup()
