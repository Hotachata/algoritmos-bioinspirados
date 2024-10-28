# práctica de inteligencia de enjambre
# minimización de la función x^2 + y^2 + [25 * senx + seny]

import random
import math

# cada particula tiene una posición x, y
def random_distancia():
    return [round(random.uniform(-5, 5),2), round(random.uniform(-5, 5),2)]

# camino de una particula
def una_particula_inicial():
    posicion = random_distancia()
    velocidad_actual = 0
    pbest = posicion
    nueva_velocidad = random_distancia()
    fitness = aptitud(posicion)
    # imprimimos los estados iniciales de la particula
    # print("posicion\t\t\t" + "velocidad actual\t" + "pbest\t\t\t\t" + "nueva velocidad\t\t\t")
    # print(str(posicion) + "\t\t\t" + str(velocidad_actual) + "\t\t\t" + str(pbest) + "\t\t\t" + str(nueva_velocidad))
    particula = [posicion, velocidad_actual, pbest, nueva_velocidad, fitness]
    return particula

def aptitud(d):
    x = d[0]
    y = d[1]
    return (round(x**2 + y**2 + (25 * (math.sin(x) + math.sin(y))),2))

def una_nueva_velocidad(velocidad_actual, posicion, pbest, gbest):
    nueva_velocidad=[]
    nueva_velocidad.clear()
    r1 = random.uniform(0, 1)
    r2 = random.uniform(0, 1)
    for i in range(0,2):
        # actualizamos la velocidad
        _ = round((0.8 * velocidad_actual[i]) + (0.7 * r1 * (pbest[i] - posicion[i])) + (1.2 * r2 * (gbest[i] - posicion[i])),2)
        nueva_velocidad.append(_)
    return nueva_velocidad

def una_particula_iteracion(posicion, velocidad_actual, pbest, nueva_velocidad):
    for i in range(10):
        # actualizamos la posicion
        posicion = [round(posicion[0] + nueva_velocidad[0],2), round(posicion[1] + nueva_velocidad[1],2)]
        # actualizamos la velocidad
        velocidad_actual = nueva_velocidad
        # actualizamos el pbest
        if aptitud(posicion) < aptitud(pbest):
            pbest = posicion
        # actualizamos la nueva velocidad
        nueva_velocidad = random_distancia()
        # actualizamos el fitness
        fitness = aptitud(posicion)
        # imprimimos los estados de la particula
        # print(str(posicion) + "\t\t\t" + str(velocidad_actual) + "\t\t" + str(pbest) + "\t\t\t" + str(nueva_velocidad))
        
        iteracion=[posicion, velocidad_actual, pbest, nueva_velocidad, fitness]
        return iteracion

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
        aux.clear()
    return lista_iteraciones

# por 20 partículas
for j in range(0):
    print("\n\n========================================================")
    print("\nparticula " + str(j+1) + "\n")
    # 50 iteraciones
    iteraciones(50)

print(una_nueva_velocidad([1,2], [4,5], [7,8], [10,11]))