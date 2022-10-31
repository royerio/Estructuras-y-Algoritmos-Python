'''
Created on Jan 26, 2021

@author: freddy
'''
## @knitr Item1
#%%

# LA SENTENCIA IF
#====================================================

estudiante = 'John'
boleano = (estudiante == 'John')
print(boleano)

print( estudiante == 'Michael')

# != es el operador de diferente
      
estudiante = 'John'
boleano= estudiante != 'John'
print( estudiante != 'Michael')

# Otros operadores de comparación
      
edad = 20
print( edad < 21 )
print( edad <= 21)
print( edad > 21 )
print( edad >= 21)
print( edad == 22 )
print( edad == 18 )
print( (edad >= 21) and (edad >= 21))

## @knitr Item2
#%%

# Operedor in

alumnos = ['alice', 'david', 'carolina','john','paul']
es_parte_de = 'david' in alumnos
print(es_parte_de)
print(  'carolina' in alumnos)


## @knitr Item3
#%%

edad = 19
if edad >= 18:
    print("Usted puede votar!")

for alumno in alumnos:
    if alumno == 'paul':
        print(alumno.upper())
    else:
        print(alumno.title())

## @knitr Item4
#%%   
alumnos = ['alice', 'david', 'carolina','john','paul']   
for alumno in alumnos:
  if alumno != 'paul':
      print(alumno.upper())
  else:
      print(alumno.title())
      
# Sentencia elif
     
edad = 12
if edad < 4:
    precio = 0
elif edad < 18:
    precio = 5
elif edad < 65:
    precio = 10
else:
    precio = 5
print("El precio de la entrada es $" + str(precio) + ".")
      
## @knitr Item4
#%% 
# Verificar que una lista está vacia

lista = []
if lista:
    print("No está vacía")
else:
    print("La lista está vacía")

lista = ["uno", "dos"]
if lista:
    print("No está vacía")
else:
    print("La lista está vacía")


# Sentencia elif
edad = 12
if edad < 4:
    precio = 0
elif edad < 18:
    precio = 5
elif edad < 65:
    precio = 10
else:
    precio = 5
print("El precio de la entrada es $" + str(precio) + ".")
      
## @knitr Item5
#%%

# Ciclos while, ejemplo de un contador
contador = 1
while contador <= 33:
    print(contador)
    contador += 1
    
## @knitr Item6
#%%
   
# Capturando una condición de salida
mensaje = ["entrada1","entrada2","entrada3","salir"]
indice =0
while mensaje[indice] != 'salir':
    print(mensaje[indice])
    indice+=1
    
## @knitr Item7
#%%
    
# Usando una bandera
mensaje = ["entrada1","entrada2","entrada3","entrada4","entrada5","salir"]
indice =0
activo = True
while activo:
    if mensaje[indice] == 'salir':
        activo = False
    else:
        print(mensaje[indice])
        indice+=1
        
        
## @knitr Item8
#%%
# Usando continue
mensaje = ["inicio","entrada1","entrada2","entrada3","entrada4","entrada5","salir"]
indice =0
activo = True
while activo:
    if mensaje[indice] == 'inicio':
        indice+=1
        continue
    elif mensaje[indice] == 'salir':
        break
    else:
        print(mensaje[indice])
    indice+=1
    
## @knitr Item9
#%%
numero= 150
if numero % 2 == 0:
    print("\nEl número " + str(numero) + " es par.")
else:
    print("\nEl número " + str(numero) + " es impar.")
   
## @knitr Item10
#%%
contenedor = {'color': 'azul', 'distancia': 5}
print(contenedor['color'])
print(contenedor['distancia'])
print(contenedor)

## @knitr Item11
#%%

contenedor={"color":"azul","distancia":5,"edad":20}
print(contenedor)

## @knitr Item12
#%%
# Un diccionario vacío
contenedor = {}
contenedor['color']='rojo'
contenedor['distancia']=2
contenedor['planeta'] = 'tierra'
contenedor['edad'] = 23
contenedor

## @knitr Item13
#%%
# Un diccionario vacío
contenedor['planeta'] = 'marte'
contenedor

## @knitr Item14
#%%
# Un diccionario vacío
if contenedor['edad'] >= 23:
    contenedor['planeta'] = 'jupiter'
    
print(contenedor)

## @knitr Item15
#%%

usuario = {
  'nombre_usuario': 'jose',
  'nombre': 'José',
  'apellido': 'Rojas',
}

print(usuario.items())

for key, value in usuario.items():
    print("\nLlave: " + key)
    print("Valor: " + value)
    
print(usuario.keys())

print(usuario.values())    
  
## @knitr Item16
#%%    
programadores={"juan":"Java","jose":"Python","eduardo":"C++","juan_carlos":"Python","carla":"R","monica":"Ruby"} 

#Ordena por lenguaje
for lenguaje in sorted(programadores.values()):
    print(lenguaje)

#Ordena por usuario
for lenguaje in sorted(programadores.keys()):
    print(lenguaje)
    
## @knitr Item17
#%%
# Listas dentro de un diccionario
   
programadores_avanzados = {
  'juan': ['Java','python','C++'],
  'jose': ['Python',"C++"],
  'eduardo': ['C++','Java'],
  'juan_carlos': ['Python','C','Pascal'],
  'carla': ["R","Python"],
  "monica": ["Ruby,C++"]
}
    
#Ordena por lenguaje
for lenguaje in sorted(programadores_avanzados.values()):
    print(lenguaje)

#Ordena por usuario
for lenguaje in sorted(programadores_avanzados.keys()):
    print(lenguaje)
    
## @knitr Item18
#%%   
usuarios = {
  'mcespedes': {
     'nombre': 'maría',
     'apellido': 'céspedes',
     'lugar': 'alajuela',
   },
   'malfaro': {
     'nombre': 'mario',
     'apellido': 'alfaro',
     'lugar': 'heredia',
   },
   'jrojas': {
     'nombre': 'julián',
     'apellido': 'rojas',
     'lugar': 'curridabat',
   },
}

for usuario, info_usuario in usuarios.items():
    print("\nNombre de usuario: " + usuario)
    nombre_completo = info_usuario['nombre'] + " " + info_usuario['apellido'] 
    lugar = info_usuario['lugar']
    print("\tNombre Completo: " + nombre_completo.title())
    print("\tLugar: " + lugar.title())
    
