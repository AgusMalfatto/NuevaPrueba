import math

radio = float(input("Ingrese el radio: "))

#math.pi es el número pi dentro de la biblioteca "math"
area = math.pi * radio**2
longitud = 2 * math.pi * radio
 
#Imprimir solo dos decimales= :.2f
print(f"El área es: {area:.2f}")
print(f"La longitud es: {longitud:.2f}")

precio = float(input("Ingrese el precio: "))

descuento = precio * 0.15

precioFinal = precio - descuento

print(f"El precio final es: ${precioFinal:.2f}")