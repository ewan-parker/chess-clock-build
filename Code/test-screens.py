from machine import Pin, I2C
import ssd1306
import time

# I2C OLED
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled1 = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
oled2 = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3D)

button = Pin(10, Pin.IN, Pin.PULL_UP)


while True:
    oled1.text("Screen 1",5,5)
    oled2.text("Screen 2",5,5)
    oled1.show()
    oled2.show()
    
