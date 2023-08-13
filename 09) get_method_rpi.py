import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import urllib.request

pin = 2

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
    
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f} *C Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    
    time.sleep(2)
    
    f = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=44HACA5Y9FH1MKU7&field1=%s&field2=%s" % (temperature, humidity))
    print(f.read())
    f.close()