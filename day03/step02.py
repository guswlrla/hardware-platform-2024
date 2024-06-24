import RPi.GPIO as GPIO
import time

steps = [21, 22, 23, 24]
GPIO.setmode(GPIO.BCM)

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

stepCounter = 0
stepCount = 4
seq = [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]]

try:
	while 1:
		for stepPin in range(0, 4):
			moter = steps[stepPin]
			if seq[stepCounter][stepPin] != 0:
				GPIO.output(moter, True)
			else:
				GPIO.output(moter, False)

		stepCounter += 1

		if stepCounter == stepCount:
			stepCounter = 0
		if stepCounter < 0:
			stepCounter = stepCount

		time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()
