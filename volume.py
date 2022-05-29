from math import sqrt, pi
print('\033[34mVamos calcular o volume de figuras geométricas!\033[m')
figura = input('''Para analisar um cubo ou um paralelepípedo, digite 1;
Para analisar uma tetraedro regular, digite 2;
Para analisar uma esfera, digite 3;
Para analisar um cilindro, digite 4;
Para analisar um cone, digite 5.''')
if '1' in figura:
    l1 = float(input('Informe o valor do comprimento:'))
    l2 = float(input('Informe o valor da largura:'))
    l3 = float(input('Informe o valor da altura:'))
    print(f'O volume é {l1 * l2 * l3}')
elif '2' in figura:
    a = float(input('Informe o valor da aresta:'))
    print('O volume da pirâmide é {:.2f}'.format(a ** 3 * sqrt(2) / 12))
elif '3' in figura:
    r = float(input('Informe o valor do raio da esfera:'))
    print('O volume da esfera é {:.2f}'.format((4 * pi * r**3)/3))
elif '4' in figura:
    rb = float(input('Informe o valor do raio da base:'))
    alt = float(input('Informe o valor da altura co cilindro:'))
    print('O volume do cilindro é {:.2f}'.format(pi * rb ** 2 * alt))
elif '5' in figura:
    RB = float(input('Informe o valor do raio da base:'))
    H = float(input('Informe o valor da altura do cone:'))
    print('O volume do cone é {:.2f}'.format(1/3 * pi * RB ** 2 * H))
else:
    print('Número inválido.')