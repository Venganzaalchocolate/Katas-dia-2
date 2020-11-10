#Fabricando una baraja
import random

#o=oros, c=copas, e=espadas y b=bastos

def creacionBaraja(palos,numeroPalos):
    baraja=[]
    for tipos in palos:
        for x in numerosPalos:
            baraja.append((tipos,x))
    return baraja

palos=['o','c','e','b']
numerosPalos=['A','2','3','4','5','6','7','S','C','R']

baraja=(creacionBaraja(palos,numerosPalos))

def barajarBaraja(baraja):
    barajaMezclada=[]
    barajaMezclada.append(random.choice(baraja))
    while len(baraja) != len(barajaMezclada):
        for cartas in baraja:
            if cartas in not barajaMezclada:
                barajaMezclada.append(random.choice(baraja))
    return barajaMezclada
        

print(len(baraja))
print(barajarBaraja(baraja))
print(len(barajarBaraja(baraja)))
