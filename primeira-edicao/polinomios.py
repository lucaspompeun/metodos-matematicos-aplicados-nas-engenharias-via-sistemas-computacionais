# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:41:14 2019

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
        Operações Polinomiais em Python

Nome do sript: polinomios

"""

# Importanto da Bilbioteca numpy
import numpy as np

# Dado o Polinômio encontrar as suas raízes: P1 = x² - 5x + 6
# Coeficientes do polinômio P1: coef
coef = (1, -5, 6)  
# Comando para contruir o polinômio: np.poly1d  
P1 = np.poly1d(coef) 
# Apresentar o polinômio P1 
print('P1 =')
print(P1)

# Determinando a raízes de P1
Zeros_P1 = np.roots(P1)
print('Raízes = ', Zeros_P1)

# Cálculo do valor numérico de P1 para x = 2.5: P1(x)
P1x = P1(2.5)
print('P1x=',P1(2.5))

# A linha de comando a seguir serve para pausar o programa
input("Pressione <enter> para continuar")
print('')

# Contruindo um Pominômio a partir das suas raízes: (-2 e 5)
# Raízes de P2
P2 = np.poly1d([-2, 5], True)
print('P2 =')
print(P2)

input("Pressione <enter> para continuar")
print('')

# Adição e Subtração de Polinômios 
P3 = P1 + P2
print('P3 = P1 + P2:')
print(P3)
input("Pressione <enter> para continuar")
print('')

P4 = P1 - P2
print('P4 = P1 - P2:')
print(P4)

input("Pressione <enter> para continuar")
print('')

# Multiplicação e Divisão de Polinômios
P5 = P1*P2
print('P5 = P1*P2 :')
print(P5)
input("Pressione <enter> para continuar")
print('')

P6 = P1/P2
print('P6 = P1 / P2:')
print('Quociente e resto -->',P6)

input("Pressione <enter> para continuar")
print('=== Fim do Programa polinomios ===')
print('')
print('Acione Ctrl + l para limpar a área de trabalho')


