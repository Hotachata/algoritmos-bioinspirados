
# CREAMOS una funcion de evaluacion
def funcion_evaluacion(individuo):
    return sum(individuo)

# CREAMOS una funcion de seleccion
def seleccion(individuos):
    # Ordenamos los individuos por su funcion de evaluacion
    individuos.sort(key=funcion_evaluacion, reverse=True)
    # Seleccionamos los 10 individuos con mejor evaluacion
    return individuos[:10]
# CREAMOS una funcion de cruce
def cruce(individuo1, individuo2):
    # Cruzamos los individuos en un punto aleatorio
    punto_cruce = random.randint(1, len(individuo1)-1)
    hijo1 = individuo1[:punto_cruce] + individuo2[punto_cruce:]
    hijo2 = individuo2[:punto_cruce] + individuo1[punto_cruce:]
    return hijo1, hijo2

# CREAMOS una funcion de mutacion
def mutacion(individuo):
    # Mutamos un gen aleatorio del individuo
    gen = random.randint(0, len(individuo)-1)
    individuo[gen] = 1 - individuo[gen]
    return individuo

# CREAMOS una funcion de evolucion
def evolucion(individuos):
    # Seleccionamos los 10 individuos con mejor evaluacion
    seleccionados = seleccion(individuos)
    # Cruzamos los individuos seleccionados
    hijos = []
    for i in range(0, len(seleccionados), 2):
        hijo1, hijo2 = cruce(seleccionados[i], seleccionados[i+1])
        # Mutamos los hijos
        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)
        # Agregamos los hijos a la lista de individuos
        hijos.append(hijo1)
        hijos.append(hijo2)
    return hijos
# CREAMOS una funcion de seleccion
def seleccion(individuos):
    # Ordenamos los individuos por su evaluacion
    individuos.sort(key=lambda x: evaluacion(x), reverse=True)
    # Seleccionamos los 10 individuos con mejor evaluacion
    seleccionados = individuos[:10]
    return seleccionados

