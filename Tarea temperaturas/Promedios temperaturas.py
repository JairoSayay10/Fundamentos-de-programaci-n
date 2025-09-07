#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
#Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
#Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.
# Matriz 3D: ciudades x semanas x días
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

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for ciudad, semanas in temperaturas.items():
    for i, semana in enumerate(semanas):
        promedio = sum(semana) / len(semana)
        print(f"En {ciudad} La temperatura promedio en la semana {i+1} del mes de Agosto fue de = {promedio:.1f}°C")
