# Numeros romanos

resposta = "s"
while resposta == "s":
    
    opcao = int(input('O que deseja fazer? \n [1] Decimal para romano \n [2] Romano para decimal\n'))
    
    if opcao == 1:
        decimal = str(input('Insira o numero (1 até 3000): '))
        if len(decimal) == 1:
            if "1" in decimal:
                unidade = "I"
            elif "2"in decimal:
                unidade = "II"
            elif "3" in decimal:
                unidade = "III"
            elif "4" in decimal:
                unidade = "IV"
            elif "5" in decimal:
                unidade = "V"
            elif "6" in decimal:
                unidade = "VI"
            elif "7" in decimal:
                unidade = "VII"
            elif "8" in decimal:
                unidade = "VIII"
            elif "9" in decimal:
                unidade = "IX"
            elif "0" in decimal:
                unidade = "inexistente."
            print(f'O numero {decimal} em romano é {unidade}')
        elif len(decimal) == 2: 
            if "1" in decimal:
                if decimal.find('1') == 0:
                    dezena = "X"
                if decimal.rfind('1') == 1:
                    unidade = "I"
            if "2" in decimal:
                if decimal.find('2') == 0:
                    dezena = "XX"
                if decimal.rfind('2') == 1:
                    unidade = "II"
            if "3" in decimal:
                if decimal.find('3') == 0:
                    dezena = "XXX"
                if decimal.rfind('3') == 1:
                    unidade = "III"
            if "4" in decimal:
                if decimal.find('4') == 0:
                    dezena = "XL"
                if decimal.rfind('4') == 1:
                    unidade = "IV"
            if "5" in decimal:
                if decimal.find('5') == 0:
                    dezena = "L"
                if decimal.rfind('5') == 1:
                    unidade = "V"
            if "6" in decimal:
                if decimal.find('6') == 0:
                    dezena = "LX"
                if decimal.rfind('6') == 1:
                    unidade = "VI"
            if "7" in decimal:
                if decimal.find('7') == 0:
                    dezena = "LXX"
                if decimal.rfind('7') == 1:
                    unidade = "VII"
            if "8" in decimal:
                if decimal.find('8') == 0:
                    dezena = "LXXX"
                if decimal.rfind('8') == 1:
                    unidade = "VIII"
            if "9" in decimal:
                if decimal.find('9') == 0:
                    dezena = "XC"
                if decimal.rfind('9') == 1:
                    unidade = "IX"
            if "0" in decimal:
                unidade = ""
            print(f'O numero {decimal} em romano é {dezena + unidade}')
        elif len(decimal) == 3:
            if "1" in decimal:
                if decimal.find('1') == 0:
                    centena = "C"
                if decimal.find('1', 1) == 1:
                    dezena = "X"
                if decimal.rfind('1') == 2:
                    unidade = "I"
            if "2"in decimal:
                if decimal.find('2') == 0:
                    centena = "CC"
                if decimal.find('2', 1) == 1:
                    dezena = "XX"
                if decimal.rfind('2') == 2:
                    unidade = "II"
            if "3" in decimal:
                if decimal.find('3') == 0:
                    centena = "CCC"
                if decimal.find('3', 1) == 1:
                    dezena = "XXX"
                if decimal.rfind('3') == 2:
                    unidade = "III"
            if "4" in decimal:
                if decimal.find('4') == 0:
                    centena = "CD"
                if decimal.find('4', 1) == 1:
                    dezena = "XL"
                if decimal.rfind('4') == 2:
                    unidade = "IV"
            if "5" in decimal:
                if decimal.find('5') == 0:
                    centena = "D"
                if decimal.find('5', 1) == 1:
                    dezena = "L"
                if decimal.rfind('5') == 2:
                    unidade = "V"
            if "6" in decimal:
                if decimal.find('6') == 0:
                    centena = "DC"
                if decimal.find('6', 1) == 1:
                    dezena = "LX"
                if decimal.rfind('6') == 2:
                    unidade = "VI"
            if "7" in decimal:
                if decimal.find('7') == 0:
                    centena = "DCC"
                if decimal.find('7', 1) == 1:
                    dezena = "LXX"
                if decimal.rfind('7') == 2:
                    unidade = "VII"
            if "8" in decimal:
                if decimal.find('8') == 0:
                    centena = "DCCC"
                if decimal.find('8', 1) == 1:
                    dezena = "LXXX"
                if decimal.rfind('8') == 2:
                    unidade = "VIII"
            if "9" in decimal:
                if decimal.find('9') == 0:
                    centena = "CM"
                if decimal.find('9', 1) == 1:
                    dezena = "XC"
                if decimal.rfind('9') == 2:
                    unidade = "IX"
            if "0" in decimal:
                if decimal.find('0') == 1:
                    dezena = ""
                if decimal.rfind('0') == 2:
                    unidade = ""
            print(f'O numero {decimal} em romano é {centena + dezena + unidade}')
        elif len(decimal) == 4:
            if "1" in decimal:
                if decimal.find('1') == 0:
                    milhar = "M"
                if decimal.find('1', 1) == 1:
                    centena = "C"
                if decimal.find('1', 2) == 2:
                    dezena = "X"
                if decimal.rfind('1') == 3:
                    unidade = "I"
            if "2" in decimal:
                if decimal.find('2') == 0:
                    milhar = "MM"
                if decimal.find('2', 1) == 1:
                    centena = "CC"
                if decimal.find('2', 2) == 2:
                    dezena = "XX"
                if decimal.rfind('2') == 3:
                    unidade = "II"
            if "3" in decimal:
                if decimal.find('3') == 0:
                    milhar = "MMM"
                if decimal.find('3', 1) == 1:
                    centena = "CCC"
                if decimal.find('3', 2) == 2:
                    dezena = "XXX"
                if decimal.rfind('3') == 3:
                    unidade = "III"
            if "4" in decimal:
                if decimal.find('4') == 1:
                    centena = "CD"
                if decimal.find('4', 2) == 2:
                    dezena = "XL"
                if decimal.rfind('4') == 3:
                    unidade = "IV"
            if "5" in decimal:
                if decimal.find('5') == 1:
                    centena = "D"
                if decimal.find('5', 2) == 2:
                    dezena = "L"
                if decimal.rfind('5') == 3:
                    unidade = "V"
            if "6" in decimal:
                if decimal.find('6') == 1:
                    centena = "DC"
                if decimal.find('6', 2) == 2:
                    dezena = "LX"
                if decimal.rfind('6') == 3:
                    unidade = "VI"
            if "7" in decimal:
                if decimal.find('7') == 1:
                    centena = "DCC"
                if decimal.find('7', 2) == 2:
                    dezena = "LXX"
                if decimal.rfind('7') == 3:
                    unidade = "VII"
            if "8" in decimal:
                if decimal.find('8') == 1:
                    centena = "DCCC"
                if decimal.find('8', 2) == 2:
                    dezena = "LXXX"
                if decimal.rfind('8') == 3:
                    unidade = "VIII"
            if "9" in decimal:
                if decimal.find('9') == 1:
                    centena = "CM"
                if decimal.find('9', 2) == 2:
                    dezena = "XC"
                if decimal.rfind('9') == 3:
                    unidade = "IX"
            if "0" in decimal:
                if decimal.find("0") == 1:
                    centena = ""
                if decimal.find('0', 2) == 2:
                    dezena = ""
                if decimal.rfind('0') == 3:
                    unidade = ""
            print(f'O numero {decimal} é representado por {milhar + centena + dezena + unidade} em romano.')
    if opcao == 2:
        romano = str(input('Insira o numero romano: ')).upper() # EXEMPLO: MMMCCXXIV
        milhar = 0
        centena = 0
        dezena = 0
        unidade = 0
        if 'MMM' in romano:
            milhar = 3000
        elif 'MM' in romano:
            milhar = 2000
        elif 'M' in romano:
            milhar = 1000
        if 'CM' in romano:
            centena = 900
        elif 'DCCC' in romano:
            centena = 800
        elif 'DCC' in romano:
            centena = 700
        elif 'DC' in romano:
            centena = 600
        elif 'D' in romano and 'C' not in romano:
            centena = 500
        elif 'CD' in romano:
            centena = 400
        elif 'CCC' in romano and 'D' not in romano:
            centena = 300
        elif 'CC' in romano and 'D' not in romano:
            centena = 200
        elif 'C' in romano and 'D' not in romano:
            centena = 100
        if 'XC' in romano:
            dezena = 90
        elif 'LXXX' in romano:
            dezena = 80
        elif 'LXX' in romano:
            dezena = 70
        elif 'LX' in romano:
            dezena = 60
        elif 'L' in romano and 'X' not in romano:
            dezena = 50
        elif 'XL' in romano:
            dezena = 40
        elif 'XXX' in romano and 'L' not in romano:
            dezena = 30
        elif 'XX' in romano and 'L' not in romano:
            dezena = 20
        elif 'X' in romano and 'L' not in romano:
            dezena = 10
        if 'IX' in romano:
            unidade = 9
        elif 'VIII' in romano:
            unidade = 8
        elif 'VII' in romano:
            unidade = 7
        elif 'VI' in romano:
            unidade = 6
        elif 'V' in romano and 'I' not in romano:
            unidade = 5
        elif 'IV' in romano:
            unidade = 4
        elif 'III' in romano and 'V' not in romano:
            unidade = 3
        elif 'II' in romano and 'V' not in romano:
            unidade = 2
        elif 'I' in romano and 'V' not in romano:
            unidade = 1
        print(f'O numero {romano} é representado por {milhar + centena + dezena + unidade}')
    resposta = str(input("Deseja continuar? [s/n]")).lower()
print('-'*10)
print('Até mais!')
print('-'*10)
