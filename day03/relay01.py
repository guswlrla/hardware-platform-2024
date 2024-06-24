import RPi.GPIO as GPIO
import time

relayPin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
	GPIO.output(relayPin, 1)

except KeyboardInterrupt:
	GPIO.cleanup()
