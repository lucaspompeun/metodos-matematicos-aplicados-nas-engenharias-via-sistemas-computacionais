# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:36:14 2019

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
        Derivadas Parciais
        
Nome do sript: derivadas_parciais

Disponível em: 
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/SINEPEM_2019/derivadas_parciais.py
    
"""

# Bibliotecas

# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x,y = sy.symbols('x,y')

print('')

# Função de várias Variáveis: f(x,y)
def f(x,y):
    return 3*x**2*y**3

# (f(x,y), x, 1) --> (Função, variável, ordem da derivada) 
# Derivada em função de x: dfx(x,y)
def dfx(x,y):
    return sy.diff(f(x,y), x, 1) 
# Derivada em função de y: dfy(x,y)
def dfy(x,y):
    return sy.diff(f(x,y), y, 1) 
print('')
print('=======================================================')
print('Função Analisada: f(x,y) =', f(x,y))

print('Derivada Parcial em função de x: dfx(x,y) =', dfx(x,y))

print('Derivada Parcial em função de y: dfy(x,y) =', dfy(x,y))

print('=======================================================')
print('')
# Valor Numérico das Derivadas Parciais
print('Valor Numérico da Derivada Parcial dfx')
x1 = 2; y1 = -1
print('nos pontos x1 e y1 -->', (x1,y1))

VN_dfx= dfx(x,y).subs(x,x1).subs(y,y1)
print('VN_dfx =', VN_dfx)

print('')
print('Valor Numérico da Derivada Parcial dfy')
x2 = 1; y2 = 3
print('nos pontos x2 e y2 -->', (x2,y2))
VN_dfy= dfy(x,y).subs(x,x2).subs(y,y2)
print('VN_dfy =', VN_dfy)

print('')
print('---> Fim do Programa derivadas_parciais <---')


