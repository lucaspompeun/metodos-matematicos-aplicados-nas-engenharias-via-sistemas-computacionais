# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:31:35 2019

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PÁRA - IFPA ANANINDEUA

@author: 
        Prof. Dr. Denis C. L. Costa
        
        Discentes:
            Heictor Alves de Oliveira Costa
            Lucas Pompeu Neves
        
Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
                 
Assunto: 
        Representação de Gráfica de Funções com duas variáveis independentes
        
Nome do sript: graficos_3d

Disponível em:
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/SINEPEM_2019/graficos_3d.py
    
"""
# Bibliotecas

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Comandos para plotar Gráficos em 3D
fig = plt.figure(1)
ax = Axes3D(fig)

# Intervalos de Análises: (x1, x2) e (y1, y2)
x1 = -5; x2 = 5
y1 = -5; y2 = 5
# Elemento de discretização: d
d = 0.25
x = np.arange(x1, x2, d)
# Valores de y:
y = np.arange(y1, y2, d)
print('')
print('=======================================')
print('Intervalos de Análises:')
print('(x1, x2), (y1, y2):', (x1, x2), (y1, y2))
print('=======================================')

# Função de duas Variáveis: z(x,y)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

# Títulos do Gráfico 3D
ax.set_xlabel('Valores de x')
ax.set_ylabel('Valores de y')
ax.set_zlabel('Valores de z')
ax.set_title('Superfície de z = f(x,y)')

# Layout do Gráfico 3D:
# Opções de cores: cmap --> escolha a letra correspondente
a =  'Spectral'
b =  'seismic'
c =  'coolwarm'
d =  'PRGn'
e = 'RdYlBu'
f = 'RdGy' 
g = 'RdYlGn'

ax.plot_surface(x, y, z, cmap = b)
print('')
print(' **** Gráficos gerados pelo Programa graficos_3d ****')

# Gráfico de Contornos
fig = plt.figure()
# n --> Número de linhas de contorno
n = 25
plt.contour(x, y, z, n)
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Curvas de Nível de z = f(x,y)')
plt.show()
