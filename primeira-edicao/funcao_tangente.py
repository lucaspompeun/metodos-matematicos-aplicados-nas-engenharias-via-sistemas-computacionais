# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:23:35 2019

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
        Função Trigonométrica em Python: Função Tangente

Nome do sript: funcao_tangente

Disponível em: 
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-
    COMPUTATIONAL-ENVIRONMENT/blob/master/SINEPEM_2019/funcao_tangente.py
    
"""
# Importando Bibliotecas
# Biblioteca numpy: Operações matemáticas
 
import numpy as np
# Biblioteca matplotlib: Representação Gráfica
import matplotlib.pyplot as plt

# Variável independente: x em radianos
# Declarando pi: np.pi
x = np.linspace(-2*np.pi, 2*np.pi,100)
# Função tangente: np.tan
ft = np.tan(x)
print('')
print('Função Tangente = tan(x)')

input("Pressione <enter> para representar graficamente")
print('')

# Representação Gráfica de fs
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,ft,'k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função Tangente')
plt.grid(True)
plt.show()

print('=== Fim do Programa funcao_tangente ===')
print('')
input("Acione <Ctrl + l> para limpar o console")
