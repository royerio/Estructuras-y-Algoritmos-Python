# TAREA#3 - ROYER MÉNDEZ RAMÍREZ
# EJERCICIO#1. PARTE B

import numpy as np

lista1 = [13, 2, 104, 36, 9, 120, 29, 500, 89, 41, 65, 7]
lista1.sort()   #Se ordena la lista en orden ascendente de sus elementos


diccionario = {0:20, 1:320, 2:90, 3:147, 4:122, 5:717, 6:2, 7:77, 8:112, 9:14, 10:17, 11:24}

valores_diccionario = [] #Decidí crear una lista con los valores del diccionario

for valor in diccionario.values():
    valores_diccionario.append(valor)
    
valores_diccionario.sort()  #Se ordena en orden ascendente de sus elementos


def calculos_estadisticos (lista1, valores_diccionario):

    #Media y desviacion estandar para la lista y el diccionario, respectivamente
    media_lista = np.mean(lista1)
    desviacion_estandar_lista = np.std(lista1)
    media_diccionario = np.mean(valores_diccionario)
    desviacion_estandar_diccionario = np.std(valores_diccionario)
    

    ###CALCULOS PARA OBTENER LA MEDIANA DE LA LISTA MANUALMENTE###
    contador = 0

    for i in range (0, len(lista1)):
        contador += 1

    numero_total_elementos = contador  #son 12 elementos

    elemento_izq = (numero_total_elementos/2)-1 #elemento 05 de la lista
    elemento_der = (numero_total_elementos/2) #elemento 06 de la lista

    valor_izq = lista1[int(elemento_izq)]   #El valor que esta contenido en el elemento 05 de la lista (36)
    valor_der = lista1[int(elemento_der)]   #El valor que esta contenido en el elemento 06 de la lista (41)

    mediana_lista = (valor_izq + valor_der)/2
    
    ###CALCULOS PARA OBTENER LA MEDIANA DEL DICCIONARIO MANUALMENTE###
    contador = 0

    for i in range (0, len(valores_diccionario)):
        contador += 1

    numero_total_elementos = contador  #son 12 elementos

    elemento_izq = (numero_total_elementos/2)-1 #elemento 05 de la lista
    elemento_der = (numero_total_elementos/2) #elemento 06 de la lista

    valor_izq = valores_diccionario[int(elemento_izq)]   #El valor que esta contenido en el elemento 05 de la lista (77)
    valor_der = valores_diccionario[int(elemento_der)]   #El valor que esta contenido en el elemento 06 de la lista (90)

    mediana_diccionario = (valor_izq + valor_der)/2

    return media_lista, desviacion_estandar_lista, mediana_lista, media_diccionario, desviacion_estandar_diccionario, mediana_diccionario


    #Llamado a la funcion

valores_estadisticos = calculos_estadisticos(lista1, valores_diccionario)

print("\nLos valores estadisticos de la lista1 son: \n\t Media: ",valores_estadisticos[0], "\n\t Desviación estandar: ",valores_estadisticos[1], "\n\t Mediana: ",valores_estadisticos[2], "\n\nLos valores estadisticos del diccionario son: \n\t Media: ",valores_estadisticos[3], "\n\t Desviación estandar: ",valores_estadisticos[4], "\n\t Mediana: ",valores_estadisticos[5])



###MANERA FACIL PARA OBTENER LA MEDIANA DE LA LISTA1 Y DE LOS VALORES DEL DICCIONARIO###

mediana_lista_prueba = np.median(lista1)
mediana_diccionario_prueba = np.median(valores_diccionario)

#print(mediana_lista_prueba, mediana_diccionario_prueba)  #son los mismos valores de arriba