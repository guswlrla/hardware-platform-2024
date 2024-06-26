import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin = (21,22,23,24,25,6,12)
digits = (13,19,5,17)
switch = 26
count = 0

GPIO.setup(switch, GPIO.IN)
for a in pin:
	GPIO.setup(a, GPIO.OUT)
	GPIO.output(a, 0)

for b in digits:
	GPIO.setup(b, GPIO.OUT)
	GPIO.output(b, 1)

list = {
	'0':(1,1,1,1,1,1,0,0), # 0
	'1':(0,1,1,0,0,0,0,0), # 1
	'2':(1,1,0,1,1,0,1,0), # 2
	'3':(1,1,1,1,0,0,1,0), # 3
	'4':(0,1,1,0,0,1,1,0), # 4
	'5':(1,0,1,1,0,1,1,0), # 5
	'6':(1,0,1,1,1,1,1,0), # 6
	'7':(1,1,1,0,0,1,0,0), # 7
	'8':(1,1,1,1,1,1,1,0), # 8
	'9':(1,1,1,1,0,1,1,0) # 9
}

try:
	while True:
		if GPIO.input(switch) == True:
			count += 1
			time.sleep(0.1)
		for digit in range(4):
			fnd = [0,0,0,0]
			fnd[0] = int((count/100)/10)
			fnd[1] = int((count/100)%10)
			fnd[2] = int((count%100)/10)
			fnd[3] = int((count%100)%10)
			s = str(fnd[digit])
			for loop in range(0, 7):
				GPIO.output(pin[loop], list[s][loop])
			GPIO.output(digits[digit],0)
			time.sleep(0.005)
			GPIO.output(digits[digit],1)


except KeyboardInterrupt:
	GPIO.cleanup()
