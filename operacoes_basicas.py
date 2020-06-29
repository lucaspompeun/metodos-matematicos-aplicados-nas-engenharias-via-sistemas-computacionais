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
        Operações Básicas de Matemática em Python

Nome do sript: operacoes_basicas
            
"""
# Importanto da Bilbioteca numpy
import numpy as np

# Declarando as Informações:
a = 5.7
b = -3.0
c = 7.4

# Executando as Operações:
D = a + b - c
print('D =', D)

E = (a*b)/c
print('E =', E) 
# ou poderemos arrendondar: round
print('E =', round(E,3))

# A linha de comando a seguir serve para pausar o programa
input("Pressione <enter> para continuar")

# Utilizando a biblioteca numpy na raiz quadrada: np.sqrt
F = np.sqrt(a+c)
print('F =', F) 
# ou poderemos arrendondar: round
print('F =', round(F,2))

input("Pressione <enter> para continuar")
# Utilizando a biblioteca numpy no Logaritmo: np.log
G = np.log2(c)
print('G =', G) 
# ou poderemos arrendondar: round
print('G =', round(G,5))


input("Pressione <enter> para continuar")
# Logaritmo Natural
H = np.log(a)
print('H =', H) 
# ou poderemos arrendondar: round
print('H =', round(H,4))

input("Pressione <enter> para continuar")
# Potenciação 1
I1 = a**3+b**2-c**(-1)
print('I1 =', I1) 

# Potenciação 2
I2 = pow(a,3)+pow(b,2)-pow(c,-1)
print('I2 =', I2) 

input("Pressione <enter> para continuar")

# Logo I1 = I2
print('I1 = I2 =', I1)
# ou poderemos arrendondar: round
print('I1 =', round(I1,2))

# Exponencial de base e: bilbioteca numpy
J = 2*np.exp(4)
print('J =', round(J,3))

input("Pressione <enter> para continuar")
print('=== Fim do Programa operacoes_basicas ===')
# Utilize o compando Ctrl + l no console para limpar a área de trabalho do spyder.






