# modulos
import random
random.seed(0)

# lista de individuos
individuos = []
# listas de aptitudes y restricciones
aptitudes = []
costos = []
# listas de probabilidades y probabilidades acumuladas
probabilidades = []
probabilidades_ac = []
# padres 1 y 2
padre1 = []
padre2 = []
# hijos 1 y 2
hijo1 = []
hijo2 = []
# listas cruza y mutacion
cruza = []
auxiliar = []


# CREAMOS individuos con genes aleatorios
def genera_individuo():
    return [random.randint(1, 10) for _ in range(7)]

# EVALUAMOS la aptitud (costo) de un individuo
def aptitud(individuo):
    return sum([individuo.count(1)*10, 
                individuo.count(2)*8, 
                individuo.count(3)*12, 
                individuo.count(4)*6, 
                individuo.count(5)*3, 
                individuo.count(6)*2, 
                individuo.count(7)*2])

# EVALUAMOS las restricciones (peso) de un individuo
def restriccion(individuo):
    return sum([individuo.count(1)*4,
                individuo.count(2)*2,
                individuo.count(3)*5,
                individuo.count(4)*5,
                individuo.count(5)*2,
                individuo.count(6)*1.5,
                individuo.count(7)*1])

# CREAMOS la lista de invidiuos considerando las restricciones
def genera_lista_individuos(individuos):
    numero_deseado_i = 10
    while len(individuos) < numero_deseado_i:
    # generamos un individuo aleatorio
        individuo = genera_individuo()
        # los individuos deben tener al menos 3 love potion (2) y 2 skiving snackbox (4),
        # además, si el individuo pesa mas del limite (30), se descarta
        if individuo.count(2)>=3 and individuo.count(4)>=2 and restriccion(individuo)<=30:
                individuos.append(individuo)
                # print(str(individuo) + "\ncuesta: " + str(aptitud(individuo)) + " y pesa: " + str(restriccion(individuo)))
    print("Se han generado suficientes individuos (" + str(len(individuos)) + ")")

# CALCULAMOS la aptitud de cada individuo
def vector_aptitud(aptitudes, individuos):
    for individuo in individuos:
        apt = aptitud(individuo)
        aptitudes.append(apt)

# CALCULAMOS el costo de cada individuo
def vector_costos(costos, individuos):
    for individuo in individuos:
        cst = restriccion(individuo)
        costos.append(cst)

# CALCULAMOS la probabilidad de seleccion
def probabilidad(probabilidades, probabilidades_ac, aptitudes):
    #suma de todas las aptitudes
    siu = sum(aptitudes)
    for apt in aptitudes:
        probabilidades.append(apt / siu)
    probabilidad_ac = 0
    for apt in aptitudes:
        probabilidad_ac += apt / siu
        probabilidades_ac.append(probabilidad_ac)

# GENERAMOS la lista random de cruza
def genera_elemento_cruza():
    return [random.uniform(0,1) for _ in range(7)]

# ruleta
def ruleta(probabilidades_ac, individuos):
    global padre1, padre2  
    # Hacer uso de variables globales
    # crear dos números al azar
    r1 = random.uniform(0,1)
    r2 = random.uniform(0,1)
    # recorrer probabilidad acumulada para decidir los dos papás
    for i in range(len(probabilidades_ac)): 
        if probabilidades_ac[i] > r1:
            padre1 = individuos[i]
            no_repetir = probabilidades_ac[i]
            break
    encontrado = False
    while not encontrado:
        for i in range(len(probabilidades_ac)):
            if probabilidades_ac[i] > r2:
                if probabilidades_ac[i] == no_repetir:
                    r2 = random.uniform(0,1)
                    print("Reasigno r2 para evitar cruza del mismo individuo")
                    break  # Salir del ciclo for y volver a empezar
                else:
                    padre2 = individuos[i]
                    encontrado = True  # Hemos encontrado un padre diferente, salir del while
                    break 
    return padre1, padre2

# algoritmo de cruza
def cruzar(cruza, hijo1, hijo2):
    hijo1.clear()  # Limpiar antes de cada cruce
    hijo2.clear()
    
    for i in range(7):  # Ajustar para que el índice empiece en 0
        if cruza[i] <= .5:
            hijo1.append(padre1[i])
        else:
            hijo1.append(padre2[i])

    for i in range(7):  # Ajustar para que el índice empiece en 0
        if cruza[i] <= .5:
            hijo2.append(padre2[i])
        else:
            hijo2.append(padre1[i])


def test():
    # se genera la lista de individuos
    genera_lista_individuos(individuos)

    # hacemos los vectores de aptitudes y costos
    vector_aptitud(aptitudes, individuos)
    vector_costos(costos, individuos)

    print("valores (vector): " + str(aptitudes))
    print("costos (vector): " + str(costos))

    # calculamos la probabilidad de seleccion y la probabilidad acumulada usando las aptitudes de los individuos
    probabilidad(probabilidades, probabilidades_ac, aptitudes)

    print("probabilidad de seleccion (vector): " + str(probabilidades))
    print("probabilidad acumulada (vector): " + str(probabilidades_ac))


test()