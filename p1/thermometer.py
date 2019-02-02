"""
By Amir Mofakhar <amir@mofakhar.info>
"""
import time
from p1.lib import I2C_LCD_driver

import RPi.GPIO as GPIO
from p1.lib import dht11


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()
mylcd.lcd_display_string('Initializing ...', 1)


def therm():
    min_temp = None
    max_temp = None
    min_h = None
    max_h = None
    init_measurments = True
    while True:
        input_state = GPIO.input(23)
        if input_state == False:
            mylcd.lcd_clear()
            mylcd.lcd_display_string('Temperature {}C'.format(chr(223)), 1)
            mylcd.lcd_display_string('Min:{} Max:{}'.format(min_temp, max_temp), 2)
            time.sleep(5)
            mylcd.lcd_clear()
            mylcd.lcd_display_string('Humidity', 1)
            mylcd.lcd_display_string('Min:{}% Max:{}%'.format(min_h, max_h), 2)
            time.sleep(5)
            mylcd.lcd_clear()

        instance = dht11.DHT11(pin=4)
        result = instance.read()

        if result.is_valid():
            cent = result.temperature
            fah = (result.temperature * 1.8) + 32
            humidity = result.humidity

            if init_measurments:
                min_temp = max_temp = cent
                min_h = max_h = humidity
                init_measurments = False

            if cent < min_temp:
                min_temp = cent

            if cent > max_temp:
                max_temp = cent

            if humidity < min_h:
                min_h = humidity

            if humidity > max_h:
                max_h = humidity

            mylcd.lcd_display_string("Temp: %d%sC, %d%sF" % (cent, chr(223), fah, chr(223) ), 1)
            mylcd.lcd_display_string("Humidity: %d%%" % humidity, 2)


if __name__ == '__main__':
    while True:
        therm()