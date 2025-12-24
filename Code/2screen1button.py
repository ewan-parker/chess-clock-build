from machine import Pin, I2C
import ssd1306
import time

# I2C OLED
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled1 = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
oled2 = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3D)
button = Pin(10, Pin.IN, Pin.PULL_UP)

button = Pin(10, Pin.IN, Pin.PULL_UP)

player1 = True
last_button = 1
last_tick = time.ticks_ms()


m1 = 2 # Player 1 Minutes
s1 = 0 # Player 1 Seconds

m2 = 2 # Player 2 Minutes
s2 = 0 # Player 2 Seconds









# Main loop

while not (m1 == 0 and s1 == 0) and not (m2 == 0 and s2 == 0):
    
    now = time.ticks_ms()
    
    #Change turn on button pressed.
    current = button.value()
    if last_button == 1 and current == 0:
        player1 = not player1
        time.sleep(0.15)  # debounce
    last_button = current
    
    
    # # Update required players time based on turn, update once per second
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
        

    

    #Print minutes   
    oled1.fill(0)
    oled1.text(str(m1),10,10)
            
    #Print seconds
    if s1 >= 10:
        oled1.text(str(s1),25,10)
    else:
        oled1.text("0" + str(s1),25,10)
    oled1.text(":", 18,10)

    #Print minutes   
    oled2.fill(0)
    oled2.text(str(m1),10,10)
            
    #Print seconds
    if s2 >= 10:
        oled2.text(str(s2),25,10)
    else:
        oled2.text("0" + str(s2),25,10)
    oled2.text(":", 18,10)
        
    
    oled1.show()
    oled2.show()
    
    time.sleep(0.02)
                
                
        
        
        
        
        
        
