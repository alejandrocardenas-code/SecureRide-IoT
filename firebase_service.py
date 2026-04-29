import ufirebase as firebase
from utime import time, localtime
from config import FIREBASE_URL

firebase.setURL(FIREBASE_URL)

def guardar_evento(tipo, mensaje, extra=None):
    t = localtime(time())

    data = {
        "tipo": tipo,
        "mensaje": mensaje,
        "hora": "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5]),
        "timestamp": time()
    }

    if extra:
        data.update(extra)

    firebase.put("securide/logs", data, bg=0)