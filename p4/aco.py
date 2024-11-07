# inicializamos las constantes
p=0.5
Q=1
a=1.5
b=0.8
# numpy
import numpy as np
# matriz de ciudades con costos
c1=[0, 6, 9, 17, 13, 21]
c2=[6, 0, 19, 21, 12, 18]
c3=[9, 19, 0, 20, 23, 11]
c4=[17, 21, 20, 0, 15, 10]
c5=[13, 12, 23, 15, 0, 21]
c6=[21, 18, 11, 10, 21, 0]
ciudades=[c1, c2, c3, c4, c5, c6]
vista_ciudades=np.array(ciudades)
print("\nDistancias entre las ciudades:\n", vista_ciudades,"\n")
# matriz inicial de feromonas
t1=[0, 0.2, 0.2, 0.2, 0.2, 0.2]
t2=[0.2, 0, 0.2, 0.2, 0.2, 0.2]
t3=[0.2, 0.2, 0, 0.2, 0.2, 0.2]
t4=[0.2, 0.2, 0.2, 0, 0.2, 0.2]
t5=[0.2, 0.2, 0.2, 0.2, 0, 0.2]
t6=[0.2, 0.2, 0.2, 0.2, 0.2, 0]
feromonas=[t1, t2, t3, t4, t5, t6]

def iteraciones(vector_costos, vector_feromonas):
    # calculamos los caminos que podría tomar la hormiga
    numeradores=[] # numeradores de la formula
    denominador=0 # denominador de la formula
    P=[] # vector de probabilidades
    for i in range(len(vector_costos)):
        if vector_costos[i]!=0:
            numerador=(vector_feromonas[i]**a)*((1/vector_costos[i])**b)
            numeradores.append(numerador) # tenemos una lista de numeradores
            denominador=denominador+numerador # y un solo denominador
    for j in range(len(numeradores)):
        probabilidad=numeradores[j]/denominador
        P.append(probabilidad)
    return P

print(iteraciones(c1, t1))