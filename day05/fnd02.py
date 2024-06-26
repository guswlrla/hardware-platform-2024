import RPi.GPIO as GPIO
import time

led = [21, 22, 23, 24, 25, 6, 12]
switch = 26
count = 0

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
			count += 1
			if count == 10:
				count = 0

			for i in range(0, 7):
				GPIO.output(led[i], num[count][i])
			time.sleep(0.3)

except KeyboardInterrupt:
	GPIO.cleanup()
