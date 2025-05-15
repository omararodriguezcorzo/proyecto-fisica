import math

def obtener_componentes(magnitud, direccion):
    direccion = direccion.upper().strip()  
    direcciones_validas = {"N", "S", "E", "O", "NE", "NO", "SE", "SO"}

    if direccion not in direcciones_validas:
        print("Error: Dirección no válida. Usa: N, S, E, O, NE, NO, SE, SO.")
        return (0, 0)

    if direccion == "N":
        return (0, magnitud)
    elif direccion == "S":
        return (0, -magnitud)
    elif direccion == "E":
        return (magnitud, 0)
    elif direccion == "O":
        return (-magnitud, 0)
    elif direccion == "NE":
        return (magnitud / math.sqrt(2), magnitud / math.sqrt(2))
    elif direccion == "NO":
        return (-magnitud / math.sqrt(2), magnitud / math.sqrt(2))
    elif direccion == "SE":
        return (magnitud / math.sqrt(2), -magnitud / math.sqrt(2))
    elif direccion == "SO":
        return (-magnitud / math.sqrt(2), -magnitud / math.sqrt(2))

def calcular_resultante(vectores):
    """Calcula la suma de los vectores y devuelve su magnitud y ángulo."""
    R_x = sum(v[0] for v in vectores)
    R_y = sum(v[1] for v in vectores)

    magnitud_R = math.sqrt(R_x ** 2 + R_y ** 2)
    angulo_R = math.degrees(math.atan2(R_y, R_x)) % 360

    return R_x, R_y, magnitud_R, angulo_R