# importamos la funcion random
import random

# Creamos la baraja añadindo elementos de ambas listas en una sola
# Atención !!!! la primera vez lo hice con listas dentro de una lista pero resultaba demasiado complicado después mezclarla.
def creacionBaraja(palos,numeroPalos):
    baraja=[]
    for numeros in numeroPalos:
        for tipos in palos:
            baraja.append(numeros+tipos)
    return baraja


# Sangre sudor y lagrimas me ha costado esta puñetera función para mezclar.
# Actua de la siguiente forma:
    # - cuenta la unidades de la baraja mezclada, si hay menos de 40 sigue adelante
    # - escoge un valor al azar
    # - comprueba si ese valor esta en la baraja mezclada
    #     - si NO está : lo añade
    #     - Después elimina de la baraja original el elemento para evitar BUCLE INFINITO ( ya que como la posición es aleatoria podría repetirse infinifad de veces)
def MezclarBaraja(baraja):
    barajaMezclada=[]
    while len(barajaMezclada)<40: # la condición también podría ser cuando la lista original llegue a 0
        for random.choice in baraja:
            if random.choice not in barajaMezclada:
                barajaMezclada.append(random.choice)
                baraja.remove(random.choice)
    return barajaMezclada