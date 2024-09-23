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

# CREAMOS individuos con genes aleatorios
def genera_individuo():
    return [random.randint(1, 7) for _ in range(10)]

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
    # generamos un individuo aleatorio
    individuo = genera_individuo()
    # los individuos deben tener al menos 3 love potion (2) y 2 skiving snackbox (4)
    if individuo.count(2)>=3 and individuo.count(4)>=2 :
        # si el individuo pesa mas del limite (30), se descarta
        if restriccion(individuo)<=30:
            individuos.append(individuo)
            # print(str(individuo) + "\ncuesta: " + str(aptitud(individuo)) + " y pesa: " + str(restriccion(individuo)))
    # los individuos que no cumplan las condiciones son descartados (se repite el proceso)
    if len(individuos) < numero_deseado_i:
        genera_lista_individuos(individuos)
    else:
        print("Se han generado suficientes individuos (" + str(len(individuos)) + ")")

# CALCULAMOS la aptitud de cada individuo
def vector_aptitud(aptitudes, individuos):
    for i in range(1, 11): 
        apt = aptitud(individuos[i-1])  
        aptitudes.append(apt)  

# CALCULAMOS el costo de cada individuo
def vector_costos(costos, individuos):
    for i in range(1, 11): 
        cst = restriccion(individuos[i-1])  
        costos.append(cst)  

# CALCULAMOS la probabilidad de seleccion
def probabilidad(probabilidades, probabilidades_ac, aptitudes):
    #sumar todas las aptitudes
    siu = 0
    for i in range(1, 11): 
        siu += aptitudes[i-1]

    for i in range(1, 11): 
        #calculando el vector de probabilidades normales
        probabilidad = aptitudes[i-1] / siu 
        probabilidades.append(probabilidad)
        
    probabilidad_ac =0
    for i in range(1, 11): 
        #calculando el vector de probabilidades acumuladas
        probabilidad_ac += aptitudes[i-1] / siu 
        probabilidades_ac.append(probabilidad_ac)

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