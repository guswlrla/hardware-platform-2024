import RPi.GPIO as GPIO
import time

swPin = 13
oldSw = 0
newSw = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)

try:
	while True:
		newSw = GPIO.input(swPin)
		if newSw != oldSw:
			oldSw = newSw

			if newSw == True:
				print("click!")

			time.sleep(0.2)
			
except KeyboardInterrupt:
	GPIO.cleanup()
