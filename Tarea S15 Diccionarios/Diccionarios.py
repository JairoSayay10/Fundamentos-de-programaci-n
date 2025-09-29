# ============================================
# Ejercicio: Operaciones con Diccionarios
# ============================================

# 1. CREAR UN DICCIONARIO
# Creamos un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Jairo Sayay",
    "edad": 23,
    "ciudad": "Riobamba",
    "profesion": "Licenciado en Finanzas"
}

print("1. Diccionario inicial:")
print(informacion_personal)
print("-" * 50)

# 2. ACCEDER Y MODIFICAR VALORES
# Accedemos al valor de "ciudad" y lo modificamos
print("\n2. Modificando la ciudad:")
print(f"Ciudad actual: {informacion_personal['ciudad']}")

# Modificamos la ciudad
informacion_personal["ciudad"] = "Colta"
print(f"Nueva ciudad: {informacion_personal['ciudad']}")
print("-" * 50)

# 3. VERIFICAR EXISTENCIA DE CLAVES
# Verificamos si existe la clave "telefono"
print("\n3. Verificando existencia de 'telefono':")

if "telefono" in informacion_personal:
    print("La clave 'telefono' ya existe")
else:
    print("La clave 'telefono' NO existe, agregándola...")
    informacion_personal["telefono"] = "+593 997504022"
    print(f"Teléfono agregado: {informacion_personal['telefono']}")

print("-" * 50)

# 4. ELIMINAR UNA CLAVE
# Eliminamos la clave "edad" del diccionario
print("\n4. Eliminando la clave 'edad':")

if "edad" in informacion_personal:
    edad_eliminada = informacion_personal.pop("edad")
    print(f"Se eliminó la edad: {edad_eliminada}")
else:
    print("La clave 'edad' no existe en el diccionario")

print("-" * 50)

# 5. IMPRIMIR EL DICCIONARIO FINAL
print("\n5. Diccionario final:")
print("\n--- Información Personal ---")
for clave, valor in informacion_personal.items():
    print(f"{clave.capitalize()}: {valor}")

print("\n" + "=" * 50)
print("Operaciones completadas exitosamente")
