from machine import Pin, I2C
import ssd1306
import time

# I2C OLED
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

button = Pin(10, Pin.IN, Pin.PULL_UP)

m1 = 2 # Player 1 Minutes
s1 = 0 # Player 1 Seconds

m2 = 2 # Player 2 Minutes
s2 = 0 # Player 2 Seconds

player1 = True
last_button = 1

# timer logic
last_tick = time.ticks_ms()

while not (m1 == 0 and s1 == 0) and not (m2 == 0 and s2 == 0):
    
    now = time.ticks_ms()
    
    #Change turn on button pressed.
    current = button.value()
    if last_button == 1 and current == 0:
        player1 = not player1
        time.sleep(0.15)  # debounce
    last_button = current
    
    
    # Update required players time based on turn, update once per second
    if time.ticks_diff(now, last_tick) >= 1000:
        last_tick = now
        
        if player1:
            if m1 == 0 and s1 == 0:
                pass
            elif s1 > 0 :
                s1 -= 1
            else:
                m1 = m1-1
                s1 = 59
        else:
            if m2 == 0 and s2 == 0:
                pass
            elif s2 > 0:
                s2 -= 1
            else:
                m2 -= 1
                s2 = 59
    
    
    
    
    #Print the current times:
    
    oled.fill(0)
    
    #Print player 1 time.
    oled.text(str(m1),10,10)
    
    if s1 >= 10:
        oled.text(str(s1),25,10)
    else:
        oled.text("0" + str(s1),25,10)
    oled.text(":", 18,10)
    
    
    #Lines to enclose times
    oled.line(5,5,5,20,1)
    oled.line(50,5,50,20,1)
    oled.line(95,5,95,20,1)
    
    oled.line(5,5,95,5,1)
    oled.line(5,20,95,20,1)
    
    if player1:
        oled.line(20,35,25,30,1)
        oled.line(25,30,30,35,1)
    else:
        oled.line(70,35,75,30,1)
        oled.line(75,30,80,35,1)
    
    
    #Print player 2 time.
    oled.text(str(m2),60,10)
    
    if s2 >= 10:
        oled.text(str(s2),75,10)
    else:
        oled.text("0" + str(s2),75,10)
    oled.text(":", 68,10)
    

    oled.show()
    
    time.sleep(0.02)
    
    
oled.fill(0)
oled.text("Times up!",10,5)
oled.show()
time.sleep(5)
