import numpy as np 
import matplotlib.pyplot as plt
import math

'''
Ejemplo 1:
En este codigo se tiene que obtener el valor de e^o,5 con una serie de Mclaurin
'''
#definimos los valores de n, en este caso de 1 a 100

iteraciones = np.linspace(1,100,100)

#Como la serie es: (x^n)/n! vamos a hacer un ciclo for para recorrer los 100 elementos de n y asi poder aproximar el resultado
E = 1

for n in np.linspace(1,100,100):
    
    E = E + ((1/2)**n)/(math.factorial(int(n)))

plt.plot(iteraciones, E)
plt.show()
