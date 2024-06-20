# hardware-platform-2024
IoT 개발자과정 오픈 하드웨어 플랫폼활용 리포지토리

물리적인 핀번호랑 실질적인 핀번호 다름
GPIO핀에 high(5v=VCC)/low(0v=GND)값 줄수잇음
power on = 전기공급해서 전류가 흐를 수 있도록...

★옴의 법칙 V(전압)=I(전류)R(저항), 키르히호프 법칙(2kuc, 2klc)(전압법칙, 전류법칙?) 공부!!!!!!!!!!
+) 전류, 전압, 저항의 개념

전압차로 인해 전류는 높은곳에서 낮은곳으로 흐름(5v->0v)
GND의 역할 : 전류를 모이게 함(모든 전류는 GND로 흐름), GND는 기준전압이라고도 부름...

ex) 21번핀을 키려면 Low를 걸어줘야 함(5v->0v로 흐르도록 전압차)
	만약 HIGH로 한다면 전압차가 없어서 안켜짐!!!!

디지털 : 0과 1로 표현, 극성 잘못 연결하면 터짐
아날로그

파이썬
GPIO 설정함수
	GPIO.setmode(GPIO.BOARD)-wPi
	GPIO.setmode(GPIO.BCM) -BCM // 보통 이걸 많이 사용함
	GPIO.setup(channel, GPIO.mode)
	- channel : 핀번호, mode : IN/OUT
	GPIO.cleanup()
GPIO 출력함수
	GPIO.output(channel, state)
	- channel : 핀번호, state : HIGH/LOW or 1/0 or True/False
GPIO 입력함수
	GPIO.input(channel)
	- channel : 핀번호, 반환값 : H/L or 1/0 or T/F
시간지연 함수
	time.sleep(secs)

GPIO.PWM 함수도 찾아보고 적기!!
----------------------------------------------------------------------------------------------------------------------------------
플로팅- 어쩔땐 0v, 어쩔땐 5v로 읽히는 현상
풀업저항(5v에 연결되어 있는 저항) ->스위치 off일때 입력핀에 5v가 읽히고, 스위치 on일때 입력핀은 0v
풀다운저항(GND에 연결되어 있는 저항) -> 스위치 off일때 입력핀 0v, 스위치 on일때 입력핀 5v

인터럽트 = 우선순위

pwm - 펄스 폭을 제어해서 ?? 어쩌구,, 
duty = on 되는 시간
