#Ultrasonic
import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(trigPin, True) # 10us동안 HIGH레벨로 triger 출력하여 초음파 발생준비
	time.sleep(0.00001)
	GPIO.output(trigPin, False)
	start = time.time() # 현재시간 저장

	while GPIO.input(echoPin) == False: # echo가 없으면 
		start = time.time() # 현재시간을 start변수에 저장하고
	while GPIO.input(echoPin) == True: # echo가 있으면
		stop = time.time() # 현재시간을 stop변수에 저장
	elapsed = stop - start # 걸린시간
	distance = (elapsed * 19000) / 2 # 초음파속도를 이용하여 거리 계산
	
	return distance	# 거리반환

# 핀설정
trigPin = 17
echoPin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
	while True:
		distance = measure()
		print("Distance : %.2f cm" %distance)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
