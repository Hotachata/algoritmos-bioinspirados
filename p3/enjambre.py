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

def una_particula():
    posicion_inicial = random_distancia()
    velocidad_actual = 0
    pbest = posicion_inicial
    nueva_velocidad = random_distancia()
    return print(str(posicion_inicial) + "\t\t" + str(velocidad_actual) + "\t\t\t" + str(pbest) + "\t" + str(nueva_velocidad))

# 2. inicialización aleatoria de posiciones y velocidades

print("posicion inicial\t" + "velocidad actual\t" + "pbest\t\t" + "nueva velocidad\t")
una_particula()