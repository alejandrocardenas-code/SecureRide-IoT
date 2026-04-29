import time
from wifi import connect_wifi
from sensors import *
from helmet_logic import *
from distance_sensor import medir_distancia
from firebase_service import guardar_evento
from telegram_service import enviar_mensaje
from config import *

wifi = connect_wifi(WIFI_SSID, WIFI_PASSWORD)

estado = "SIN_CASCO"

if wifi:

    print("Sistema SecureRide activo")

    while True:
        x, z = leer_movimiento()
        evaluar_movimiento(x, z)

        distancia = medir_distancia()

        # 🚨 PROXIMIDAD
        if distancia < DISTANCIA_LIMITE:
            estado = "PELIGRO_PROXIMIDAD"
            apagar_moto()
            
            mensaje = f"Peligro: objeto a {distancia:.2f}m"
            print(mensaje)

            guardar_evento("ALERTA", mensaje, {"distancia": distancia})
            enviar_mensaje(mensaje)

            time.sleep(2)
            continue

        # 🪖 CASCO
        if not casco_puesto():
            estado = "SIN_CASCO"
            apagar_moto()

            print("Casco no puesto")
            guardar_evento("ERROR", "Intento sin casco")

        else:
            if casco_correcto():
                estado = "CASCO_OK"
                encender_moto()

                print("Moto encendida")
                guardar_evento("OK", "Moto encendida correctamente")

            else:
                estado = "CASCO_MAL_PUESTO"
                apagar_moto()

                print("Casco mal ajustado")
                guardar_evento("ERROR", "Movimiento incompleto")

        print("Estado actual:", estado)
        time.sleep(1)