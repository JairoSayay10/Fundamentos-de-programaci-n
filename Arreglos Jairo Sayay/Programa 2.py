# Programa 2: Ordenación de Arreglo Multidimensional
# Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.
# Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).
# Implementa un algoritmo que ordene todos los números de la matriz en orden ascendente y los coloque en una nueva matriz.
# Muestra la matriz original y la nueva matriz ordenada.

matriz = [
    [9, 3, 7],
    [5, 8, 1],
    [4, 6, 2]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Convertir la matriz en una lista simple
numeros = []
for fila in matriz:
    for valor in fila:
        numeros.append(valor)

# Ordenar todos los números
numeros.sort()

# Crear una nueva matriz 3x3 con los números ordenados
nueva_matriz = [
    numeros[0:3],
    numeros[3:6],
    numeros[6:9]
]

print("\nNueva matriz con los números ordenados:")
for fila in nueva_matriz:
    print(fila)
