import pandas as pd
import numpy as np
import math 
import matplotlib.pyplot as plt # Se importa la librería
import matplotlib.patches as patches
from valoresentrada import tamano_particulas
tamiz = pd.Series(['1 1/2"','1"','3/4"','3/8"','No.4','No.10','No.20','No.40','No.60','No.100','No.200'])
tamaño_particulas = pd.Series(dtype='float64')
porcentaje_pasa = pd.Series([
    100, #porcentaje de partículas que pasan por el tamiz 1 1/2"
    100, #porcentaje de partículas que pasan por el tamiz 1"
    90, #porcentaje de partículas que pasan por el tamiz 3/4"
    86.5, #porcentaje de partículas que pasan por el tamiz 3/8"
    70, #porcentaje de partículas que pasan por el tamiz No.4
    66.5, #porcentaje de partículas que pasan por el tamiz No.10
    52, #porcentaje de partículas que pasan por el tamiz No.20
    38.4, #porcentaje de partículas que pasan por el tamiz No.40
    23, #porcentaje de partículas que pasan por el tamiz No.60
    8.5, #porcentaje de partículas que pasan por el tamiz No.100
    5 #porcentaje de partículas que pasan por el tamiz No.200
])
T200 = porcentaje_pasa[10]
T4 = porcentaje_pasa[4]
print("Porcentaje que pasa del tamiz 200:", T200)
print("Porcentaje que pasa del número 4:", T4)
tamaño_particulas = pd.Series([
    37.5, #abertura tamiz 1 1/2"
    25.4, #abertura tamiz 1"
    19, #abertura tamiz 3/4"
    9.51, #abertura tamiz 3/8"
    4.76, #abertura tamiz No.4
    2, #abertura tamiz No.10
    0.841, #abertura tamiz No.20
    0.420, #abertura tamiz No.40
    0.250, #abertura tamiz No.60
    0.149, #abertura tamiz No.100
    0.074 #abertura tamiz No.200
])

# Calcula el Cu y Cc
d60 = tamaño_particulas[6]  # Tamaño de partícula correspondiente al tamiz No. 40
d10 = tamaño_particulas[9]  # Tamaño de partícula correspondiente al tamiz No. 200
d30 = tamaño_particulas[8]  # Tamaño de partícula correspondiente al tamiz No. 60

Cu = d60 / d10
Cc = (d30 ** 2) / (d60 * d10)

#se tabulan los límites superior e inferior máximo permitidos por el INVIAS
#limite superior
limite_superior_ejey = pd.Series([100,100,100,100,100,100,100,85,60,30,10])
limite_superior_ejex = pd.Series([25,19,12.5,9.5,6.6,4.75,2.36,1.18,0.6,0.3,0.15]) 

#limite inferior
limite_inferior_ejey = pd.Series([100,100,100,100,100,95,80,50,25,10,2])
limite_inferior_ejex = pd.Series([25,19,12.5,9.5,6.6,4.75,2.36,1.18,0.6,0.3,0.15])

#Se crea una variable para poder organizar los datos en forma de tabla
tabla = pd.DataFrame({
    'tamiz': tamiz,
    'tamaño particulas(mm)': tamaño_particulas,
    'porcentaje pasa': porcentaje_pasa,
    'Limite superior y': limite_superior_ejey,
    'limite superior x': limite_superior_ejex,
})

print(tabla)#se imprime la tabla de la granulometria
# Imprime el Cu y Cc
print("Coeficiente de Uniformidad (Cu):", round(Cu, 2))
print("Coeficiente de Curvatura (Cc):", round(Cc, 2))
#se crea la grafica granulometrica
plt.figure(figsize=(10, 3))  # Ajusta el tamaño de la figura

plt.scatter(limite_superior_ejex, limite_superior_ejey)
plt.plot(limite_superior_ejex, limite_superior_ejey, label="Límite superior")
plt.scatter(limite_inferior_ejex, limite_inferior_ejey, label="Límite inferior")
plt.plot(limite_inferior_ejex, limite_inferior_ejey, label="Límite inferior")
plt.scatter(tamaño_particulas, porcentaje_pasa, label="granulometria")
plt.plot(tamaño_particulas, porcentaje_pasa, label="granulometria")
plt.grid(color='grey', lw=0.5)
plt.xscale('log', base=10)
plt.gca().invert_xaxis()
plt.title("DISTRIBUCION GRANULOMETRICA", fontsize=15, color="black")  # se agrega el título a la gráfica granulométrica
plt.xlabel("Tamaño de partícula (mm)", fontsize=12)  # se agregan los títulos a los ejes
plt.ylabel("Porcentaje que pasa (%)", fontsize=12)  # se agregan los títulos a los ejes
plt.ylim(0, 110)  # Se establece el límite máximo del eje y
plt.annotate("Limite superior", (0.5, 65))  # se agregan los títulos
plt.annotate("Limite inferior", (4, 30))  # se agregan los títulos
rect = patches.Rectangle((0.05, 75), 0.06, 30, linewidth=1, edgecolor='black', facecolor='none')
plt.gca().add_patch(rect)
# Agrega los valores de Cu y Cc en la gráfica
plt.text(0.1, 80, f"Cu: {Cu:.2f}", fontsize=12, ha='left')
plt.text(0.1, 90, f"Cc: {Cc:.2f}", fontsize=12, ha='left')
plt.tight_layout()  # Ajusta el espaciado de la figura
plt.show()