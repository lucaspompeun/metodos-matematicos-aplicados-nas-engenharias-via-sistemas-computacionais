# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:23:50 2019

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
        Cálculo de Integrais Duplas
        
Nome do sript: integrais_duplas

Disponível em:
    
"""

# Bibliotecas

# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x,y = sy.symbols('x, y')

print('')
print('=======================================')
# Função de duas variáveis: f(x,y)
def f(x,y):
    return 6*x**2*y
print('Função de duas variáveis:')
print('f(x,y) =', f(x,y))
print('')
print('Integral Dupla')
x1 = 1; x2 = 2
y1 = 1; y2 = 2
print('Intervalos de Integração:')
print('(x1, x2), (y1, y2):', (x1, x2), (y1, y2))
# Integral dupla de f(x,y): F(x,y) 
def F(x,y):
    return sy.integrate(f(x,y), (x, x1, x2), (y, y1, y2))
print('F(x,y) =', F(x,y))

print('')
print('=======================================')
print(' ')
print(' ---> Fim do Programa integrais_duplas <---')