# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 09:26:04 2019

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
        Função Exponencial em Python

Nome do sript: funcao_exp

Disponível em: 
    
"""
# Importando Bibliotecas
# Biblioteca numpy: Operações matemáticas
 
import numpy as np
# Biblioteca matplotlib: Represntação Gráfica
import matplotlib.pyplot as plt

# Função Exponencial : fe = a**x
# Valor da base: a 
print('==========================')
print('Base da Função Exponencial:')
a = 0.5
print('a =',a)
print('')
# Classificação da Função: Crescente ou Decrescente
print('Classificação da Função:')
# Loop condicional
if (a > 1):
    print('Exponencial Crescente')
elif (0<a<1): 
    print('Exponencial Decrescente')
else:
    print('Não é Função Exponencial')
print('==========================')  

# Variável independente: x
# Domínio da Função: (início, fim, número de pontos)
x = np.linspace(-5,5,20)
fe = a**x

input("Pressione <enter> para representar graficamente")
print('')

# Representação Gráfica de fe
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,fe,'k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função Exponencial')
plt.grid(True)
plt.show()

print('=== Fim do Programa funcao_exp ===')
print('')
input("Acione <Ctrl + l> para limpar o console")
