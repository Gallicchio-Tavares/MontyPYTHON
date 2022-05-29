from math import sqrt, trunc

print('-x-' * 15)
print('\033[36m- Calculando uma equação de segundo grau -\033[m')
print('-x-' * 15)

a = float(input('Insira o valor de "a" :'))
b = float(input('Insira o valor de "b" :'))
c = float(input('Insira o valor de "c" :'))

delta = b**2 - 4 * a * c

if delta < 0:
    print('O valor de Delta é negativo. Dessa forma, não existem soluções Reais para essa equação.')
    print(f'O valor de Delta é {delta}')

elif delta == 0:
    print('O valor de delta é 0. Dessa forma, existem duas soluções Reais e iguais para a equação.')
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'As soluções são {x1} e {x2}')

elif delta > 0:
    print('O valor de Delta é positivo. Dessa forma, existem duas soluções Reais e diferentes para essa equação')
    print(f'O valor de Delta é {delta}')
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'As soluções são {x1} e {x2}')
    if x1 - trunc(x1) != 0 and x2 - trunc(x2) != 0:
        print('Soluções aproximadas: {:.2f} e {:.2f}'.format(x1, x2))
