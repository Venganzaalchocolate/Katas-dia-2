#Fabricando una baraja

#o=oros, c=copas, e=espadas y b=bastos
palos=['o','c','e','b']
numerosPalos=['A','2','3','4','5','6','7','S','C','R']
baraja={}

for tipo in palos:
    for numero in numerosPalos:
        baraja[tipo]=numero

print(baraja)
    