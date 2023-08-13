import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

while True:
    GPIO.output(3, True)
    time.sleep(1) #Put time in seconds
    GPIO.output(3, False)
    time.sleep(1)