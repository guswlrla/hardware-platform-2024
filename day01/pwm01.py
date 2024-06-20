# 피에조
import RPi.GPIO as GPIO
import time

piezo = 5
melody = [130, 146, 164, 174, 195, 220, 246, 261]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezo, GPIO.OUT)

# 아날로그 출력을 위한 객체생성(440Hz 출력)
Buzz = GPIO.PWM(piezo, 440)

try:
	while True:
		Buzz.start(20) # duty cycle : 20
		for i in range(0, len(melody)):
			Buzz.ChangeFrequency(melody[i])
			time.sleep(0.3)
		Buzz.stop()
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
