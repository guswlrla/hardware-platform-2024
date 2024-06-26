import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


pin = (17, 26, 16, 25, 27, 4, 18)
digits = (22, 5, 19, 20)

swPin = 6
oldSw = 0
newSw = 0


index = [0, 0, 0, 0]


GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


for a in pin:
    GPIO.setup(a, GPIO.OUT)
    GPIO.output(a, 0)

for b in digits:
    GPIO.setup(b, GPIO.OUT)
    GPIO.output(b, 1)

list = {
    '0': (1, 1, 1, 1, 1, 1, 0, 0),
    '1': (0, 1, 1, 0, 0, 0, 0, 0),
    '2': (1, 1, 0, 1, 1, 0, 1, 0),
    '3': (1, 1, 1, 1, 0, 0, 1, 0),
    '4': (0, 1, 1, 0, 0, 1, 1, 0),
    '5': (1, 0, 1, 1, 0, 1, 1, 0),
    '6': (1, 0, 1, 1, 1, 1, 1, 0),
    '7': (1, 1, 1, 0, 0, 1, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1, 0),
    '9': (1, 1, 1, 1, 0, 1, 1, 0)
}

def displayNum(index):
    for i in range(7):
        GPIO.output(pin[i], list[str(index)][i])

def displaydigit():
    for i in range(4):
        displayNum(index[i])
        GPIO.output(digits[i], 0)
        time.sleep(0.001)
        GPIO.output(digits[i], 1)

try:
    while True:
        newSw = GPIO.input(swPin)

        displaydigit()

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

except KeyboardInterrupt:
    GPIO.cleanup()
