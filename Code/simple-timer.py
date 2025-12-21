from machine import Pin, I2C
import ssd1306
import time

# I2C OLED
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

button = Pin(10, Pin.IN, Pin.PULL_UP)

m = 2 # 2 Minutes
s = 5 # 5 Seconds

while m > 0 or s > 0:
    
    oled.fill(0)
    
    
    oled.text(str(m),10,5)
    
    if s >= 10:
        oled.text(str(s),25,5)
    else:
        oled.text("0" + str(s),25,5)
    oled.text(":", 18,5)
        
    
    if s != 0:
        s = s - 1
    else:
        m = m-1
        s = 60
        
    
    oled.show()
    
    time.sleep(1)
    
oled.fill(0)
oled.text("Times up!",10,5)
oled.show()
time.sleep(5)
