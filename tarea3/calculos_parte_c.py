# TAREA#3 - ROYER MÉNDEZ RAMÍREZ
# EJERCICIO#1. PARTE C

lista1 = [13, 2, 104, 36, 9, 120, 29, 500, 89, 41, 65, 7]
diccionario = {0:20, 1:320, 2:90, 3:147, 4:122, 5:717, 6:2, 7:77, 8:112, 9:14, 10:17, 11:24}

lista1_copia = lista1 [:]
diccionario_copia = diccionario.copy()


def diccionario_nuevo(diccionario_copia, lista1_copia):
    
    nuevo_diccionario = dict(zip(diccionario_copia, lista1_copia))
    
    return nuevo_diccionario

#Llamado a la funcion


diccionario_nuevo = diccionario_nuevo(diccionario_copia.keys(), lista1_copia)

print(diccionario_nuevo)




'''
def diccionario_nuevo(lista1_copia, diccionario_copia):
    
    diccionario_nuevo = {}
    for key in diccionario_copia.keys(key):
        diccionario_nuevo.keys.append(key)
    
    for value in lista1_copia:
        diccionario_nuevo.values.append(value)
    
    return diccionario_nuevo

print (diccionario_nuevo)
'''