import random

# lim superior (lsup) e inferior (linf), respetando los limites de 3 Love Potions y 2 Skiving Snackbox
lsup=10
linf=0
linf_lp = 3
linf_ss = 2
lim = 50 # limite de iteraciones

# población inicial aleatoria
def poblacion_inicial(linf, lsup):
    return round((linf + random.uniform(0,1) * (lsup - linf)),1)

# inicializamos las abejas
def inicializa_abejas():
    abejas = []
    for i in range(0, 5): # 20 abejas
        aux = []
        # son siete soluciones
        aux.append(poblacion_inicial(linf, lsup)) # sol 1
        aux.append(poblacion_inicial(linf_lp, lsup)) # sol 2
        aux.append(poblacion_inicial(linf_ss, lsup)) # sol 3
        for j in range(4):
            aux.append(poblacion_inicial(linf, lsup)) # sol 4-7
        abejas.append(aux)
        print(aux)
    return abejas

inicializa_abejas()