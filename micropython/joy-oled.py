from machine import ADC, Pin
import ssd1306, time

I2C_SDA_PIN = 0
I2C_SCL_PIN = 1
i2c = machine.I2C(0,sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)

# using default address 0x3C
display = ssd1306.SSD1306_I2C(128, 32, i2c)

#display.text('Hello, World!', 0, 0, 1)
#display.show()

display.fill(0)

#display.show()

adcx = ADC(Pin(26))             # create ADC object on ADC pin
adcy = ADC(Pin(27))             # create ADC object on ADC pin

while True:
    xvalue = int(adcx.read_u16() / 512)        # read value, 0-65535 across voltage range 0.0v - 3.3v
    yvalue = int(adcy.read_u16() / 2048)        # read value, 0-65535 across voltage range 0.0v - 3.3v
    display.text('X: ' + str(xvalue), 0, 0, 1)
    display.text('Y: ' + str(yvalue), 0, 10, 1)
    display.pixel(xvalue,yvalue,1)
    display.show()
    if (xvalue == 0 and yvalue == 0):
        display.fill(0)
    display.text('X: ' + str(xvalue), 0, 0, 0)
    display.text('Y: ' + str(yvalue), 0, 10, 0)
#    time.sleep(.01)

#for line in range(128):
#    display.vline(line, 0, 32, 1)
#    display.show()
    
      
