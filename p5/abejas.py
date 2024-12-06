import random

# lim superior (lsup) e inferior (linf), respetando los limites de 3 Love Potions y 2 Skiving Snackbox
lsup=10
linf=0
linf_lp = 3
linf_ss = 2
iteraciones = 50 # limite de iteraciones
lim = 5 # limite de evaluaciones
nobreras = 5 # numero de obreras

# población inicial aleatoria
def poblacion_inicial(linf, lsup):
    return round((linf + random.uniform(0,1) * (lsup - linf)),1)

# inicializamos las abejas
def inicializa_abejas():
    abejas = []
    for i in range(0, len(nobreras)): # 20 abejas
        aux = []
        # cada variable es una solución, son siete soluciones
        aux.append(poblacion_inicial(linf, lsup)) # sol 1
        aux.append(poblacion_inicial(linf_lp, lsup)) # sol 2
        aux.append(poblacion_inicial(linf_ss, lsup)) # sol 3
        for j in range(4):
            aux.append(poblacion_inicial(linf, lsup)) # sol 4-7
        abejas.append(aux)
        print(aux)
    return abejas

def aptitud():
    pass

def fase_obrera():
    abejas = inicializa_abejas() # inicializamos la colonia de abejas (20)
    for i in range(0, len(abejas)):
        x = abejas[i] # extraemos la abeja con la que vamos a trabajar
        abeja_random = random.uniform(0,len(abejas)) # numero de la abeja aleatoria
        k = abejas[abeja_random] # abeja aleatoria
        
        # por cada abeja seleccionamos una fuente de alimento
        j = random.uniform(0,6) # número aleatorio para modificar (posición)
        vmodif = x[j] + random.uniform(-1,1) * (x[j] - k[j]) # variable modificada
        
        aux = x
        aux[j] = vmodif # actualizamos la variable modificada en un auxiliar
