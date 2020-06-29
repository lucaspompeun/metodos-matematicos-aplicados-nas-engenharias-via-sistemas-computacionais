# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:11:15 2019

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
        Solucionar uma Equação
        
Nome do sript: equacao

Disponível em: 
    
"""
# Importando Biblioteca
# Biblioteca sympy: Matemática para Variáveis Simbólicas

import sympy as sy

# Declarando a variável simbólica: x

x = sy.symbols('x')
print('')
print('Equação a ser resolvida:')
# Declarando a Equação a ser resolvida: E(x) = 0
def E(x):
        return sy.sqrt(x+2)-2
print('E(x) =', E(x))
print('')
# Conjunto Solução: S
S = sy.solve(E(x))
print('Solução da Equação:')
print('=========')
print(' x =', S)
print('=========')
print('')
print('---> Fim do Programa equacao <---')


