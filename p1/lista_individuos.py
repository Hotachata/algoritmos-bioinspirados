# modulos
import random
random.seed(0)

# lista de individuos
individuos = []

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
def genera_lista_individuos():
    numero_deseado_i = 10
    # generamos un individuo aleatorio
    individuo = genera_individuo()
    # los individuos deben tener al menos 3 love potion (2) y 2 skiving snackbox (4)
    if individuo.count(2)>=3 and individuo.count(4)>=2 :
        # si el individuo pesa mas del limite (30), se descarta
        if restriccion(individuo)<=30:
            individuos.append(individuo)
            print(str(individuo) + "\ncuesta: " + str(aptitud(individuo)) + " y pesa: " + str(restriccion(individuo)))
    # los individuos que no cumplan las condiciones son descartados (se repite el proceso)
    if len(individuos) < numero_deseado_i:
        genera_lista_individuos()
    else:
        print("Se han generado suficientes individuos")

# probabilidad de seleccion
def probabilidad(individuo):
    return "woaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaooooooooos"

def algoritmo_genetico():
    print("Algoritmo genetico")
