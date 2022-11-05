#TAREA #3 ROYER MÉNDEZ RAMÍREZ
#PARTE #3

#Sección a 
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

archivo = 'time_series_covid19_confirmed_ready.csv'

#Se crea la funcion
def CargarArchivo(archivo):
    
    variable = pd.read_csv(archivo)
            
    return variable
    
    
#Llamado a la funcion

datos = CargarArchivo(archivo)

##################################################

#Sección b 
# %%

datos['fechas'] = pd.to_datetime(datos['fechas'], format='%Y/%m/%d')
datos.dtypes

def ChangeIndex(datos):
    
    nueva_tabla = datos.set_index('fechas')

    return nueva_tabla

#Se realiza el llamado a la función
datos2 = ChangeIndex(datos)
print(datos2)
datos2.dtypes
##################################################

#Sección c
# %%

print(datos2.loc['2020-09-01':'2020-09-25',['Panama', 'Uruguay', 'Costa.Rica']])

##################################################

#Sección d
# %%

plt.plot(datos['Costa.Rica'], label="Costa Rica")
plt.legend(loc="upper left")
plt.xlabel('# de Día')
plt.ylabel('Cantidad de casos')
plt.show()
##################################################

#Sección e
# %%

datos2.iloc[222:247,[162,85,62]] #Se efectua la seleccion de las celdas solicitadas en el enunciado
datos3 = datos2.iloc[222:247,[162,85,62]] # Este DF contiene los paises España, Italia y Francia
plt.plot(datos3['Spain'], '-p', color='blue', label='España')
plt.plot(datos3['Italy'], '-p', color='gray', label='Italia')
plt.plot(datos3['France'], '-p', color='orange', label='Francia')
plt.legend(loc="upper left")
plt.xlabel('Fecha')
plt.ylabel('Cantidad de casos')
plt.show()

# %%
