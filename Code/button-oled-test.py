## A program i made to test one screen and one button in isolation.
from machine import Pin, I2C
import ssd1306
import time

# I2C OLED
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

button = Pin(10, Pin.IN, Pin.PULL_UP)

x = 0
y = 20
dx = 6 
dy = 6



oled.fill(0)
oled.text("OLED OK", 0, 0)
oled.text("Press button", 0, 16)
oled.show()

while True:
    if not button.value():
        while True:
            
            oled.fill(0)
            oled.rect(x, y, 32, 15, 1)
            oled.text("BEN",x+3,y+4)
            
            x += dx
            if x > 118 - 10:
                dx = -dx
            elif x < 0:
                dx = -dx
                
            y += dy
            if y > 54 - 10:
                dy = -dy
            elif y < 0:
                dy = -dy
                
        
            oled.show()
            time.sleep(0.3)  # debounce
