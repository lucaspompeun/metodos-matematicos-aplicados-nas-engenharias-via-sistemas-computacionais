# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:55:29 2019

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
        Função Logaritmica em Python

Nome do sript: funcao_log

Disponível em:
    
    
"""
# Importando Bibliotecas
# Biblioteca numpy: Operações matemáticas

import numpy as np
 
# Biblioteca matplotlib: Represntação Gráfica
import matplotlib.pyplot as plt

# Função Logaritmica : fl = log(x) na base a
# Valor da base: a 
print('==========================')
print('Base da Função Logaritmica:')
a = 2
print('a =',a)
print('')
# Classificação da Função: Crescente ou Decrescente
print('Classificação da Função:')
# Loop condicional
if (a > 1):
    print('Logaritmica Crescente')
elif (0<a<1): 
    print('Logaritmica Decrescente')
else:
    print('Não é Função Logaritmica')
print('==========================')  

# Variável independente: x
# Domínio da Função: (início, fim, número de pontos)
x = np.linspace(0.1,10,30)
fl = np.log(x)/np.log(a)

input("Pressione <enter> para representar graficamente")
print('')

# Representação Gráfica de fl
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,fl,'k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função Logaritmica')
plt.grid(True)
plt.show()

print('=== Fim do Programa funcao_log ===')
print('')
input("Acione <Ctrl + l> para limpar o console")
