# práctica de inteligencia de enjambre
# minimización de la función x^2 + y^2 + [25 * senx + seny]

import random

# 1. crear un enjambre de 20 particulas
#   cada particula tiene una posición x, y
def random_distancia():
    return [round(random.uniform(-5, 5),2), round(random.uniform(-5, 5),2)]

#   generamos la lista de particulas
def genera_distancias_enjambre():
    enjambre = []
    for i in range(20):
        enjambre.append(random_distancia())
    return enjambre

posicion = 0
velocidad_actual = 0
pbest = 0
nueva_velocidad = 0

# camino de una particula
def una_particula_inicial():
    posicion = random_distancia()
    velocidad_actual = 0
    pbest = posicion
    nueva_velocidad = random_distancia()
    
    # imprimimos los estados iniciales de la particula
    # print("posicion\t\t\t" + "velocidad actual\t" + "pbest\t\t\t\t" + "nueva velocidad\t\t\t")
    # print(str(posicion) + "\t\t\t" + str(velocidad_actual) + "\t\t\t" + str(pbest) + "\t\t\t" + str(nueva_velocidad))
    
    particula = [posicion, velocidad_actual, pbest, nueva_velocidad]
    return particula

def una_particula_iteracion(posicion, velocidad_actual, pbest, nueva_velocidad):
    for i in range(10):
        # actualizamos la posicion
        posicion = [round(posicion[0] + nueva_velocidad[0],2), round(posicion[1] + nueva_velocidad[1],2)]
        # actualizamos la velocidad
        velocidad_actual = nueva_velocidad
        # actualizamos el pbest
        
        # actualizamos la nueva velocidad
        nueva_velocidad = random_distancia()
        
        # imprimimos los estados de la particula
        # print(str(posicion) + "\t\t\t" + str(velocidad_actual) + "\t\t" + str(pbest) + "\t\t\t" + str(nueva_velocidad))
        
        iteracion=[posicion, velocidad_actual, pbest, nueva_velocidad]
        return iteracion

# 2. inicialización aleatoria de posiciones y velocidades

def iteraciones(num_iteraciones):
    # creamos una particula
    p=una_particula_inicial()
    print(str(p))
    lista_iteraciones=[]
    lista_iteraciones.append(p)
    for i in range(num_iteraciones):
        aux=una_particula_iteracion(p[0], p[1], p[2], p[3])
        lista_iteraciones.append(aux)
        p[0]=aux[0]
        p[1]=aux[1]
        p[2]=aux[2]
        p[3]=aux[3]
        print(str(aux))
    return lista_iteraciones

iteraciones(20)