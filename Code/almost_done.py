from machine import Pin, I2C
import ssd1306
import time

# Hardware
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled1 = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
oled2 = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3D)
both_switches = Pin(9, Pin.IN, Pin.PULL_UP)
mode_button = Pin(22, Pin.IN, Pin.PULL_UP)


mode_locked = False


#Turn swithing variables:
player1 = True
last_tick = time.ticks_ms()
switch_locked = False
first_move = True
paused = False

# Game Status
currently_playing = False


# Time Control:
MODES = [
    (1, 0),   # 1 
    (2, 1),   # 2|1
    (3, 0),   # 3 
    (3, 2),   # 3|2
    (5, 0),   # 5 
    (10, 0),   # 10 
    (15, 10) # 15|10 
]

mode_index = 0
increment = 0

def apply_mode():
    global m1, s1, m2, s2, increment
    minutes, increment = MODES[mode_index]
    
    m1 = minutes
    s1 = 0
    m2 = minutes
    s2 = 0
    



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

apply_mode()

while True:
    
    now = time.ticks_ms()
    mode_value = mode_button.value()
    switch_value = both_switches.value()

    # Button press → next mode
    if not mode_locked and mode_value == 0:
        mode_index = (mode_index + 1) % len(MODES)
        apply_mode()
        player1 = True
        last_tick = time.ticks_ms()
        mode_locked = True
        time.sleep(0.15)  # debounce

    # Button release
    if mode_locked and mode_value == 1:
        mode_locked = False
        
    oled1.fill(1)
    oled2.fill(0)
    
    oled1.text("Player: White", 10 , 10, 0)
    oled1.text("Press to start!", 5 , 40 , 0)
    oled1.rect(2,25,123,35,0)
    
    oled2.text("Player: Black", 10 , 10 , 1)
    oled2.text("Time Setting:", 7 , 30 , 1)
    oled2.rect(2,25,120,35,1)
    oled2.text(str(MODES[mode_index]), 35 , 45 , 1)
    
    
    
    oled1.show()
    oled2.show()
    
    
    

    # Detect press
    if not switch_locked and switch_value == 0:
        currently_playing = True
    
    while currently_playing:
        
        now = time.ticks_ms()
        
        switch_value = both_switches.value()

        # Player switches
        if not switch_locked and switch_value == 0:
            
            if not first_move:

                # add increment to seconds and switch turn
                if player1:
                    s1 += increment
                    if s1 >= 60:
                        m1 += s1 // 60
                        s1 %= 60
                else:
                    s2 += increment
                    if s2 >= 60:
                        m2 += s2 // 60
                        s2 %= 60
            else:
                first_move = False

            player1 = not player1
            switch_locked = True
            time.sleep(0.05)   

        # release 
        if switch_locked and switch_value == 1:
            switch_locked = False
        
        
        # Leave game with cycle modes button
        
        mode_value = mode_button.value()

        if mode_value == 0 and not mode_locked:
            press_start_time = now
            mode_locked = True

        if mode_locked and mode_value == 1:
            held_time = time.ticks_diff(now, press_start_time)
            if held_time < 2000:
                paused = not paused       # short press
            else:
                currently_playing = False # long press 
                paused = False
                apply_mode()
            mode_locked = False
        
        
        
            # Update required players time based on turn, update once per second
        if not paused and time.ticks_diff(now, last_tick) >= 1000:
            
            last_tick = now
                
            if player1:
                if m1 == 0 and s1 == 0:
                    pass
                elif s1 > 0:
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
            
        if (m1 == 0 and s1 == 0):
            oled1.fill(1)
            oled1.text("Time's Up!",25,20,0)
            

        if (m2 == 0 and s2 == 0):
            oled2.fill(1)
            oled2.text("Time's Up!",25,20,0)

        
        oled1.show()
        oled2.show()
        
        time.sleep(0.02)

