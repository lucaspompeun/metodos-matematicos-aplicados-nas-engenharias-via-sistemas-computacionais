# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:20:48 2019

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
        Função Trigonométrica em Python: Função Cosseno

Nome do sript: funcao_cosseno

Disponível em: 
    
"""

# Importando Bibliotecas
# Biblioteca numpy: Operações matemáticas
 
import numpy as np
# Biblioteca matplotlib: Represntação Gráfica
import matplotlib.pyplot as plt

# Variável independente: x em radianos
# Declarando pi: np.pi
x = np.linspace(-2*np.pi, 2*np.pi,100)
# Função cosseno: np.cos
fc = np.cos(x)
print('')
print('Função Cosseno')

input("Pressione <enter> para representar graficamente")
print('')

# Representação Gráfica de fs
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,fc,'k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função Cosseno')
plt.grid(True)
plt.show()

print('=== Fim do Programa funcao_cosseno ===')
print('')
input("Acione <Ctrl + l> para limpar o console")
