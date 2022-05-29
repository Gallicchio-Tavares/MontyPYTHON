from math import trunc

print('-x-' * 15)
print('\033[35m- Transformando unidades de temperatura -\033[m')
print('-x-' * 15)

uni = str(input('''Para transformar Kelvin em Celsius, digite "1";
Para transformar Kelvin em Fahrenheit, digite "2";
Para transformar Fahrenheit em Celsius, digite "3";
Para transformar Fahrenheit em Kelvin, digite "4";
Para transformar Celsius em Kelvin, digite "5";
Para transformar Celsius em Fahrenheit, digite "6". '''))

n = float(input('Escreva o valor da temperatura: '))

if '1' in uni:
    c = n - 273
    print(f'O valor é {c} graus Celsius.')
elif '2' in uni:
    f = (9 * n - 2457) / 5
    print(f'O valor é {trunc(f)} graus Fahrenheit.')
elif '3' in uni:
    ce = (5 * n - 160) / 9
    print(f'O valor é {ce} graus Celsius.')
elif '4' in uni:
    k = (5 * n + 2297) / 9
    print(f'O valor é {trunc(k)} Kelvin.')
elif '5' in uni:
    kelvin = n + 273
    print(f'O valor é {kelvin} Kelvin.')
elif '6' in uni:
    fah = (9 * n + 160) / 5
    print(f'O valor é {fah} Fahrenheit.')