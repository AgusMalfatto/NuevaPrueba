'''# ESTRUCTURA DE DATOS

# LISTAS

lista = [20, 13, -8, "hola", True]
lista_vacia = []

#Agregar elementos

lista.append('Banano')

lista.insert(2, "Yamila")

# Eliminar 

print(lista)

indice = 4

eliminado = lista.pop(indice)

del lista[indice]

print(lista)
print(eliminado)'''

'''# TUPLAS

tupla = (20, 'hola' , 3, "hola")
tupla_2 = (55, 'Yamila', 'hola')

tupla_3 = tupla + tupla_2

verificar = 20 in tupla_3

print(verificar)'''

#Diccionarios
'''
dic = {
    'nombre' : 'Yamila',
    'apellido' : 'Malfatto',
    'edad' : 26
}

dic['nombre'] = 'Carolina'

dic_2 = dic

dic_2['edad'] = 23

print(dic_2)
print(dic)'''
'''
numero = int(input("Ingrese número: "))

if numero == 5:
    print("Sos un genio")
elif (numero == 4) or (numero == 6):
    print("Cerca")
else:
    print("Puto el que lo lea")'''

'''contador = 0

while contador < 10:
    print(contador)
    contador = contador + 1

print("final")'''

cadena = 'Yamila22'
cadena_nueva = ""

tupla = ('a', 'e', 'i', 'o', 'u')

for i in cadena:
    if i in tupla:
        cadena_nueva = cadena_nueva + i

print(cadena_nueva)





