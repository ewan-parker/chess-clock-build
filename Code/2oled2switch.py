from machine import Pin, I2C
import ssd1306
import time

# Hardware
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled1 = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
oled2 = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3D)
both_switches = Pin(9, Pin.IN, Pin.PULL_UP)


#Turn swithing variables:
player1 = True
last_switch = 1
last_tick = time.ticks_ms()
switch_locked = False


m1 = 2 # Player 1 Minutes
s1 = 0 # Player 1 Seconds

m2 = 2 # Player 2 Minutes
s2 = 0 # Player 2 Seconds



#BIG NUMBERS:


SEGMENTS = {
    "0": (1,1,1,1,1,1,0),
    "1": (0,1,1,0,0,0,0),
    "2": (1,1,0,1,1,0,1),
    "3": (1,1,1,1,0,0,1),
    "4": (0,1,1,0,0,1,1),
    "5": (1,0,1,1,0,1,1),
    "6": (1,0,1,1,1,1,1),
    "7": (1,1,1,0,0,0,0),
    "8": (1,1,1,1,1,1,1),
    "9": (1,1,1,1,0,1,1)
}

def draw_digit(oled, d, x, y, w=24, h=40, t=5):
    seg = SEGMENTS[d]

    if seg[0]:
        oled.fill_rect(x+t, y, w-2*t, t, 1)
    if seg[1]:
        oled.fill_rect(x+w-t, y+t, t, h//2-t, 1)
    if seg[2]:
        oled.fill_rect(x+w-t, y+h//2, t, h//2-t, 1)
    if seg[3]:
        oled.fill_rect(x+t, y+h-t, w-2*t, t, 1)
    if seg[4]:
        oled.fill_rect(x, y+h//2, t, h//2-t, 1)
    if seg[5]:
        oled.fill_rect(x, y+t, t, h//2-t, 1)
    if seg[6]:
        oled.fill_rect(x+t, y+h//2-t//2, w-2*t, t, 1)
        
        
        
def draw_time(oled, m, s):
    oled.fill(0)

    digits = "{:02d}{:02d}".format(m, s)

    x = 4        # left margin
    y = 10       # vertical centering

    for i, ch in enumerate(digits):
        draw_digit(oled, ch, x, y)
        x += 30

        if i == 1:
            oled.fill_rect(x-3, y+12, 6, 6, 1)
            oled.fill_rect(x-3, y+24, 6, 6, 1)
            x += 6



# Main loop

while not (m1 == 0 and s1 == 0) and not (m2 == 0 and s2 == 0):
    
    
    now = time.ticks_ms()
    
    
    switch_value = both_switches.value()


    # Detect press
    if not switch_locked and switch_value == 0:
        player1 = not player1
        switch_locked = True
        time.sleep(0.05)   

    # Detect release 
    if switch_locked and switch_value == 1:
        switch_locked = False
    
    
    
    
    
    
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
            
        

    

    draw_time(oled1, m1, s1)
    draw_time(oled2, m2, s2)
    
    if player1:
        oled1.line(0,63,128,63,1) # bottom border
        oled1.line(0,1,128,1,1) # top border
        oled1.line(0,1,0,64,1) # left border
        oled1.line(127,1,127,64,1) # right border
    else:
        oled2.line(0,63,128,63,1) # bottom border
        oled2.line(0,1,128,1,1) # top border
        oled2.line(0,1,0,64,1) # left border
        oled2.line(127,1,127,64,1) # right border
    
    oled1.show()
    oled2.show()
    
    time.sleep(0.02)
