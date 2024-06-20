import RPi.GPIO as GPIO
import time

piezo = 5
melody = [130, 146, 164, 174, 195, 220, 246, 261]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezo, GPIO.OUT)

Buzz = GPIO.PWM(piezo, 440)

try:
	while True:
		Buzz.start(20)
		a = int(input("입력(1~8) : "))
		if a == 1:
			Buzz.ChangeFrequency(melody[0])
		elif a == 2:
			Buzz.ChangeFrequency(melody[1])
		elif a == 3:
			Buzz.ChangeFrequency(melody[2])
		elif a == 4:
		 Buzz.ChangeFrequency(melody[3])
		elif a == 5:
			Buzz.ChangeFrequency(melody[4])
		elif a == 6:
			Buzz.ChangeFrequency(melody[5])
		elif a == 7:
			Buzz.ChangeFrequency(melody[6])
		elif a == 8:
			Buzz.ChangeFrequency(melody[7])
		else:
			print("정확한 값 입력!")
			
except KeyboardInterrupt:
	GPIO.cleanup()
