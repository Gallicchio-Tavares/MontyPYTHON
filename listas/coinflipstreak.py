'''
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads 
and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 
'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 
10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the 
function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.
'''

import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
  lista = []
  for i in range(100):
      lista.append(random.randint(0, 1))  # admitir que 0 é cara e 1 é coroa

  lista2 = []

  for num in lista:
      if not lista2 or num == lista2[-1]:  # Se lista2 estiver vazia ou o número atual for igual ao último número em lista2
          lista2.append(num)
          if len(lista2) == 6:  # Se lista2 tem 6 elementos
              numberOfStreaks += 1
              lista2.pop(0)  # Remover o primeiro elemento para manter a janela de 6 elementos
      else:
          lista2 = [num]  # Começar uma nova sequência com o número atual

print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))
