''' TIPOS DE ALMACENAMIENTO DE DATOS '''

# LISTAS

''' 
Mutables: se puede editar el dato
Ordenados: basado en un índice que inicia en 'cero'
Los datos dentro no están relacionados entre sí
'''
cadena = "Hola soy pepe"
cadena_lista = cadena.split() # Separa cada elemento de la cadena y arma una lista
'''
cadena_lista = cadena.split(", ") indicamos el tipo de separador que queremos usar
'''

lista1 = [1, 2 , 3, 4] # Alacena varios datos
lista2 = ["Hola", 39, 20.3] # Puede almacenar distintos tipos de datos
lista = ["Manu", "Agus", "Pepe", "Mati Bombón"]


'''
    posición 0 => primer elemento
    posición 1 => segundo elemento
    posición 3 => tercer elemento
    ...
'''

copia_lista = [num * 5 for num in lista1] # Se puede colocar una función en la modificación de los elementos de la lista
'''
for num in lista1:
    copia = num * 5
    copia_lista.append(copia)
'''
lista.append("Josesito") # Agrego un elemento a la lista en la última posición
lista.insert(3, "Messi") # Agrego un elemento a la lista en la posición que deseo
lista.pop(2) # Elimino el elemento de una lista 

agus = "Agus" in lista # Corrobora que 'Agus' se encuentre en la lista. Devuelve un booleano
indice = lista.index("Agus") # Me devuelve la posición en la que está 'Agus'
contador = lista.count("Messi") # Devuelve la cantidad de veces que se repite el valor 
long = len(lista) # Devuelve la cantidad de valores que tiene la lista

print(f"Lista1: {lista1}")
print(f"Lista2: {lista2}")
print(f"Lista: {lista}")
print(f"Copio la lista1 por 5: {copia_lista}")
print(f"¿Está 'Agus' en la lista: {agus}")
print(f"'Agus' se encuentra en la posición: {indice}")
print(f"Cantidad de veces que está 'Messi': {contador}")
print(f"Cantidad de valores: {long}")

# TUPLAS

'''
No son mutables: No se puede modificar el dato 
Ordenados: basado en un índice que inicia en 'cero'
Los datos están relacionados entre sí
'''

tupla1 = ("Agustín", 21)
tupla2 = ("José", 23)

tupla_Aux = tupla1 + tupla2 # Unifico ambas tuplas en una sola
tupla_Aux = tupla_Aux + ("Martina", 25) # Agrego un valor a la tupla
largo = len(tupla_Aux) # Devuelve la cantidad de valores que tiene la tupla
martu = "Martina" in tupla_Aux # Corrobora que 'Martina' se encuentre en la tupla. Devuelve un booleano

print(f"Tupla1: {tupla1}")
print(f"Tupla_Aux: {tupla_Aux}")
print(f"Largo tupla_Aux: {largo}")
print(f"¿Está 'Martina' en la tupla_Aux?: {martu}")

# DICCIONARIOS

'''
Se basan en una relación key-value, donde la llave (identificador único) contiene el valor
Son mutables: Se puede cambiar el valor que contiene una llave
Una llave puede contener una lista, una tupla u otro diccionario como valor
'''

dic = {
    "Nombre": "Agustín",
    "Apellido": "Malfatto",
    "Edad": 21
}

'''
'Nombre', 'Apellido' y 'Edad' son las llaves del diccionario; 
'Agustín', 'Malfatto' y '21' son los valores
'''

dic["Profesion"] = "Programador" # Agrego una nueva llave con un nuevo valor
dic.pop("Edad") # Elimino la key que paso como parámetro
dic["Profesion"] = "Ingeniero" # Actualizo el valor de una key


print(f"Dic: {dic}")

# SET

'''
Valores únicos: no se pueden repetir 
No son ordenados: No tienen un índice con el cual acceder a los datos
Son mutables: Se pueden modificar los datos guardados
'''

set1 = {"Iphone", "Samsung", "LG", "Motorola"}
set2 = {"Iphone", 24, "Argentina", "LG"}

set_union = set1.union(set2) # Une ambos set en uno, descarta los repetidos
set_interseccion = set1.intersection(set2) # Junta los valores que comparten los dos sets y los guarda en uno nuevo
es_subset = set2.issubset(set1) # Comprueba que si el set 2 es un subset del set 1
set1.add("Huawei") # Agrego un nuevo elemento al set

print(f"La unión de los sets: {set_union}")
print(f"La intersección de los sets: {set_interseccion}")
print(f"¿El set2 es subset del set1?: {es_subset}")
print(f"Añado el 'Huawei' al set1: {set1}")

if "LG" in set1: # Corroboro que 'LG' pertenezca a set1
    set1.remove("LG") # Elimino un elemento del set
    print(f"Remuevo 'LG' del set1: {set1}")


mensaje = "Hola bb mi nombre es banana"

