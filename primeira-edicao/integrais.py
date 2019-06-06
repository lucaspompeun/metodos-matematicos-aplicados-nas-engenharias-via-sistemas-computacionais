# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:57:47 2019

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
        Integral de uma Função com uma variável independente
        
Nome do sript: integrais

Disponível em: 

"""
# Bibliotecas

# Cálculo Diferencial e Integral: sympy
import sympy as sy

# Variáveis simbólicas
x=sy.symbols('x')
print('')
print('=======================================')
# Função de uma variável: f(x)
def f(x):
    return 3*x**2
print('Função:')
print('f(x) =', f(x))
print('')
# Integral Indefinida de f(x): F(x)
def F(x):
    return sy.integrate(f(x), x)
print('Integral Indefinida')
print('F(x) =', F(x))
print('')

# Integral Definida de f(x): F1(x) --> x = [a, b]
print('Integral Definida')
a = 0; b = 2
print('Intervalo de Integração: [a,b] = ', (a, b))
def F1(x):
    return sy.integrate(f(x), (x, a, b))
print('F1(x) = ', F1(x))
print('=======================================')
print(' ')
print(' ---> Fim do Programa integrais <---')
