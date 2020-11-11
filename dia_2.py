#Fabricando una baraja

# Importamos las funciones from=desde import *=todas
from funcionesBaraja import *

# Creamos las listas que se usarán para crear y mezclar la baraja
palos=['o','c','e','b']
numerosPalos=['A','2','3','4','5','6','7','S','C','R']


baraja=(creacionBaraja(palos,numerosPalos))

#Comprobamos que funciona con los print
print(len(baraja)) # len cuanta el número de items
print(baraja) # muestra la baraja
print((MezclarBaraja(baraja))) # muestra la baraja mezclada