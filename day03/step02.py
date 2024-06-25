import RPi.GPIO as GPIO
import time

steps = [21, 22, 23, 24]
GPIO.setmode(GPIO.BCM)

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

step_seq = [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]]

try:
	while 1:
		for seq in step_seq:
			for pin in range(4):
				GPIO.output(steps[pin], seq[pin])
			time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()
