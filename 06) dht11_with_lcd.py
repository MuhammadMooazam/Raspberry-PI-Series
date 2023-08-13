import Adafruit_CharLCD as LCD
import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcd1 = 12
lcd2 = 7
lcd3 = 8
lcd4 = 25
lcd5 = 24
lcd6 = 23

lcd = LCD.Adafruit_CharLCD(lcd1, lcd2, lcd3, lcd4, lcd5, lcd6, 0, 16, 2)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 2)
    lcd.clear()
    lcd.message("Temp: " + str(temperature) + " C\nHumidity: " + str(humidity) + " %")
    time.sleep(1)