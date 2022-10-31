'''
Created on Jan 23, 2021

@author: freddy
'''
## @knitr Item1
#%%

# FUNCIONES:

# def nombre_funcion(parametro_0, ... , parametro_n):
#    Desarrollo de la función tabulado.
#    return valor  
    
# Función suma(x,y)
    
# Se define la función
def suma(x,y):
  z = x + y
  return z

# Se hace el llamado a la función
res = suma(30,12)
print(res)

## @knitr Item2
#%%

# Definición de la función imprime_informacion.

def imprime_informacion(usuario):
  print("Contenido de informacion de usuario: " + usuario.title() + "!")
 
# Invocación
imprime_informacion('jose')
imprime_informacion('eduardo')

## @knitr Item3
#%%
# Definición de una función con parámetros estatícos. No tienen valor por omision y deben aporarse ambos siempre.
def area_triangulo_estatica(base,altura):
  area = (base*altura)/2
  return(area)

# Invocación
print(area_triangulo_estatica(3,4))

print(area_triangulo_estatica(base=10, altura=15))

print(area_triangulo_estatica(altura=15, base=10))

## @knitr Item4
#%%
# Valores por defecto en parámetros

def area_triangulo(base=1,altura=1):
  area = (base*altura)/2
  return(area)

# Invocación
print(area_triangulo(30,15))

# Usa los valores por defecto
print(area_triangulo(30))
print("++++++++++++++++\n")

print(area_triangulo())
print("++++++++++++++++\n")


## @knitr Item5
#%%
# Retornando conjuntos con valores
# Retornando un diccionario (Similar a R que se retorna una lista)
def nombre_completo_(nombre, apellido):
  persona = {'Nombre': nombre, 'Apellido': apellido}
  return persona

usuario = nombre_completo_('Juan Mora', 'Fernández')
print(usuario)

def nombre_completo(nombre, apellido, edad=''):
  persona = {'Nombre': nombre, 'Apellido': apellido}
  if edad:
    persona['Edad'] = edad
  return persona

usuario = nombre_completo('Juan Mora', 'Fernández')
print(usuario)

usuario = nombre_completo('Juan Mora', 'Fernández',edad=50)
print(usuario)

## @knitr Item6
#%%
def conformacion_lista_impares(datos_impares=0):
  lista=[]
  for i in range(0,datos_impares+1):
    if i % 2 !=0:
      lista.append(i)
  return lista

lista_impares=conformacion_lista_impares(151)
print(lista_impares)

## @knitr Item7
#%%

# Ejemplo con if: El mayor entre 3 números
def mayor(A, B, C):
  if (A > B) and (A > C):
    return(A)
  elif (B > A) and (B > C):
    return(B)
  else:
    return(C)	

mayor(9,0,2)

## @knitr Item8
#%%
# Ejemplo con for
# construye un vector “v” 
# tal que en la entrada k sea una serie dada porr k^2−4.
#  v[k]=k^2−4:    
def cvector_f(n):
  # Inicializa un vector con n ceros
  v = []
  for k in range(n):
    v.append(0) 
  for k in range(n):
    v[k]=k**2 - 4
  return(v)

cvector_f(9)
cvector_f(35)

## @knitr Item9
#%%
# Otro Ejemplo con for: Norma de un vector
def norma1(v):
  suma = 0
  for i in range(len(v)):
    suma = suma + abs(v[i])
  return suma

vec0=(4,-7,2,1)
print(norma1(vec0))

v=(-1, 20, 38, -4, 51, -6, -7, 82, 91, 20)
print(norma1(v))


## @knitr Item10
#%%
# Ejemplo
# La siguiente función multiplica una matriz por un vector.
# Se calcula y=Ax
# : A es una matriz de tamaño m×n,
# : x es un vector (matriz de n×1) y 
# : El resulado es otro vector (matriz de m×1).

def mat_x_vec(A,x):
  n = len(A) # Número de filas
  m = len(A[0])  # Número de columnas
  y = []      # Crea el vector columana y
  for i in range(n):
    y.append(0)
  for j in range(m):
    for i in range(n):
      y[i] = y[i] + A[i][j]*x[j]
  return(y)

A = [[5,2,-3],[1,3,0],[-15,4,18],[2,-3,5]] # 4 x 3
print(A)

x = [3,-4,0] # 3 x 1
print(x)

y = mat_x_vec(A,x) 
print(y)

## @knitr Item11
#%%

# Ejemplo
# La siguiente función multiplica una matriz por un vector.
# Se calcula y=Ax
# : A es una matriz de tamaño m×n,
# : x es un vector (matriz de n×1) y 
# : El resulado es otro vector (matriz de m×1).
# : NOTA se usa la biblioteca: numpy

import numpy as np # Carga el paquete

# Cálculo del producto.
def mat_x_vec2(A,x):
  n = np.shape(A)[0] # Número de filas
  m = np.shape(A)[1]  # Número de columnas
  y = np.zeros((n,1), float)        # Crea el vector columana y
  for j in range(m):
    for i in range(n):
      y[i] = y[i] + A[i,j]*x[j]
  return(y)
## @knitr Item12
#%%

#Construcción de solución
# Matriz
A = np.matrix([[4,1,-3],[2,4.4,0],[-5,9,198],[2,4,-5]])
print(A)
np.shape(A)[0]
np.shape(A)[1]

# Vector
x = np.matrix([[2],[-1],[0]]) # 3 x 1
print(x)
np.shape(x)[0]
np.shape(x)[1]

#Evaluación
y = mat_x_vec2(A,x) 
print(y)

## @knitr Item13
#%%

def ordenamientoBurbuja(unaListaOriginal):
    unaLista=unaListaOriginal.copy()
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
    return unaLista

## @knitr Item14
#%%
unaLista = [54,26,93,17,77,31,44,55,20]
unaListaOrdenada=ordenamientoBurbuja(unaLista)
print(unaLista)

## @knitr Item15
#%%

# Definición de funciones para ordenamiento rápido de un vector de datos.

def quicksort(arreglo, izquierda, derecha):
    '''
    Se utiliza en forma recursiva haciendo particiones de los datos de entrada.
    '''
    if izquierda < derecha:
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort(arreglo, izquierda, indiceParticion)
        quicksort(arreglo, indiceParticion + 1, derecha)


def particion(arreglo, izquierda, derecha):
    '''
    Se hace la partición por cada caso que se invoca "quicksort"
    '''
    pivote = arreglo[izquierda]
    while True:
        # Mientras cada elemento desde la izquierda esté en orden (sea menor que el
        # pivote) continúa avanzando el índice
        while arreglo[izquierda] < pivote:
            izquierda += 1

        # Mientras cada elemento desde la derecha esté en orden (sea mayor que el
        # pivote) continúa disminuyendo el índice
        while arreglo[derecha] > pivote:
            derecha -= 1

        """
            Si la izquierda es mayor o igual que la derecha significa que no
            necesitamos hacer ningún intercambio
            de variables, pues los elementos ya están en orden (al menos en esta
            iteración)
        """
        if izquierda >= derecha:
            # Indicar "en dónde nos quedamos" para poder dividir el arreglo de nuevo
            # y ordenar los demás elementos
            return derecha
        else:
            # Nota: yo sé que el else no hace falta por el return de arriba, pero así el algoritmo es más claro
            """
                Si las variables quedaron "lejos" (es decir, la izquierda no superó ni
                alcanzó a la derecha)
                significa que se detuvieron porque encontraron un valor que no estaba
                en orden, así que lo intercambiamos
            """
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
            """
                Ya intercambiamos, pero seguimos avanzando los índices
            """
            izquierda += 1
            derecha -= 1


## @knitr Item16
#%%
arreglo = [5, 1, 2, 1, 1, 3, 5, 1, 5, 1, 99, 231, 234, 12, 121,
           312, 123, 123, 12, 312, 321, 312, 31, 23, 12, 3123, 123, ]
print("Antes de ordenarlo: ")
print(arreglo)
quicksort(arreglo, 0, len(arreglo) - 1)
print("Después de ordenarlo: ")
print(arreglo)

## @knitr Item17
#%%
# Se construye la serie mediante la utilización de datos en parejas, una de las capacidades de Python.
def fibonacci(n):
    '''
    Serie de Fibonacci
    '''
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
## @knitr Item18
#%%
fibonacci(5)
fibonacci(100)

## @knitr Item19
#%%
def Fibonacci(n):
  '''
  Serie de Fibonacci
  '''
  result=[] 
  a, b = 0,1
  while a < n:
      result.append(a)
      a, b = b, a+b
  return result

serie=Fibonacci(5)
print(serie)

serie1=Fibonacci(100)
print(serie1)
