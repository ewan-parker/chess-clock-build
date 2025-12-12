# research


## Prototype:
will be a breadboard version with a oled screen just hanging off, this is what ill use to code
the finished product will be the enclosure which can press the buttons from afar or the buttons can be moved, 
it will need a way to hold the oled in place quite sturdily. 

I think we can probably get the prototype done in 2 weeks easy.


## Display:
Likely going to need two 2.42" OLED displays... heres an image of one 2.4 for reference

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/55da7888-d6f5-4517-9bb6-204e7047391b" />

**Wiring plan:**

`Pico GP4 → SDA1 → OLED1 SDA`
`Pico GP5 → SCL1 → OLED1 SCL`

`Pico GP2 → SDA2 → OLED2 SDA`
`Pico GP3 → SCL2 → OLED2 SCL`

`Pico 3.3V → VCC of both`
`Pico GND  → GND of both`

if we need to use tft's:

3.5 inch tft(https://www.amazon.ca/3-5-Display-ILI9486-ILI9488-Mega2560/dp/B0D6KYHPRX/ref=sr_1_29?crid=3NT864Y3F4UCV&dib=eyJ2IjoiMSJ9._j7jR6lCBr4mOgmiLSzL8TQv1j2qz8AFFLQ0jef2VC5VOtR7zAMAfzO2lyMBEBLgUnOJ-OOTThOQwGC0W56k78PpjRHtag2B2OuvvwhPNBYcr4oyFsbFz6Q32GjLk9WBXdaCFpi5Y86beCngseYvnlSD3fkveYnmGB9NX63aVn8W9YbMJ-X5oX5panEzY4vECXqUYP8NzBHzlSaf8LFXMN45bif6p5Q3NSACc-581LgdimHo8trbj-6d5uoPD4WDCcQg-h7IWHpD8IMcwnEJHVK6HxmY3V2u1RlqVM-66Yc.YPKBLob0PDPEiqP_WK33dp2WadxNhJu4JI8IrNL6UFc&dib_tag=se&keywords=tft%2Bdisplay&qid=1765531941&s=electronics&sprefix=tft%2Bdisplay%2Celectronics%2C128&sr=1-29&th=1)

2.4 inch tft (https://www.amazon.ca/DIYmalls-Resistive-Touchscreen-Parallel-Interface/dp/B0BFDS4YD7?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A2RJ79XBQX6W3M&utm_source=chatgpt.com)
