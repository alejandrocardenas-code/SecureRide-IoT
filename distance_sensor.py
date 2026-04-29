from machine import Pin, time_pulse_us
import time

trigger = Pin(5, Pin.OUT)
echo = Pin(17, Pin.IN)

def medir_distancia():
    trigger.off()
    time.sleep_us(2)
    
    trigger.on()
    time.sleep_us(10)
    trigger.off()

    duracion = time_pulse_us(echo, 1, 30000)

    distancia = (duracion * 0.0343) / 2
    return distancia / 100  # metros