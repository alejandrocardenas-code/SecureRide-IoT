import network
import time

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, password)

        print("Conectando WiFi...")

        timeout = time.time()
        while not wlan.isconnected():
            if time.time() - timeout > 10:
                print("Error de conexión")
                return None

    print("WiFi conectado:", wlan.ifconfig())
    return wlan