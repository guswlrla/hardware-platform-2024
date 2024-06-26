import RPi.GPIO as GPIO
import time

led = [21, 22, 23, 24, 25, 6, 12]
digit = [13, 19, 5, 17]
switch = 26

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
			for i in range(4):
				for j in range(7):
					GPIO.output(digit[i], True)
					GPIO.output(led[j], num[][])

except KeyboardInterrupt:
	GPIO.cleanup()
