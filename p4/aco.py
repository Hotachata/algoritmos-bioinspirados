# inicializamos las constantes
p=0.5
Q=1
a=1.5
b=0.8
# bibliotecas
import random
import numpy as np
# matriz de ciudades con costos
c0=[0, 6, 9, 17, 13, 21]
c1=[6, 0, 19, 21, 12, 18]
c2=[9, 19, 0, 20, 23, 11]
c3=[17, 21, 20, 0, 15, 10]
c4=[13, 12, 23, 15, 0, 21]
c5=[21, 18, 11, 10, 21, 0]
ciudades=[c0, c1, c2, c3, c4, c5]
vista_ciudades=np.array(ciudades)
print("\nDistancias entre las ciudades:\n", vista_ciudades,"\n")
# matriz inicial de feromonas
t0=[0, 0.2, 0.2, 0.2, 0.2, 0.2]
t1=[0.2, 0, 0.2, 0.2, 0.2, 0.2]
t2=[0.2, 0.2, 0, 0.2, 0.2, 0.2]
t3=[0.2, 0.2, 0.2, 0, 0.2, 0.2]
t4=[0.2, 0.2, 0.2, 0.2, 0, 0.2]
t5=[0.2, 0.2, 0.2, 0.2, 0.2, 0]
feromonas=[t0, t1, t2, t3, t4, t5]

def ruleta(Pac, vector_costos):
    # crea un random r
    r = random.uniform(0,1)
    for i in Pac:
        if Pac[i] >= r:
            return i

def probabilidades(vector_costos, vector_feromonas):
    # calculamos los caminos que podría tomar la hormiga
    numeradores=[] # numeradores de la formula
    denominador=0 # denominador de la formula
    P=[] # vector de probabilidades
    Pac=[] # vector de probabilidades acumuladas
    aux=0
    for i in range(len(vector_costos)):
        if vector_costos[i]!=0:
            numerador=(vector_feromonas[i]**a)*((1/vector_costos[i])**b)
            numeradores.append(numerador) # tenemos una lista de numeradores
            denominador+=numerador # y un solo denominador
    for j in range(len(numeradores)):
        probabilidad=numeradores[j]/denominador
        P.append(probabilidad)
    for k in P:
        aux+=k
        Pac.append(aux)
    return Pac

# la funcion [iteraciones] esta pensada para ir dentro de un ciclo for de 0 
# a 5, esto para hacer las iteraciones de las hormigas al mismo tiempo
def iteraciones(nodo_inicial):
    vc=ciudades[nodo_inicial] # establecemos un vector de costos segun el nodo
    vf=feromonas[nodo_inicial] # vector de feromonas
    print(vc)
    print(vf)
    
    Pac=probabilidades(vc, vf) # vector de probabilidades acumuladas
    print(Pac)
    
    vpendientes = [0, 1, 2, 3, 4, 5]
    vpendientes.remove(nodo_inicial) # eliminamos el nodo inicial de la lista de pendientes
    print(vpendientes)
    
    # creamos una lista vacia para ir guardando los nodos que visitamos
    vcamino=[nodo_inicial]
    print(vcamino)
    
    # elegimos un nodo al azar con ruleta
    # suponiendo que ruleta nos regrese un entero que represente un nodo
    # nos movemos a ése nodo y lo agregamos a la lista tabu
    
    for i in vpendientes:
        # nodo_nuevo=ruleta(...)
        nodo_nuevo=4
        vpendientes.remove(nodo_nuevo)
        vcamino.append(nodo_nuevo)
        
        vc=ciudades[nodo_nuevo]
        vf=feromonas[nodo_nuevo]
        
        for j in vcamino:
            vc.pop(vcamino[j])
            vf.pop(vcamino[j])
        
        Pac=probabilidades(vc, vf)
    
print(iteraciones(1))