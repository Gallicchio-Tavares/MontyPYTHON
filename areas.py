from math import pi
print('\033[32mVamos calcular áreas de figuras geométricas!\033[m')
frase = str(input('''Para analisar um quadrado ou um retângulo ou um paralelogramo, digite 1;
Para analisar um triângulo, digite 2;
Para analisar um losango, digite 3;
Para analisar um trapézio, digite 4;
Para analisar um círculo, digite 5;
Para analisar um cone, digite 6.'''))
if '1' in frase:
    l1 = float(input('Insira um valor para a Base:'))
    l2 = float(input('Insira um valor para a altura:'))
    print(f'A área é {l1 * l2}')
elif '2' in frase:
    b = float(input('Insira um valor para a Base:'))
    h = float(input('Insira um valor para a Altura:'))
    print(f'A área do triângulo é {b * h / 2}')
elif '3' in frase:
    d = float(input('Insira um valor para a diagonal menor:'))
    D = float(input('Insira um valor para a diagonal maior:'))
    print(f'A área do losango é {D * d / 2}')
elif '4' in frase:
    B = float(input('Insira um valor para a Base Maior:'))
    bm = float(input('Insira um valor para a Base Menor:'))
    a = float(input('Insira um valor para a Altura:'))
    print(f'A área do trapézio é {(B + bm) * a / 2}')
elif '5' in frase:
    r = float(input('Insira um valor para o raio:'))
    print(f'A área do círculo é {pi * r ** 2}')
elif '6' in frase:
    R = float(input('Insira um valor para o Raio da Base:'))
    g = float(input('Insira um valor para o Raio do Setor:'))
    print('A área total do cone é {:.3f}'.format(pi * R * (g + R)))
else:
    print('Desculpe, mas este número é inválido.')
