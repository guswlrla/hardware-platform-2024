import RPi.GPIO as GPIO
import time

segs = [21, 22, 23, 24, 25, 6, 12]
digits = [13, 19, 5, 17]
switch = 26
nums = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

GPIO.setmode(GPIO.BCM)
for seg in segs:
	GPIO.setup(seg, GPIO.OUT)
	GPIO.output(seg, 0) # 초기화

for digit in digits:
	GPIO.setup(digit, GPIO.OUT)
	GPIO.output(digit, 1) # 초기화

def display(data): # 하나의 숫자 형태를 만드는 함수
	for i in range(0, 7):
		GPIO.output(segs[i], nums[data] & (0x01 << i)) # 비트 이동시킴

try:
	while 1:
		for i in range(0, 1):
			GPIO.output(digits[i], 0) # com1~4 선택
			for j in range(0, 10): # 0~9까지 숫자 표시
				display(j)
				time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
