import RPi.GPIO as GPIO

led = 21

#GPIO를 BCM 모드로 설정
GPIO.setmode(GPIO.BCM)

#GPIO핀 설정(입력/출력)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		GPIO.output(led, False) # 전압차가 생기도록 False

except KeyboardInterrupt: #Ctrl + c
	GPIO.cleanup()
