import RPi.GPIO as GPIO
import time

led = [21, 22, 23, 24, 25, 6, 12]
switch = 26
count = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

for ledPin in led:
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, False)

num = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],
				[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],
				[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

try:
	while True:
		if GPIO.input(switch) == True:
			if count == 9:
				count = 0 
			else:
				count += 1

		for 

except KeyboardInterrupt:
	GPIO.cleanup()
