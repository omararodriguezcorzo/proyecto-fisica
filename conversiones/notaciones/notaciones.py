def decimal_a_cientifica(numero, decimales = 9):
    mantisa, exponente = f"{numero:.{decimales}e}".split("e")

    # Elimina los ceros a la derecha
    mantisa = mantisa.rstrip("0").rstrip(".")
    return f"{mantisa}e{int(exponente)}"

def cientifica_a_decimal(notacion_cientifica):
    return float(notacion_cientifica)