# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:23:49 2019

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
        Função Polinomial do 2º grau em Python

Nome do sript: funcao2

Disponível em: 
    
    
"""

# Importando Bibliotecas
# Biblioteca numpy: Operações matemáticas 
import numpy as np

# Biblioteca matplotlib: Represntação Gráfica
import matplotlib.pyplot as plt

# Função do 2º grau : f2 = ax² + bx + c
print('Coeficientes da Função do 2º grau')
# Coeficientes: a (a ≠ 0), b e c
a = -2
b = 6
c = 20
print('Coeficiente: a =', a)
print('Coeficiente: b =', b)
print('Coeficiente: c =', c)

# Variável independente: x
# Domínio da Função: (início, fim, número de pontos)
x = np.linspace(-3,6,20)
f2 = a*x**2 + b*x + c

input("Pressione <enter> para representar graficamente")
print('')

# Representação Gráfica de f2
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,f2,'k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função do 2º grau')
plt.grid(True)
plt.show()

print('=== Fim do Programa funcao2 ===')
print('')
input("Acione <Ctrl + l> para limpar o console")

