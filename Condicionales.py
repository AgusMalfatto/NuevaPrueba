''' CONDICIONALES '''

numero = int(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es 'cero'")
else:
    print("El número es negativo")

''' CONDICIONALES COMBINADOS '''

if numero > 0 and numero < 100:
    print("Edad correcta")
    if numero >= 18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")

if 0 < numero < 100:
    print("Edad correcta")
    if numero >= 18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")


''' PARIDAD E IMPARIDAD '''

num1 = int(input("Digite el primer número: "))
num2 = int(input("Digite el segundo número: "))

if num1%2 == 0 and num2%2 == 0:
    print("Ambos son pares")
elif num1%2 == 0 and num2%2 != 0:
    print(f"{num1} es par")
elif num1%2 != 0 and num2%2 == 0:
    print(f"{num2} es par")    
else: 
    print("Ninguno es par")

''' MAYOR NÚMERO '''

numero_uno = int(input("Digite el primer número: "))
numero_dos = int(input("Digite el segundo número: "))
numero_tres = int(input("Digite el tercer número: "))

if numero_uno >= numero_dos and numero_uno >= numero_tres:
    print(f"El primer número es el más grande ({numero_uno})")
elif numero_dos >= numero_uno and numero_dos >= numero_tres:
    print(f"El segundo número es el más grande ({numero_dos})")
else:
    print(f"El tercer número es el mas grande ({numero_tres})")