# hardware-platform-2024
:fire:IoT 개발자과정 오픈 하드웨어 플랫폼활용 리포지토리:rocket:

## 1일차
1. 라즈베리파이 기초
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
	- 전압차로 인해 전류는 높은 곳(5v)에서 낮은 곳(0v)에서 흐름
		- GND(기준전압)의 역할 : 전류를 모이게 함(모든 전류는 GND로 흐름)
		- 예를 들어, 21번 핀을 키려면 LOW을 걸어줘야 함(5v -> 0v로 흐르도록 전압차를 줌) HIGH를 준다면 전압차가 없어서 안켜짐!

2. GPIO모둘 기본함수
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

3. 풀업(Pull-Up)저항과 풀다운(Pull-Down)저항
	- 플로팅 상태를 방지하기 위해 풀업 저항과 풀다운 저항 사용
		- 플로팅(Floating) : LOW인지 HIGH인지 알 수 없는 상태, 0과 1이 번갈아 나타나는 불안정한 상태
	- 풀업저항
		- 저항을 VCC(전원) 쪽에 걸어 입력을 받지 않은 상태일 때 HIGH로 끌어올리고, 입력을 받았을 때는 LOW로 끌어내리는 회로
		![풀업](https://raw.githubusercontent.com/guswlrla/hardware-platform-2024/main/images/pull-up.png)
	- 풀다운저항
		- 저항을 GND(접지) 쪽에 걸어 입력을 받지 않은 상태일 때 LOW로 끌어내리고, 입력을 받았을 때는 HIGH으로 끌어올리는 회로
		![풀다운](https://raw.githubusercontent.com/guswlrla/hardware-platform-2024/main/images/pull-down.png)

4. 인터럽트



GPIO.PWM 함수도 찾아보고 적기!!
----------------------------------------------------------------------------------------------------------------------------------


인터럽트 = 우선순위

pwm - 펄스 폭을 제어해서 ?? 어쩌구,, 
duty = on 되는 시간

인터럽트랑 스위치 파일 수정!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!