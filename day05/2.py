import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

seg = (21, 22, 23, 24, 25, 6, 12)
digits = (13, 19, 5, 17)
swPin = 26

for led in seg:
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, 0)

for i in digits:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, 1)

segment = {
    0: (1, 1, 1, 1, 1, 1, 0, 0),
    1: (0, 1, 1, 0, 0, 0, 0, 0),
    2: (1, 1, 0, 1, 1, 0, 1, 0),
    3: (1, 1, 1, 1, 0, 0, 1, 0),
    4: (0, 1, 1, 0, 0, 1, 1, 0),
    5: (1, 0, 1, 1, 0, 1, 1, 0),
    6: (1, 0, 1, 1, 1, 1, 1, 0),
    7: (1, 1, 1, 0, 0, 1, 0, 0),
    8: (1, 1, 1, 1, 1, 1, 1, 0),
    9: (1, 1, 1, 1, 0, 1, 1, 0)
}

GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def display_digit(number, digit_index):
	for loop in range(7):
		GPIO.output(seg[loop], segment[number][loop])
		GPIO.output(digits[digit_index], 0)
		time.sleep(0.005)
		GPIO.output(digits[digit_index], 1)

def display_number(number):
	thousands = number // 1000
	hundreds = (number // 100) % 10
	tens = (number // 10) % 10
	ones = number % 10

	for _ in range(50):
		display_digit(thousands, 0)
		display_digit(hundreds, 1)
		display_digit(tens, 2)
		display_digit(ones, 3)

try:
	count = -1
	while True:
		if GPIO.input(swPin) == False:
			time.sleep(0.01)
			if GPIO.input(swPin) == False:
				count = (count + 1) % 10000
				print("Display number:", count)
				while GPIO.input(swPin) == GPIO.LOW:
					time.sleep(0.1)

			display_number(count)
			time.sleep(0.005)

except KeyboardInterrupt:
	GPIO.cleanup()
