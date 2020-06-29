# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 09:20:00 2019

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
        Limite de uma Função 
        
Nome do sript: limites

Disponível em: 
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/SINEPEM_2019/limites.py

"""

# Bibliotecas

# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x = sy.symbols('x')
print('')
# Função de uma Variável: f(x)
def f(x):
    return sy.sin(x)

# (f(x), x,1) --> (Função, variável, valor assumido) 
# Limite da Função: L(x)
# Tendência: x --> a
a =  sy.pi/2   
def L(x):
    return sy.limit(f(x), x, a) 
print('')
print('=======================================')
print('Função Analisada: f(x) =', f(x))
print('Limite da Função f(x) ')
print('quando x -->', a)
print('   L(x) =', L(x))
print('=======================================')
print('')
print('---> Fim do Programa limites <---')

