''' ELEMENTOS BÁSICOS '''
# Expresiones en forma algorítmica

a = float(input("Ingrese primer número: "))
b = float(input("Ingrese segundo número: "))
c = float(input("Ingrese tercer número: "))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)

print(f"El resultado es: {resultado}")

nuevoResultado = ((3+5*8) < 3 and (((-6/3)*4) - 2 < 2)) or (a>b)

print(f"El resultado es: {nuevoResultado}")

''' INTERCAMBIAR EL VALOR DE DOS VARIABLES '''

primero = int(input("Ingrese el primero: "))
segundo = int(input("Ingrese el segundo: "))

primero, segundo = segundo, primero

print(f"Primero: {primero} --- Segundo {segundo}")
