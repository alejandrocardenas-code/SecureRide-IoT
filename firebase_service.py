import ufirebase as firebase
from utime import time, localtime
from config import FIREBASE_URL

firebase.setURL(FIREBASE_URL)

def guardar_evento(mensaje):
    t = localtime(time())

    data = {
        "mensaje": mensaje,
        "fecha": "{:02d}/{:02d}/{:04d}".format(t[2], t[1], t[0]),
        "hora": "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5]),
        "timestamp": time()
    }

    firebase.put("securide/eventos", data, bg=0)