''' TIPOS DE DATOS '''
print("TIPO DE DATOS")
# Enteros

numero = 10
print(numero)
# La función 'Type' indica el tipo de dato que contiene la variable 
print(type(numero))

# Flotantes 

flotante = 5.3
print(flotante)
print(type(flotante))

# Strings: Pueden ir con comillas simples o dobles 

cadena = 'a'
nuevaCadena = "Hola"
print(cadena, nuevaCadena)
print(type(cadena))
print(type(nuevaCadena))

# Booleanos: La primera letra del valor debe estar en mayúscula 

booleano = True

print(booleano)
print(type(booleano))

# CONCATENACIÓN 

num1 = 10
num2 = 23.6
resultado = (num1 + num2) * 22 / 16

print("El resultado es: ", resultado)

''' OPERADORES ARITMÉTICOS (Mayor prioridad) '''

print("OPERADORES ARITMÉTICOS")

num1 = 8
num2 = 6

# División entera

resultado = num1 // num2
print("División entera: ", resultado)

# Resto/módulo de una división

resultado = num1 % num2
print("Resto de una división: ", resultado)

# Potencia

resultado = num1 ** num2
print("Potencia: ", resultado)

''' OPRADORES RELACIONALES (Menor prioridad) '''

'''
    > Mayor que
    < Menor que
    >= Mayor o igual que
    <= Menor o igual que
    != Diferente
    == Igual
'''

a = 10
b = 20 
c = 30

resultado = a + b == c
print("10 + 20 = 30",resultado)
print(type(resultado))

''' OPERADORES LÓGICOS (and, or, not) '''

'''
PRIORIDAD DE OPERADORES LÓGICOS
1- NOT
2- AND 
3- OR
'''
print("OPERADORES LÓGICOS")
a = 10
b = 12
c = 13
d = 10

resultado = ((a>b) or (a<c)) and (not((a==c) or (a>=b)))

print(resultado)

'''
PRIORIDAD DE LOS OPERADORES EN GENERAL
1- ()
2- **
3- *, /, resto/módulo, not
4- +, -, and 
5- >, <, ==, >=, <=, !=, or
'''

''' OPERADORES DE ASIGNACIÓN '''

a = 0

a += 5  # Suma en asignación
a -= 2  # Resta en asignación
a *= 3  # Multiplicación en asignación
a /= 3  # División en asignación
a **= 2 # Potencia en asignación
a %= 2  # Módulo en asignación

print(a)

''' SALIDA DE DATOS '''
print("SALIDA DE DATOS")
# PRIMERA FORMA

nombre = "Agustín"
edad = 21

print("Hola", nombre, "tienes", edad, "años")

# SEGUNDA FORMA (.format)

print("Hola {} tienes {} años".format(nombre, edad))

# TERCERA FORMA (f)

print(f"Hola {nombre} tienes {edad} años")

''' ENTRADA DE DATOS '''

# DATOS DE TIPO CADENA (STRINGS)
nombre = input("Digite su nombre: ")

print(f"Hola {nombre}")

# DATOS DE TIPO ENTERO (int)
numero = int(input("Digite un número: "))

print(f"El número entero es: {numero}")

# DATOS DE TIPO FLOTANTE (float)
numeroFlotante = float(input("Digite un número flotante: "))

print(f"El número flotante es: {numeroFlotante}")

''' FUNCIONES INTEGRADAS (convertir un dato de un tipo a otro) '''

a = "10"

# CADENA A ENTERO/FLOTANTE

b = int(a)
c = float(a)

# ENTERO/FLOTANTE A CADENA

d = str(b)
e = str(c)

# ENTERO A BINARIO

binario = bin(15)
print(f"15 en binario: {binario}")

# ENTERO A HEXADECIMAL

hexa = hex(15)
print(f"15 en hexadecimal: {hexa}")

# BINARIO A ENTERO ("0b número en binario", base del número)

num = int("0b1010",2)
print(f"1010 en entero: {num}")

# HEXADECIMAL A ENTERO ("0x número en hexadecimal", base del número)

nuevoNumero = int("0xf",16)
print(f"f en entero: {nuevoNumero}")

# EL ABSOLUTO DE UN NÚMERO

absoluto = abs(-36)
print(f"El ansoluto de -36 es: {absoluto}")

# REDONDEAR UN NÚMERO AL ENTERO MÁS CERCANO

redon = round(2.6)
print(f"2.6 redondeado es: {redon}")

# CONTAR CANTIDAD DE CARACTERES DE UNA CADENA

palabra = len("Agustín")
print(f"Agustín tiene {palabra} caracteres")