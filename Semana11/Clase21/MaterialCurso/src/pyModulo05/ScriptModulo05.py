'''
Created on Jan 27, 2021

@author: freddy
'''
## @knitr Item1
#%%
import matplotlib.pyplot as plt
import numpy as np

#import seaborn 

plt.style.use('classic') # Estilo clásico

# Ejemplos de gráficos de líneas (graficando funciones)
# Datos del eje X para los siguientes gráficos
x = np.linspace(0, 10, 100)
x

# Lo siguiente se ejecuta todo junto
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()
plt.close()

## @knitr Item2
#%%
plt.plot(x, np.sin(x), '-*')
plt.plot(x, np.cos(x), '--');
plt.show()
plt.close()


## @knitr Item3
#%%
# Crea el primer panel
plt.subplot(2, 1, 1) # (filas, columnas, número de paneles)
plt.plot(x, np.sin(x))
# crea el segundo panel
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.show()
plt.close()

## @knitr Item4
#%%
# Un estilo Orientado a Objetos para situaciones más complejas
# Crea la figura y ax un arreglo de dos objectos
fig, ax = plt.subplots(2)
# Llama el método plot() method 
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()
plt.close()

## @knitr Item5
#%%

# Otro ejemplo Orientado a Objetos
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
plt.show()
plt.close()

## @knitr Item6
#%%
# Estilo funcional
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.show()
plt.close()

## @knitr Item7
#%%
# Usando colores
plt.plot(x, np.sin(x - 0), color='blue')        # Nombre del color
plt.plot(x, np.sin(x - 1), color='g')           # Código del color (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # escala de gris entre 0 y 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Código exadecimal (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # Tupla RGB entre 0 y 1
plt.plot(x, np.sin(x - 5), color='chartreuse') # Nombres de color en HTML
plt.show()
plt.close()

## @knitr Item8
#%%
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted')
plt.show()
plt.close()

## @knitr Item9
#%%
# Lo mismo pero con código
plt.plot(x, x + 4, linestyle='-')  
plt.plot(x, x + 5, linestyle='--') 
plt.plot(x, x + 6, linestyle='-.') 
plt.plot(x, x + 7, linestyle=':') 
plt.show()
plt.close()

## @knitr Item10
#%%
# Cambiando los límites de los ejes
# Evaluar todo junto
plt.plot(x, np.sin(x))
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)
plt.show()
plt.close()

## @knitr Item11
#%%
# Otro ejemplo
plt.plot(x, np.sin(x))
plt.axis('tight')
plt.show()

## @knitr Item12
#%%
# Títulos
plt.plot(x, np.sin(x))
plt.title("Función Seno(x)")
plt.xlabel("x")
plt.ylabel("Seno(x)") 
plt.show()

## @knitr Item13
#%%
# Leyendas
plt.plot(x, np.sin(x), '-g', label='Seno(x)')
plt.plot(x, np.cos(x), ':b', label='Coseno(x)')
plt.axis('equal')
plt.legend()
plt.show()

## @knitr Item14
#%%
# Orientado a Objetos
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='Seno(x)',
       title='Un ploteo de Seno(x)')
plt.show()

## @knitr Item15
#%%
# Gráficos scatter plot = Ejes XY
# Comando plot

# Ejemplo 1
x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.plot(x, y, 'o', color='black')
plt.show()

## @knitr Item16
#%%

# Ejemplo 2
rng = np.random.RandomState(0)
for marca in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marca,
             label="marca='{0}'".format(marca))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)
plt.show()

## @knitr Item17
#%%
# Ejemplo 3
plt.plot(x, y, '-ok')
plt.show()

## @knitr Item18
#%%
# Ejemplo 4
plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2)

plt.show()
plt.close()

## @knitr Item19
#%%
# Comando scatter, más potente

# Ejemplo 5
plt.scatter(x, y, marker='o')
plt.show()
plt.close()

## @knitr Item20
#%%
# Ejemplo 6

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colores = rng.rand(100)
tamanos = 1000 * rng.rand(100)
x=plt.scatter(x, y, c=colores, s=tamanos, alpha=0.3,cmap='viridis')
x=plt.colorbar() 
plt.show()
plt.close()

## @knitr Item21
#%%
### INSTALAR pip3 sklearn

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
print("Nombres de variables:",iris.target_names)
print("Nombres de mediciones para cada variable:",iris.feature_names)

# Convertir IRIS a Data Frame para observar componentes.
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print("Datos iniciales de IRIS vistos en un dataframe: ",df.head(10))

caracteristicas = iris.data.T
#df1 = pd.DataFrame(caracteristicas, columns=caracteristicas.feature_names)

#print("Datos iniciales de IRIS vistos en un dataframe: ",df1.head(10))

#Ahora se grafica datos de la transpuesta.
plt.scatter(caracteristicas[0], caracteristicas[1], 
            alpha=0.2,s=100*caracteristicas[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()

## @knitr Item22
#%%

# Plotenadola variación del error (por ejemplo en Validación Cruzada)
plt.style.use('seaborn-whitegrid') # Define el estilo del gráfico

x = np.linspace(0, 10, 100)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(100)
plt.errorbar(x, y, yerr=dy, fmt='.k')
# fmt es un código de formato que controla la apariencia de líneas y puntos

plt.show()

## @knitr Item23
#%%
# Ploteando Histogramas y Densidad
# Ejemplo 1
plt.style.use('seaborn-white')
datos = np.random.randn(1000)
plt.hist(datos)
plt.show()


## @knitr Item24
#%%
from plotnine.data import economics
from plotnine.data import mpg
from plotnine.data import huron

from plotnine import ggplot, aes, geom_line,geom_point,geom_bar,stat_bin,geom_boxplot

x=(ggplot(economics) + 
  aes(x="date", y="pop") + 
  geom_line() 
)
print(x)
ggplot(mpg) + aes(x="class", y="hwy") + geom_point()

ggplot(mpg) + aes(x="class") + geom_bar()

ggplot(huron) + aes(x="level") + stat_bin(bins=10) + geom_bar()

ggplot(huron)  + aes(x="factor(decade)", y="level")  + geom_boxplot()
  
#%%
