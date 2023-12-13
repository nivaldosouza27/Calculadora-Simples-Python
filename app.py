import os

while True:
    print("Calculadora Python")
    print('\n')
    print("0: Soma")
    print("1: Subtração")
    print("2: Multiplicação")
    print("3: Divisão")
    print("4: Exponenciação")
    print('\n')
    operator = input('Escolha uma das operações acima: ')

    if int(operator) == 0:
        print("Operação Escolhida foi Soma")
        print('\n')

        number_01 = input('Escolha o primeiro numero: ')
        number_02 = input('Escolha o segundo numero: ')
        result = float(number_01) + float(number_02)

        print(f'Seu resultado é {result}')
        print('\n')

        other_operation = input('Deseja fazer outra operação? S(SIM) / N(Não): ')

        if other_operation == 'S' or other_operation == 's':
            os.system('cls')
            continue
        else:
            print('Final do programa')
            break

    elif int(operator) == 1:
        print("Operação Escolhida foi Subtração")
        print('\n')

        number_01 = input('Escolha o primeiro numero: ')
        number_02 = input('Escolha o segundo numero: ')
        result = float(number_01) - float(number_02)

        print(f'Seu resultado é {result}')
        print('\n')

        other_operation = input('Deseja fazer outra operação? S(SIM) / N(Não): ')

        if other_operation == 'S' or other_operation == 's':
            os.system('cls')
            continue
        else:
            print('Final do programa')
            break

    elif int(operator) == 2:
        print("Operação Escolhida foi Multiplicação")
        print('\n')

        number_01 = input('Escolha o primeiro numero: ')
        number_02 = input('Escolha o segundo numero: ')
        result = float(number_01) * float(number_02)

        print(f'Seu resultado é {result}')
        print('\n')

        other_operation = input('Deseja fazer outra operação? S(SIM) / N(Não): ')

        if other_operation == 'S' or other_operation == 's':
            os.system('cls')
            continue
        else:
            print('Final do programa')
            break

    elif int(operator) == 3:
        print("Operação Escolhida foi Divisão")
        print('\n')

        number_01 = input('Escolha o primeiro numero: ')
        number_02 = input('Escolha o segundo numero: ')
        result = float(number_01) / float(number_02)

        print(f'Seu resultado é {result}')
        print('\n')

        other_operation = input('Deseja fazer outra operação? S(SIM) / N(Não): ')

        if other_operation == 'S' or other_operation == 's':
            os.system('cls')
            continue
        else:
            print('Final do programa')
            break

    elif int(operator) == 4:
        print("Operação Escolhida foi Exponenciação")
        print('\n')

        number_01 = input('Escolha o primeiro numero: ')
        number_02 = input('Escolha o segundo numero: ')
        result = float(number_01) ** float(number_02)

        print(f'Seu resultado é {result}')
        print('\n')

        other_operation = input('Deseja fazer outra operação? S(SIM) / N(Não): ')

        if other_operation == 'S' or other_operation == 's':
            os.system('cls')
            continue
        else:
            print('Final do programa')
            break

    else:
        print('Operação Invalida')
        print('\n')
        raise ValueError
