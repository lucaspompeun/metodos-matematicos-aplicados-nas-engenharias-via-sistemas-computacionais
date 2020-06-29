# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:50:09 2019

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
        Função Polinomial do 4º grau em Python

Nome do sript: funcao4

Disponível em: 

"""

# Importando Bibliotecas
# Biblioteca numpy: Operações matemáticas
 
import numpy as np
# Biblioteca matplotlib: Represntação Gráfica
import matplotlib.pyplot as plt

# Função do 4º grau : f4 = ax**4 + bx**3 + cx**2 + dx + e
print('Coeficientes da Função do 4º grau')
# Coeficientes: a (a ≠ 0), b, c, d, e
a = 1
b = 2
c = -13
d = -14
e = 24

print('Coeficiente: a =', a)
print('Coeficiente: b =', b)
print('Coeficiente: c =', c)
print('Coeficiente: d =', d)
print('Coeficiente: e =', e)

# Variável independente: x
# Domínio da Função: (início, fim, número de pontos)
x = np.linspace(-5,4,30)
f4 = a*x**4 + b*x**3 + c*x**2 + d*x + e

input("Pressione <enter> para representar graficamente")
print('')

# Representação Gráfica de f4
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,f4,'k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função do 4º grau')
plt.grid(True)
plt.show()

print('=== Fim do Programa funcao4 ===')
print('')
input("Acione <Ctrl + l> para limpar o console")