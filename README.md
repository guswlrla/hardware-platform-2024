# hardware-platform-2024
:fire:IoT 개발자과정 오픈 하드웨어 플랫폼활용 리포지토리:rocket:

## :white_check_mark:1일차
### 1. 라즈베리파이 기초
- 물리적인 핀번호(핀배열번호)와 실질적인 핀번호는 다르기 때문에 주의!	

	![rpi핀맵](https://raw.githubusercontent.com/guswlrla/hardware-platform-2024/main/images/gpio.png)

- 각 GPIO핀에는 레지스터가 있는데 해당 레지스터에 HIGH/LOW 값을 줄 수 있음
	- HIGH(5v=VCC), LOW(0v=GND)
- 옴의 법칙 V(전압) = I(전류)·R(저항)
	- 전압 : 회로의 두 지점 사이의 전위차(전기적 위치에너지의 차)
	- 전류 : 전하의 흐름
	- 저항 : 전류가 흐르는 것을 방해하는 정도
- 키르히호프 법칙
	- 전류법칙 : 전기가 통과하는 분기점(선의 연결지점, 만나는 지점)에서 들어온 전류의 양과 나간 전류의 양의 합은 같다.
	- 전압법칙 : 회로 속 닫힌 경로에서, 기전력(전력을 발생시키는 곳에서 나온 전력)의 합과 저항에 의한 전압 강하의 합과 같다.(=폐회로에서는 전원에서 만들어낸 기전력이 회로에서 모두 쓰인다.)
- 전압차로 인해 **전류는 높은 곳(5v)에서 낮은 곳(0v)에서 흐름**
	- GND(기준전압)의 역할 : 전류를 모이게 함(모든 전류는 GND로 흐름)
	- 예를 들어, 21번 핀을 키려면 LOW을 걸어줘야 함(5v -> 0v로 흐르도록 전압차를 줌) HIGH를 준다면 전압차가 없어서 안켜짐!

### 2. GPIO모듈 기본함수
- GPIO 설정함수
	- GPIO.setmode(GPIO.BOARD) : 보드의 핀번호를 사용할 때
	- GPIO.setmode(GPIO.BCM) : GPIO핀을 사용할 때
	- GPIO.setup(channel, GPIO.mode) : 핀 입출력 설정
		- channel : 핀번호, mode : IN/OUT
	- GPIO.cleanup() : GPIO 모듈 점유 해제
- GPIO 출력함수
	- GPIO.output(channel, state) : 출력핀에 대한 상태 지정
		- channel : 핀번호, state : HIGH/LOW or 1/0 or True/False
- GPIO 입력함수
	- GPIO.input(channel) : 입력핀으로 설정한 핀에 입력되는 값 읽음(디지털 값만)
		- channel : 핀번호, 반환값 : H/L or 1/0 or T/F
- 시간지연 함수
	- time.sleep(secs)

### 3. 풀업(Pull-Up)저항과 풀다운(Pull-Down)저항 with.스위치
- 플로팅 상태를 방지하기 위해 풀업 저항과 풀다운 저항 사용
	- 플로팅(Floating) : LOW인지 HIGH인지 알 수 없는 상태, 0과 1이 번갈아 나타나는 불안정한 상태
- 풀업저항
	- **저항을 VCC(전원) 쪽에 걸어** 입력을 받지 않은 상태일 때 HIGH로 끌어올리고, 입력을 받았을 때는 LOW로 끌어내리는 회로

		![풀업](https://raw.githubusercontent.com/guswlrla/hardware-platform-2024/main/images/pull-up.png)

- 풀다운저항
	- **저항을 GND(접지) 쪽에 걸어** 입력을 받지 않은 상태일 때 LOW로 끌어내리고, 입력을 받았을 때는 HIGH으로 끌어올리는 회로

		![풀다운](https://raw.githubusercontent.com/guswlrla/hardware-platform-2024/main/images/pull-down.png)

### 4. GPIO 인터럽트(Interrupt) 사용
- 인터럽트 : 우선순위, 기존에 CPU에서 처리하던 프로그램을 중단하고 인터럽트를 요청한 프로그램으로 실행 제어권을 넘기는 것
- wait_for_edge(핀번호, GPIO.상태)
	- 상태 : RISING/FALLING/BOTH
- event_detected(핀번호)
- add_event_detect(핀번호, 상태, callback=함수명, bouncetime=숫자)

### 5. GPIO PWM 제어 with.피에조부저
- PWM(Pulse Width Modulation) : 펄스 폭을 제어해서 디지털 신호를 아날로그 신호처럼 동작하도록 하는 기능
- Duty : 한 주기 안에서 신호가 on 되어있는 비율
- Duty Cycle : 주기에 대한 on/off 시간의 비
	- 예를들어, Duty Cycle이 50%이면 2.5v의 효과를 낼 수 있음
- PWM 객체 생성
	- 객체 = GPIO.PWM(핀번호, 주파수)
		- 주파수 : Hz단위의 주파수로 0보다 큰 값 입력
- PWM 시작
	- 객체.start(duty비)
		- duty비 : Duty Cycle %단위로서의 0~100 사이 숫자 입력
- 객체.ChangeFreqeuncy(주파수)
- [-]인터럽트랑 스위치 파일 수정!

## :white_check_mark:2일차
### 1. 파이썬 가상환경 설정
- python -m venv [가상환경이름]
- source ./[가상환경이름]/bin/activate : 가상환경접속
- deactivate : 가상환경 빠져나오기

### 2. 라즈베리파이 GPIO 확인
- sudo git clone https://github.com/WiringPi/WiringPi
- cd WiringPi
- sudo ./build
- gpio readall
- 채널이 사용중이라고 뜰 때, GPIO 핀을 확인해서 해당되는 핀을 1로 설정!

### 3. 초음파센서 실습
- 초음파센서 원리
	- 송신부(Trig)에서 일정한 시간의 간격을 둔 짧은 초음파 펄스를 방사하고 대상에 부딪혀 돌아온 신호를 수신부(Echo)에서 받아, 이에 대한 시간차를 기반으로 거리 산출
	- 초음파와 장애물간의 왕복 시간이므로 2를 나눠줘야 함
		- 거리 = (시간 × 소리의 속도) / 2

## :white_check_mark:3일차
### 1. 릴레이모듈 실습
- 낮은 전압/전류를 이용해 더 높은 전압/전류를 제어하는 상황에 쓰임
- 릴레이모듈 원리
	- 전자석의 원리로 전류가 흐르면 자기장을 형성해 자기력으로 자석을 끌어당겼다가 전류가 흐르지 않으면 자석을 놓는 원리
		- COM(common) : 공통단자로 항상 연결
		- NC(닫힌접점, normal close) : 평상시에 스위치가 닫혀있음, 릴레이에 전류가 흐르면 열림
		- NO(열린접점, normal open) : 평상시에 스위치가 열려있음, 릴레이에 전류가 흐를 때 닫힘

		![릴레이](https://raw.githubusercontent.com/guswlrla/hardware-platform-2024/main/images/relay2.png) 

### 2. 스텝모터 실습
- 모터의 회전을 잘게 쪼개서 쪼갠 조각(스텝)을 이용해 제어하는 모터
- 스텝모터 원리
	- 전자석의 기능을 이용하여 로터(모터 회전축)를 돌리는 구조

		![스텝모터](https://raw.githubusercontent.com/guswlrla/hardware-platform-2024/main/images/moter.png) 

### 3. flask 웹서버 실행
- 기본적인 라이브러리 포함 가상환경
	- python -m venv --system-site-packages [가상환경이름]
- flask 기본코드
	- port : 포트번호 수정
	- debug=True : 코드 수정마다 flask 변경된 걸 인식하고 다시 시작

	```
	from flask import Flask
	app = Flask(__name__)

	@app.route("/")
	def hello():
		return "Kim Hyeon Ji!"

	if __name__ == "__main__":
		app.run(host = "0.0.0.0", port = "10011", debug = True)
	```
- 정적라우팅

	```
	@app.route("/name")
	def name():
		return "<h1>My name is Kim Hyeon Ji!!</h1>"

	@app.route("/age")
	def age():
		return "<h1> 24 years old</h1>"
	```
- get방식 파라미터 전달
	- ?key=value&key=value 값으로 전달

## :white_check_mark:4일차
### 1. FND(Flexible Numeric Display) 실습
- 7개의 led를 이용하여 숫자나 문자를 표시하는 부품, 세븐세그먼트(7-Segment)라고도 부름
	- COM1 ~ COM4 : FND를 선택하는 단자
	- a~g핀, dp핀 : 각 7개의 led를 의미
- 공통 캐소드형(Common Cathod)
	- 각 led의 캐소드(-) 단자들이 공통으로 묶여있으므로 COM은 **gnd**에 연결
	- 데이터 신호인 a~g, dp에 output값 1을 주면 불이 켜짐

	![cathod](https://raw.githubusercontent.com/guswlrla/hardware-platform-2024/main/images/cathod.png)

- 공통 애노드형(Common Anode)
	- 각 led의 애노드(+) 단자들이 공통으로 묶여있으므로 COM은 **vcc**에 연결
	- 데이터 신호인 a~g, dp에 output값 0을 주면 불이 켜짐

	![anode](https://raw.githubusercontent.com/guswlrla/hardware-platform-2024/main/images/anode.png)

- 외형으로 타입을 구분할 수 없으므로 데이터시트로 확인
- 캐소드타입인지 애노드타입인지에 따라 16진수도 달라지고 회로도 달라짐

## :white_check_mark:5일차
### 1. FND 실습
- 불을 계속 키는게 아닌, 짧은 시간에 껐다 켰다 반복해서 화면에 띄우는 원리
- 각 자릿수가 10이 되면 다음 자릿수를 1씩 증가시키는 알고리즘

	```
	if newSw == 1 and oldSw == 0:
			index[3] += 1
			if index[3] == 10:
				index[3] = 0
				index[2] += 1
			if index[2] == 10:
				index[2] = 0
				index[1] += 1
			if index[1] == 10:
				index[1] = 0
				index[0] += 1
			if index[0] == 10:
				index[0] = 0
			time.sleep(0.2)
		oldSw = newSw
	```

## :white_check_mark:6일차
### 1. FND 실습
- 비트곱연산, 시프트연산을 통해 하나의 숫자 형태를 만듦

	```
	def display(data, sel):
		for i in range(0, 7):
			GPIO.output(segs[i], nums[data] & (0x01 << i))
			for j in range(0, 4):
				if j == sel:
					GPIO.output(digits[j], 0)
				else:
					GPIO.output(digits[j], 1)
	```
### 2. PyQt5 사용
- vncserver-virtual : vnc 서버구동 시키는 명령어
- sudo apt install qttools5-dev-tools : qt설치
- 기본코드

	```
	import sys
	from PyQt5.QtWidgets import *

	app = QApplication(sys.argv)
	mywindow = WindowClass()
	mywindow.show()
	app.exec_()
	```
- 이벤트 함수등록
	- Qt Designer에서 이벤트함수를 등록하면 코드에 따로 안적어도 됨

## :white_check_mark:7일차
### 1. 미니프로젝트
