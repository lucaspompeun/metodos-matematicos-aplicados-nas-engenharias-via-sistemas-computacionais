# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:19:25 2019

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
        Resolução de Sistemas Lineares
        
Nome do sript: sistemas_lineares

Disponível em:
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/SINEPEM_2019/sistemas_lineares.py
    
"""

# Biblioteca: numpy
import numpy as np

print('')
print('=======================================')
# Resolução de Sistemas Lineares
print('Resolução de Sistemas Lineares')
print('')
# Declarando a Matriz dos Coeficientes: A
A = np.array([[1,1,1], [1,-1,-1], [2,-1,1]])
print('Matriz dos Coeficientes:' )
print('A =',"\n", A,"\n")

# Declarando a Matriz dos Termos Independentes: B
B = np.array([[6], [-4], [1]])
print('Matriz dos Termos Independentes:' )
print('B =',"\n", B,"\n")

# Matriz Solução: X = inv(A)*B 
X = np.linalg.solve(A, B)
print('Matriz solução:') 
print('X =')
print(X)
print('')
print('=======================================')
print(' ---> Fim do Programa sistemas_lineares <---')