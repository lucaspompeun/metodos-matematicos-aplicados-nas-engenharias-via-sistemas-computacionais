# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:56:18 2019

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
        Operações com Matrizes
        
Nome do sript: operacoes_matrizes

Disponível em:
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/SINEPEM_2019/operacoes_matrizes.py
    
"""
# Biblioteca: numpy
import numpy as np

print('')
print('=======================================')
# Operações com Matrizes
# Adição de Matrizes
print("Adição de Matrizes")
A = np.array([[4, 2],[3, -1]])
B = np.array([[5, 2],[1, 0]])
C = A + B
print("A =\n",A,"\n")
print("B =\n",B,"\n")
print('C = A + B:')
print("C =\n",C,"\n")
print('')

# Multiplicação de Matrizes
print("Multiplicação de Matrizes")
D = np.array([[3, 6, 7],[5, -3, 0]])
print("D =\n",D)
print('')
E = np.array([[1,1],[2,1],[3,-3]])
print("E =\n",E)
print('')

F = D.dot(E)
print('F = DxE:')
print("F = \n",F)
print('')

# Subtração de Matrizes
print("Subtração de Matrizes")
G = A + B
print('G = A - B:')
print("G =\n",G,"\n")
print('')

# Matriz Transposta
print("At = Transposta de A:")
At = A.transpose()
print("At =\n",At)
print('')

# Matriz Inversa
Inv_A = np.linalg.inv(A)
print("Inv_A = Inversa de A:")
print("Inv_A =\n",Inv_A)
print('')

# Determinante de uma Matriz
print("Determinante da Matriz A:")
Det_A = np.linalg.det(A)
print("Det_A =\n",Det_A)
print('')
print('=======================================')
print(' ---> Fim do Programa operacoes_matrizes <---')