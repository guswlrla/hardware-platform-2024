import RPi.GPIO as GPIO
import time

def measure():
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

trigPin = 17
echoPin = 27
piezo = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezo, GPIO.OUT)

Buzz = GPIO.PWM(piezo, 440)

try:
	while True:
		distance = measure()
		if distance > 25 and distance <= 50:
			print("Distance : %.2f cm" %distance)
			Buzz.start(100)
			Buzz.ChangeFrequency(423)
			time.sleep(1)
			Buzz.stop()
		elif distance > 10 and distance <= 25:
			print("Distacne : %.2f cm" %distance)
			Buzz.start(100)
			Buzz.ChangeFrequency(423)
			time.sleep(0.5)
			Buzz.stop()
		elif distance > 5 and distance <= 10:
			print("Distance : %.2f cm" %distance)
			Buzz.start(100)
			Buzz.ChangeFrequency(423)
			time.sleep(0.1)
			Buzz.stop()
		elif distance <= 5:
			print("Distance : %.2f cm" %distance)
			Buzz.start(100)
			Buzz.ChangeFrequency(423)
			time.sleep(0.01)
			Buzz.stop()
		else:
			Buzz.stop()
			time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
