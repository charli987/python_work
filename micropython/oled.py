import machine
import ssd1306
from machine import Pin
import time

I2C_SDA_PIN = 0
I2C_SCL_PIN = 1
i2c=machine.I2C(0,sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)

print('Scanning I2C bus.')
devices = i2c.scan() # this returns a list of devices

device_count = len(devices)

if device_count == 0:
    print('No i2c device found.')
else:
    print(device_count, 'devices found.')

for device in devices:
    print('Decimal address:', device, ", Hex address: ", hex(device))




# using default address 0x3C
display = ssd1306.SSD1306_I2C(128, 32, i2c)

#display.fill(0)
#display.text('Hello, World!', 26, 24, 1)
#display.show()


p5 = Pin(27, Pin.IN)     # create input pin on GPIO2
print(p27.value())# get value, 0 or 1
#while True:
    #while p27.value() == 1:
        #display.fill(1)
        #display.text('Hello!', 26, 24, 0)
        #display.show()
        #time.sleep(0.5)
        #display.fill(0)
        #display.show()
        #time.sleep(0.5)
        

while True:
    x = 0
    y = 0
    con = 10
    while p27.value() == 1:
        display.invert(1)
        display.contrast(con)
        display.text('Hello!', x, y, 1)
        display.show()
        display.text('Hello!', x, y, 0)
        time.sleep(1)
        con += 70
        display.invert(0)
        time.sleep(1)
        x += 15
        y += 5
    else:
        display.fill(0)
        display.text("Bye", 0, 0, 1)
        display.show()
        time.sleep(1)
        display.text("Bye", 0, 0, 0)
        display.show()
        display.fill(1)
        display.fill_rect(5, 5, 250, 250, 0)
        display.show()
        time.sleep(1)
        

        
        

#display.poweroff()     # power off the display, pixels persist in memory
#display.poweron()      # power on the display, pixels redrawn
#display.contrast(0)    # dim
#display.contrast(255)  # bright
#display.invert(1)      # display inverted
#display.invert(0)      # display normal
#display.rotate(True)   # rotate 180 degrees
#display.rotate(False)  # rotate 0 degrees
#display.show()  


#display.fill(0)
#display.fill_rect(0, 0, 32, 32, 1)
#display.fill_rect(2, 2, 28, 28, 0)
#display.vline(9, 8, 22, 1)
#display.vline(16, 2, 22, 1)
#display.vline(23, 8, 22, 1)
#display.fill_rect(26, 24, 2, 4, 1)
#display.text('MicroPython', 40, 0, 1)
#display.text('SSD1306', 40, 12, 1)
#display.text('OLED 128x32', 40, 24, 1)
#display.show()

