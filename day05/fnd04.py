import RPi.GPIO as GPIO
import time

led = [21, 22, 23, 24, 25, 6, 12]
digit = [13, 19, 5, 17]
switch = 26
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

for ledPin in led:
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, False)

for digitPin in digit:
	GPIO.setup(digitPin, GPIO.OUT)
	GPIO.output(digitPin, False) # 꺼짐

num = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],
				[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],
				[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

try:
	while True:
		if GPIO.input(switch) == True:
			count += 1
			fnd = [0,0,0,0]
			fnd[0] = int(count / 1000)
			fnd[1] = int(count / 100)
			fnd[2] = int(count / 10)
			fnd[3] = int(count / 1)
			if count == 10:
				count = 0
			for j in range(4):
				for i in range(7):
					GPIO.output(led[i], num[count][i])
				GPIO.output(digit[j], False)
				time.sleep(0.005)
				GPIO.output(digit[j], True)
				
except KeyboardInterrupt:
	GPIO.cleanup()
