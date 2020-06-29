# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:11:20 2019

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
        Função Trigonométrica em Python: Função Seno

Nome do sript: funcao_seno

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
# Função seno: fs
fs = np.sin(x)
print('')
print('Função Seno = sen(x)')

input("Pressione <enter> para representar graficamente")
print('')

# Representação Gráfica de fs
# Comando plot: (variável, função, 'cor da linha')
plt.plot(x,fs,'k')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Função Seno')
plt.grid(True)
plt.show()

print('=== Fim do Programa funcao_seno ===')
print('')
input("Acione <Ctrl + l> para limpar o console")





