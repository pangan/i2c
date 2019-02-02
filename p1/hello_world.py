"""
By Amir Mofakhar <amir@mofakhar.info>
"""
from p1.lib import I2C_LCD_driver
import time

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()

def scroll_text():
    str_pad = ' ' * 16
    my_long_string = "This is a string that needs to scroll"
    my_long_string = str_pad + my_long_string

    for i in range(0, len(my_long_string)):
        lcd_text = my_long_string[i:(i + 16)]
        mylcd.lcd_display_string(lcd_text, 1)
        time.sleep(0.2)
        mylcd.lcd_display_string(str_pad, 1)


def print_time():
    mylcd.lcd_clear()
    while True:
        mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
        mylcd.lcd_display_string("Date: %s" %time.strftime("%m/%d/%Y"), 2)
        time.sleep(1)

def custom_font():
    fontdata1 = [
        # char(0) - Upper-left character
        [0b01111,
         0b10100,
         0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b00000,
         0b00000],
        [0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00000,
         0b00000],
        [0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b10001,
         0b11111,
         0b00000,
         0b00100],
        [0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00001,
         0b11111,
         0b00000,
         0b00100],


    ]

    mylcd.lcd_load_custom_chars(fontdata1)

    mylcd.lcd_write(0x80)
    mylcd.lcd_write_char(1)
    mylcd.lcd_write_char(3)
    mylcd.lcd_write_char(1)
    mylcd.lcd_write_char(3)
    mylcd.lcd_write_char(2)
    mylcd.lcd_write_char(0)

    # line 2
    # mylcd.lcd_write(0xC0)
    # mylcd.lcd_write_char(3)

if __name__ == '__main__':
    print_time()
