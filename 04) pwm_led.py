import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

P = GPIO.PWM(3, 100)
P.start(0)

while True:
    for x in range (100):
        P.start(x)
        time.sleep(0.1)
    for x in range (100):
        P.start(100-X)
        time.sleep(0.1)