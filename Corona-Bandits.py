# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:49:00 2020

@author: erick
"""

#Verificacao do melhor epsilon

from __future__ import print_function, division
from builtins import range

import numpy as np
import matplotlib.pyplot as plt

class Bandit:
    def __init__(self, m): #construtures
        self.m = m #media verdadeira
        self.mean = 0 #media estimada
        self.N = 0 #Qtde de valores total
        
    def pull(self): #Puxa alavanca
        
        for i in range(self.m):  
            dice = np.random.rand() *100
            if dice <= 3.5:
                return 1
            else:
                continue
            
        return 0
        
        
    def update(self, x): #Update medias
        self.N += 1
        self.mean = (1 - 1.0/self.N)*self.mean + 1.0/self.N*x #Formula de atualizar medias

#Retorna medias acumuladas             
def run_experiment(m1, m2, m3, eps, N):
    bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]
    
    data = np.empty(N) #N eh a qtde de testes
    
    for i in range(N):
        
        #Epsilon-Greedy
        p = np.random.random()
        if p < eps:
            j = np.random.choice(3)            
        else:
            j = np.argmax([b.mean for b in bandits])
        x = bandits[j].pull()
        bandits[j].update(x)
        
        data[i] = x
        
    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)
        
    plt.plot(cumulative_average)
    plt.plot(np.ones(N))
    plt.plot(np.ones(N))
    plt.plot(np.ones(N))
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.mean)

    return cumulative_average

if __name__ == '__main__':
  c_1 = run_experiment(1, 100, 1000, 0.1, 100000)
  c_05 = run_experiment(1, 100, 1000, 0.05, 100000)
  c_01 = run_experiment(1, 100, 1000, 0.01, 100000)

  # log scale plot
  plt.plot(c_1, label='eps = 0.1')
  plt.plot(c_05, label='eps = 0.05')
  plt.plot(c_01, label='eps = 0.01')
  plt.legend()
  plt.xscale('log')
  plt.show()


  # linear plot
  plt.plot(c_1, label='eps = 0.1')
  plt.plot(c_05, label='eps = 0.05')
  plt.plot(c_01, label='eps = 0.01')
  plt.legend()
  plt.show()