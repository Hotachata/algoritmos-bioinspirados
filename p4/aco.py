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