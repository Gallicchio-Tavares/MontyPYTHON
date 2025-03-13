import csv
import random

num = random.randint(1,397)

with open('filmes.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for indice, linha in enumerate(leitor_csv, start=1):
        if indice == num:
            print(f'Assista ao filme {linha[1]} - {linha[2]}. Link: {linha[3]}')
            break
            
print(num)