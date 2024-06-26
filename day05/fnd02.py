import RPi.GPIO as GPIO
import time

led = [21, 22, 23, 24, 25, 6, 12]
switch = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

for ledPin in led:
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, True)

num = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],
				[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],
				[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

def display(number):
    for i in range(7):
        GPIO.output(led[i], num[number][i])

try:
	while True:
		if GPIO.input(switch) == True:
			display()

except KeyboardInterrupt:
	GPIO.cleanup()
