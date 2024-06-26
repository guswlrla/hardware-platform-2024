import RPi.GPIO as GPIO
import time

led = [21, 22, 23, 24, 25, 6, 12]
digit = [13, 19, 5, 17]
switch = 26
count1 = 0
count2 = 0
count3 = 0
count4 = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

for ledPin in led:
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, False)

for comPin in digit:
	GPIO.setup(comPin, GPIO.OUT)
	GPIO.output(comPin, False) # 꺼짐

num = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],
				[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],
				[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

try:
	while True:
		if GPIO.input(switch) == True:
			count1 += 1
			if count1 == 10:
				count1 = 0
				count2 += 1
			if count2 == 10:
				count2 = 0
				count3 += 1
			if count3 == 10:
				count3 = 0
				count4 += 1
			if count4 == 10:
				count4 = 0

		digit_num = [count1, count2, count3, count4]
		for i in range(4):
			for j in range(7):
				GPIO.output(led[i], num[digit_num[i]][j])
			time.sleep(0.05)
			GPIO.output(digit[i], True)
			time.sleep(0.05)
			GPIO.output(digit[i], False)

except KeyboardInterrupt:
	GPIO.cleanup()
