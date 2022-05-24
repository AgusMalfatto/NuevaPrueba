tupla1 = ("Agustín", "Malfatto", 21, "Programador")
lista1 = ["Nombre", "Apellido", "Edad", "Profesión"]

print("PRIMERA INSTANCIA")

for indice in lista1:
    numero = lista1.index(indice) # Accedo al índice en donde se guarda el valor
    print(f"{indice}: {tupla1[numero]}")

'''
Cambiar el dato de una tupla
'''
lista_aux = list(tupla1) # Convierto la tupla en una lista
lista_aux[3] = "Ingeniero" # Cambio el valor que deseo cambiar
tupla1 = tuple(lista_aux) # 
print("SEGUNDA INSTANCIA")

for indice in lista1:
    numero = lista1.index(indice) # Accedo al índice en donde se guarda el valor
    print(f"{indice}: {tupla1[numero]}")

''' LISTA DE TUPLAS '''

empleados = []



def Ingresar_empleado(indice):
    lista = []
    lista.append(input("Ingrese nombre: "))
    lista.append(input("Ingrese apellido: "))
    lista.append(int(input("Ingrese edad: ")))
    tupla = tuple(lista)
    empleados.append(tupla)
    return empleados

def Eliminar_empleado(indice):
    lista = list(empleados[indice])
    for i in lista:
        numero = lista.index(i)
        lista.pop(numero)
    empleados[indice] = lista
    return empleados
    


empleados = Ingresar_empleado(0)

print(empleados)

empleados = Ingresar_empleado(1)

print(empleados)

numero = int(input("Eliminar empleado: "))

empleados = Eliminar_empleado(numero)

print(empleados)