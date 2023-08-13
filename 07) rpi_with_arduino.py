# Below is the code for Arduino to be run from Arduino IDE in RPI
'''
void setup() {
    pinMode(12, INPUT_PULLUP);
    Serial.begin(9600);
}

void loop() {
    int val = digitalRead(12);
    Serial.println(val);
    delay(500);
}
'''

import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

ser = serial.serial('/dev/ttyACM0', 9600)

while True:
    s = str(int(ser.readline(), 2))
    print(s)
    if s == '1':
        GPIO.output(3, GPIO.LOW)
    else:
        GPIO.output(3, GPIO.HIGH)