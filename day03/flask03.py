# URL 접속을 /led/on, /led/off로 접속하면
# led를 on, off하는 웹페이지를 만들기

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
	
@app.route("/led/on")
def led_on():
	GPIO.output(led, False)
	return "켜져랏!!!"

@app.route("/led/off")
def led_off():
	GPIO.output(led, True)
	return "꺼져랏!!!"

@app.route("/cleanup")
def cleanup():
	GPIO.cleanup()
	return "쓱싹쓱싹"

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "10201", debug = True)
