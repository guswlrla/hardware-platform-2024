import RPi.GPIO as GPIO
import time

led = [21, 22, 23, 24, 25, 6, 12]
digit = [13, 19, 5, 17]
switch = 26
oldSw = 0
newSw = 0
index = [0,0,0,0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

for a in led:
	GPIO.setup(a, GPIO.OUT)
	GPIO.output(a, 0)

for b in digit:
	GPIO.setup(b, GPIO.OUT)
	GPIO.output(b, 1)

num = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],
				[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],
				[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

try:
	while True:
		newSw = GPIO.input(switch)

		for i in range(4):
			for j in range(7):
				GPIO.output(led[j], num[index[i]][j])
			GPIO.output(digit[i], 0)
			time.sleep(0.001)
			GPIO.output(digit[i], 1)
		if newSw == 1 and oldSw == 0:
			index[3] += 1
			if index[3] == 10:
				index[3] = 0
				index[2] += 1
			if index[2] == 10:
				index[2] = 0
				index[1] += 1
			if index[1] == 10:
				index[1] = 0
				index[0] += 1
			if index[0] == 10:
				index[0] = 0
			time.sleep(0.2)
		oldSw = newSw

except KeyboardInterrupt:
	GPIO.cleanup()
