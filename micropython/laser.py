import machine  #importing ability to talk to device
import time     #importing ability to use time

machine.freq()
machine.freq(240000000)  #changing frequency

from machine import Pin  #ability to use pins

p4 = Pin(4, Pin.IN)      #setting GP04 as an input and assigning a variable
print(p4.value())

p5 = Pin(27, Pin.OUT)    #setting GP27 as an output and assigning a variable
print(p5.value())

while True:              #carries on forever
    if p4.value() == 1:  #if GP04 is on turn GP27 on
        p5.on()
    else:
        p5.off()         #otherwise turn GP27 off
