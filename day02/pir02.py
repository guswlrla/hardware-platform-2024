import RPi.GPIO as GPIO
import time

led = 21
pirPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # 풀업풀다운 역할

try:
	while True:
		if GPIO.input(pirPin) == True:
			GPIO.output(led, False)
			print("인체감지!!")
			time.sleep(0.5)
		else:
			GPIO.output(led, True)
			time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
