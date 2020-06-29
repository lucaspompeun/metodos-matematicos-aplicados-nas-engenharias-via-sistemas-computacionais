# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:52:43 2019

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
        Função Trigonométrica em Python: Funções Seno e Cosseno
        
Nome do sript: funcoes_trigonometricas

Disponível em: 
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/SINEPEM_2019/funcoes_trigonometricas.py
    
"""

# Importando Bibliotecas
# Biblioteca numpy: Operações matemáticas
 
import numpy as np
# Biblioteca matplotlib: Representação Gráfica
import matplotlib.pyplot as plt

# Variável independente: x em radianos
# Declarando pi: np.pi
x = np.linspace(-2*np.pi, 2*np.pi,100)
# Função seno: fs
fs = np.sin(x)

# Função cosseno: np.cos
fc = np.cos(x)
print('')

print('')
print('Funções Seno e Cosseno')

input("Pressione <enter> para representar graficamente")
print('')
# Representação Gráfica de fs e fc
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,fs,'k',x,fc,'--k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.legend(["Seno","Cosseno"],loc=3)
plt.title('Funções Seno e Cosseno')
plt.grid(True)
plt.show()

print('=== Fim do Programa funcoes_trigonometricas ===')
print('')
input("Acione <Ctrl + l> para limpar o console")

