# TAREA#3 - ROYER MÉNDEZ RAMÍREZ
# EJERCICIO#1. PARTE B


import numpy as np
import calculos_parte_a #Para importar la lista obtenida de la seccion A.


lista_casob = calculos_parte_a.lista #Lista_casob: lista del caso A. Contiene los datos de "lista1" + valores de "diccionario"

def calculos_estadisticos (lista_casob):

    
    #Media y desviacion estandar para la lista y el diccionario
    
    media = np.mean(lista_casob)
    desviacion_estandar = np.std(lista_casob)


    #Calculos para obtener la mediana manualmente.

    contador = 0
    for i in range (0, len(lista_casob)):
        contador += 1

    numero_total_elementos = contador  #son 24 elementos


    elemento_izq = (numero_total_elementos/2)-1 #elemento 12 de la lista
    elemento_der = (numero_total_elementos/2) #elemento 13 de la lista


    valor_izq = lista_casob[int(elemento_izq)]   #El valor que esta contenido en el elemento 12 de la lista (41)
    valor_der = lista_casob[int(elemento_der)]   #El valor que esta contenido en el elemento 13 de la lista (65)


    mediana = (valor_izq + valor_der)/2

    return media, desviacion_estandar, mediana

    #Llamado a la funcion

valores_estadisticos = calculos_estadisticos(lista_casob)

print("Los valores de la media, desviación estandar y mediana respectivamente son: ",valores_estadisticos)


############################################


#Manera facil para obtener la mediana:
mediana_prueba = np.median(lista_casob)
print(mediana_prueba)