# TAREA#3 - ROYER MÉNDEZ RAMÍREZ
# EJERCICIO#1. PARTE A

#Se crea la función
def calculos(lista1, diccionario):


    lista_de_salida = [] # Se crea una lista vacia
    
    for elemento in (lista1):
        lista_de_salida.append(elemento) #Se agregan los elementos de la lista a la lista vacía
        
    for value in diccionario.values():
            lista_de_salida.append(value) #Se agregan los elementos de los valores del diccionario a la lista vacía
    
    lista_de_salida.sort() #Se ordena en orden ascendente de sus elementos
    
    return lista_de_salida


#El llamado a la función

lista1 = [13, 2, 104, 36, 9, 120, 29, 500, 89, 41, 65, 7]
diccionario = {0:20, 1:320, 2:90, 3:147, 4:122, 5:717, 6:2, 7:77, 8:112, 9:14, 10:17, 11:24}

lista = calculos(lista1, diccionario)

print(lista)
