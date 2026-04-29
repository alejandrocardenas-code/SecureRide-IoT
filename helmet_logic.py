moved_sides = set()

def evaluar_movimiento(x, z):
    if x > 4500:
        moved_sides.add("derecha")
    elif x < -4500:
        moved_sides.add("izquierda")

    if z > 7000:
        moved_sides.add("adelante")
    elif z < -5000:
        moved_sides.add("atras")

def casco_correcto():
    if len(moved_sides) >= 4:
        moved_sides.clear()
        return True
    return False