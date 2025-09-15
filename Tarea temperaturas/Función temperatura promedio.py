# Función para calcular el promedio de temperaturas por ciudad
def promedio_ciudades(temperaturas):
    """
    Calcula el promedio de temperatura de cada ciudad
    considerando todas sus semanas y días.
    Parámetro:
        temperaturas (dict): Diccionario con datos en el formato
            { "Ciudad": [[semana1], [semana2], ...] }
    Retorna:
        dict: con cada ciudad y su promedio de temperatura
    """
    promedios = {}
    
    for ciudad, semanas in temperaturas.items():
        suma_total = 0
        conteo_total = 0
        
        # Recorremos semanas y días
        for semana in semanas:
            suma_total += sum(semana)
            conteo_total += len(semana)
        
        # Calcular el promedio de la ciudad
        promedios[ciudad] = suma_total / conteo_total
    
    return promedios

# Ejemplo con los datos de temperaturas
temperaturas = {
    "Quito": [
        [17, 18, 20, 24, 15, 19, 21],  # Semana 1
        [16, 17, 19, 23, 14, 18, 20],  # Semana 2
        [18, 19, 21, 25, 16, 20, 22],  # Semana 3
        [17, 18, 20, 24, 15, 19, 21]   # Semana 4
    ],
    "Guayaquil": [
        [25, 26, 27, 28, 29, 30, 31],  # Semana 1
        [24, 25, 26, 27, 28, 29, 30],  # Semana 2
        [26, 27, 28, 29, 30, 31, 32],  # Semana 3
        [25, 26, 27, 28, 29, 30, 31]   # Semana 4
    ],
    "Riobamba": [
        [17, 18, 20, 24, 15, 16, 18],  # Semana 1
        [16, 17, 19, 22, 14, 15, 17],  # Semana 2
        [18, 19, 21, 23, 16, 17, 19],  # Semana 3
        [17, 18, 20, 24, 15, 16, 18]   # Semana 4
    ]
}

# Llamada a la función
resultado = promedio_ciudades(temperaturas)

# Mostrar resultados
for ciudad, promedio in resultado.items():
    print(f"La temperatura promedio de {ciudad} en el mes fue de {promedio:.1f}°C")
