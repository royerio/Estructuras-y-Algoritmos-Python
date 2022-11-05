# TAREA#3 - ROYER MÉNDEZ RAMÍREZ
# EJERCICIO #2

from audioop import reverse
import pandas as pd
from numpy import mean, std

datos = {'Nombre': ["Marco", "Francisco", "Roberto", "Mariel", "Sonia", "John", "Charles"],
         'Carrera':["Ing. Eléctrica", "Educación Física", "Matemáticas", "Ing. Mecánica", "Derecho", "Idiomas", "Ing. Civil"],
         'Edad':["21", "20", "19", "29", "22", "21", "22"]}

#Parte 2.A -- Agregar los indices a la Tabla de Datos
tabla = pd.DataFrame(datos, index = ["Est 1", "Est 2", "Est 3", "Est 4", "Est 5", "Est 6", "Est 7"])


#Parte 2.B -- Imprimir la Tabla de Datos

print (tabla)

#Parte 2.C -- Imprimir por "Nombre" ascendente
tabla.sort_values(by=['Nombre'])
print (tabla.sort_values(by=['Nombre']))

#Parte 2.D -- Imprimir por "Carrera" descendente
tabla.sort_values(by=['Carrera'], ascending=False)
print (tabla.sort_values(by=['Carrera'], ascending=False))

#Parte 2.E -- Visualizacion por medio de indice binario (iloc) de los 4 primeros estudiantes

print(tabla.iloc[0:4,:])


#Parte 2.F -- Visualizacion por medio de indice textual (loc) de estudiantes a partir de la 2da entrada

print(tabla.loc['Est 2':,:])


#Parte 2.G -- Para estudiantes de las posiciones binarias 3,4,5 mostrar datos de carrera y edad

print(tabla.iloc[3:6,1:3])

#Parte 2.H -- Convertir y exportar la tabla a un archivo excel.

tabla.to_excel('Tabla_Estudiantes.xlsx')