from machine import Pin, SoftI2C
import mpu6050

# MPU6050
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
mpu = mpu6050.accel(i2c)

# Sensor táctil (casco puesto)
sensor_casco = Pin(18, Pin.IN)

# Relay (moto)
relay = Pin(4, Pin.OUT)

def leer_movimiento():
    data = mpu.get_values()
    return data['AcX'], data['AcZ']

def casco_puesto():
    return sensor_casco.value() == 1

def encender_moto():
    relay.value(1)

def apagar_moto():
    relay.value(0)