# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Cálculo del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal interactivo de usuario de ventas del centro comercial XYZ
print("=== Cálculo de Descuentos ===")

# Primera compra: usuario de ventas ingresa solo el monto (usa descuento del 10% por defecto ventas promocionales del centro comercial)
monto1 = float(input("Ingrese el monto de la primera compra: "))
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

print("\nCompra 1")
print("Monto total:", monto1)
print("Descuento aplicado (10%):", descuento1)
print("Monto final a pagar:", monto_final1)

# Segunda compra: usuario ingresa monto y también el descuento segun las promociones del centro comercial para segunda compra
monto2 = float(input("\nIngrese el monto de la segunda compra: "))
porcentaje2 = float(input("Ingrese el porcentaje de descuento a aplicar por promocion de segunda compra: "))
descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2

print("\nCompra 2")
print("Monto total:", monto2)
print("Descuento aplicado (" + str(porcentaje2) + "%):", descuento2)
print("Monto final a pagar:", monto_final2)
print("valor total a pagar por las dos compras:", monto_final1 + monto_final2)
print("\n=============================")
print("Gracias por su compra!")