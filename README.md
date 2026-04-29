# 🪖 SecureRide - Smart Helmet IoT System

SecureRide es un sistema IoT basado en ESP32 que mejora la seguridad del motociclista verificando el uso correcto del casco y detectando riesgos en tiempo real.

## 🚀 Características

- Validación del casco mediante sensor MPU6050
- Sistema de encendido inteligente (relay)
- Detección de proximidad (<1.5m)
- Alertas en Telegram
- Registro en Firebase en tiempo real

## 🧠 Tecnologías

- MicroPython
- ESP32
- Firebase Realtime Database
- Telegram Bot API

## ⚙️ Cómo funciona

1. El usuario se coloca el casco
2. El sistema verifica movimientos (izq, der, adelante, atrás)
3. Si es correcto → se habilita la moto
4. Si hay objeto cercano → alerta y bloqueo

## 📡 Sensores

- MPU6050 (movimiento)
- HC-SR04 (distancia)
- Sensor táctil (casco)

## 📊 Ejemplo de eventos

- Moto encendida
- Casco mal puesto
- Peligro por proximidad