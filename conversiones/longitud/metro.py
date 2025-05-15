def metros_a_milimetros(metros):
    milimetros = (metros * 1000)
    return f'{milimetros} mm'

def metros_a_centimetros(metros):
    centimetros = (metros * 100)
    return f'{centimetros} cm'

def metros_a_decimetro(metros):
    decimetro = (metros * 10)
    return f'{decimetro} dm'

def metros_a_decametro(metros):
    decametro = (metros / 10)
    return f'{decametro} dam'

def metros_a_hectometro(metros):
    hectometro = (metros / 100)
    return f'{hectometro} hm'

def metros_a_kilometro(metros):
    kilometro = (metros / 1000)
    return f'{kilometro} km'

def recolectar_unidades(metros):
    datos = {
        'milimetros': metros_a_milimetros(metros),
        'centimetro': metros_a_centimetros(metros),
        'decimetro': metros_a_decimetro(metros),
        'decametro': metros_a_decametro(metros),
        'hectometro': metros_a_hectometro(metros),
        'kilometro': metros_a_kilometro(metros)
    }
    return datos

def mostrar_conversiones(datos, metros):
    print(f'La unidad {metros} m convertida es: ')
    for clave, valor in datos.items():
        print(f'{clave}: {valor}')
    return datos
