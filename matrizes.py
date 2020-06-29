# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:51:13 2019

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
        Matrizes
        
Nome do sript: matrizes

Disponível em:
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/SINEPEM_2019/matrizes.py
    
"""

# Biblioteca: numpy
import numpy as np
print('')
print('=======================================')
# Construção de matrizes
# Matriz de Números Reais
print("Matriz de Números Reais")
A = np.array([[4.2, 6, 9.7],[8.1, 5, 2]])
print('Matriz A =')
print(A,"\n")
print('')
# Matriz de Números Complexos
print("Matriz com Números Complexos")
B = np.array([[4 + 2j, 6, 9],[8, 5 - 3j, 2]], dtype = complex)
print('Matriz B =')
print(B,"\n")
print('')
# Matriz Nula
print("Matriz Nula:")
C = np.zeros( (4,5) ) # Ordem 4 x 5
print('C =')
print(C, "\n")
print('')
# Matriz Identidade
print("Matriz Identidade")
D = np.identity(3,float) # 3ª Ordem  
print('D =')
print(D,"\n")
print('')
print('=======================================')
print(' ')
print(' ---> Fim do Programa matrizes <---')