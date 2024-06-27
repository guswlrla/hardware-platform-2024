import RPi.GPIO as GPIO
import time

segs = [21, 22, 23, 24, 25, 6, 12]
digits = [13, 19, 5, 17]
nums = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]
count = 0

GPIO.setmode(GPIO.BCM)
for seg in segs:
	GPIO.setup(seg, GPIO.OUT)
	GPIO.output(seg, 0) # 초기화

for digit in digits:
	GPIO.setup(digit, GPIO.OUT)
	GPIO.output(digit, 1) # 초기화

def display(data, sel): # 하나의 숫자 형태를 만드는 함수/ (데이터값, 자리수)
	for i in range(0, 7):
		GPIO.output(segs[i], nums[data] & (0x01 << i)) # 비트 이동시킴
		for j in range(0, 4): # 해당되는 위치의 fnd만 on
			if j == sel:
				GPIO.output(digits[j], 0)
			else:
				GPIO.output(digits[j], 1)

try:
	while 1:
		count += 1
		thousand = count / 1000
		hundred = count % 1000 / 100
		ten = count % 100 / 10
		one = count % 10
		fnd = [thousand, hundred, ten, one]
		for i in range(0, 4):
			display(int(fnd[i]), i) # 자리수와 값을 전달
			time.sleep(0.2)

except KeyboardInterrupt:
	GPIO.cleanup()
