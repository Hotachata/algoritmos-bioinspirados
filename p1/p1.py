# modulos
import random
random.seed(0)

# lista de individuos
individuos = []

# CREAMOS individuos con genes aleatorios
def genera_individuo():
    return [random.randint(0, 7) for _ in range(10)]

# CREAMOS la lista de invidiuos considerando las restricciones
def genera_individuos():
    numero_deseado_i = 10
    # generamos un individuo aleatorio
    individuo = genera_individuo()
    # los individuos deben tener al menos 3 love potion (2) y 2 skiving snackbox (4)
    if individuo.count(2)>=3 and individuo.count(4)>=2 :
        individuos.append(individuo)
        print(individuo)
    # los individuos que no cumplan las condiciones son descartados (se repite el proceso)
    if len(individuos) < numero_deseado_i:
        genera_individuos()
    else:
        print("Se han generado suficientes individuos")

genera_individuos()
print(individuos)