# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:02:54 2019

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
        Cálculo de Integrais Triplas
        
Nome do sript: integrais_triplas

Disponível em:
    
"""

# Bibliotecas

# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x,y,z = sy.symbols('x, y, z')

print('')
print('=======================================')
# Função de três variáveis: f(x,y,z)
def f(x,y,z):
    return 6*x**2*y*z
print('Função de três variáveis:')
print('f(x,y,z) =', f(x,y,z))
print('')
print('Integral Tripla')
x1 = 1; x2 = 2
y1 = 1; y2 = 2
z1 = 1; z2 = 2
print('Intervalos de Integração:')
print('(x1, x2), (y1, y2), (z1, z2):', (x1, x2), (y1, y2), (z1, z2))
# Integral tripla de f(x,y,z): F(x,y,z) 
def F(x,y,z):
    return sy.integrate(f(x,y,z), (x, x1, x2), (y, y1, y2), (z, z1, z2))
print('F(x,y,z) =', F(x,y,z))

print('')
print('=======================================')
print(' ')
print(' ---> Fim do Programa integrais_triplas <---')