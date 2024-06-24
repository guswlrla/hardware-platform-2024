# URL 접속을 /led/on, /led/off로 접속하면
# led를 on, off하는 웹페이지를 만들자
from flask import Flask
import RPi.GPIO as GPIO

led = 4

app = Flask(__name__)

@app.route("/")
def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, True)
	return "Hello flask!!"

@app.route("/led/<state>")
def control(state):
	if state == "on":
		GPIO.output(led, False)
		return "켜져랏!!"
	elif state == "off":
		GPIO.output(led, True)
		return "꺼져랏!!"
	elif state == "clear":
		GPIO.cleanup()
		return "쓱삭쓱삭"

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "10001", debug = True)
