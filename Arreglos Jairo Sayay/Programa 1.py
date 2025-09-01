# Programa 1: Búsqueda en Arreglo Multidimensional
# Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.
# Escribe un programa que incluya una matriz bidimensional (puede ser una matriz pequeña de 3x3) con valores numéricos.
# Implementa una función que realice una búsqueda en la matriz para encontrar un valor específico que definas.
# Muestra un mensaje que indique si el valor se encontró o no, y muestra su posición en la matriz si se encontró.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numero_a_buscar = int(input("Ingrese el valor a buscar: "))

encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == numero_a_buscar:
            print("El valor se encontró en la matriz")
            print("Posición: fila", i, "columna", j)
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print("El valor no se encontró en la matriz")
