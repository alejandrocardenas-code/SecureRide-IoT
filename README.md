# SecureRide - Smart Helmet IoT System

SecureRide es un sistema IoT basado en ESP32 diseñado para mejorar la seguridad de motociclistas mediante la validación del uso correcto del casco antes de permitir el encendido del vehículo, así como la detección de riesgos en tiempo real durante el recorrido.

## Descripción

El sistema utiliza sensores para verificar que el casco esté correctamente colocado y que el usuario realice ciertos movimientos necesarios para validar su uso. Solo cuando estas condiciones se cumplen, se habilita el encendido del vehículo. Además, el sistema monitorea la proximidad de objetos y genera alertas cuando se detectan posibles riesgos.

## Funcionalidades

* Validación del casco mediante sensor MPU6050
* Control de encendido del vehículo mediante relay
* Detección de proximidad con sensor ultrasónico
* Generación de alertas en tiempo real
* Registro de eventos en Firebase
* Integración con Telegram para notificaciones

## Lógica del sistema

El sistema opera bajo diferentes estados:

* SIN_CASCO: no permite el encendido
* CASCO_MAL_PUESTO: bloquea el sistema
* CASCO_OK: habilita el encendido
* PELIGRO_PROXIMIDAD: detiene el sistema y genera alerta

## Tecnologías utilizadas

* MicroPython
* ESP32
* Firebase Realtime Database
* Telegram Bot API

## Hardware

* ESP32
* MPU6050 (acelerómetro)
* Sensor ultrasónico HC-SR04
* Sensor táctil
* Relay

## Estructura del proyecto

```
SecureRide/
│
├── main.py
├── wifi.py
├── sensors.py
├── helmet_logic.py
├── firebase_service.py
├── distance_sensor.py
├── telegram_service.py
├── config.py
└── README.md
```

## Instalación

1. Clonar el repositorio:

```
git clone https://github.com/alejandrocardenas-code/SecureRide-IoT.git
```

2. Configurar las credenciales en el archivo config.py:

```
WIFI_SSID = "tu_red"
WIFI_PASSWORD = "tu_password"
FIREBASE_URL = "tu_url"
```

3. Cargar el código en el ESP32 utilizando MicroPython

4. Ejecutar el archivo main.py

## Ejemplos de eventos registrados

* Moto encendida correctamente
* Intento de encendido sin casco
* Casco mal ajustado
* Alerta de proximidad

## Objetivo

El objetivo del proyecto es mejorar la seguridad vial mediante la implementación de un sistema inteligente que valide el uso del casco y detecte situaciones de riesgo en tiempo real.

## Autor

Alejandro Cardenas

## Mejoras futuras

* Implementación de un panel web de monitoreo
* Integración con aplicaciones móviles
* Uso de modelos de aprendizaje automático para detección avanzada
* Geolocalización en tiempo real
Proyecto desarrollado como parte de un trabajo académico.