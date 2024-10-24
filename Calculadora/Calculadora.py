import os
def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Adição')

    num_1 = float(input('coloque um numero:'))
    num_2 = float(input('coloque outro numero'))
    ans = num_1 + num_2
    values_entered = 2
    print(f'resultado atual: {ans}')

    continue_calc = 'y'
    while continue_calc.lower() == 'y':
        continue_calc = input('insira mais (y/n):')
        while continue_calc.lower() not in ['y', 'n']:
            print('insira \'y\' ou \'n\'')
            continue_calc = input('coloque mais (y/n):')

        if continue_calc.lower() == 'n':
            break

        num = float(input('coloque outro numero: '))
        ans += num 
        print(f'resultado atual: {ans}')
        values_entered += 1

    return [ans, values_entered]

def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('subtraction')


    num_1 = float(input('coloque um numero:'))
    num_2 = float(input('coloque outro numero'))
    ans = num_1 - num_2
    values_entered = 2
    print(f'resultado atual: {ans}')

    continue_calc = 'y'
    while continue_calc.lower() == 'y':
        continue_calc = input('insira mais (y/n):')
        while continue_calc.lower() not in ['y', 'n']:
            print('insira \'y\' ou \'n\'')
            continue_calc = input('coloque mais(y/n):')

        if continue_calc.lower() == 'n':
            break

        num = float(input('coloque outro numero: '))
        ans -= num 
        print(f'resultado atual: {ans}')
        values_entered += 1

    return [ans, values_entered]

def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('multiplication')

    num_1 = float(input('coloque um numero:'))
    num_2 = float(input('coloque outro numero'))
    ans = num_1 * num_2
    values_entered = 2
    print(f'resultado atual: {ans}')

    continue_calc = 'y'
    while continue_calc.lower() == 'y':
        continue_calc = (input('insira mais (y/n):'))
        while continue_calc.lower() not in ['y', 'n']:
            print('insira \'y\' ou \'n\'')
            continue_calc = (input('coloque mais(y/n):'))

        if continue_calc.lower() == 'n':
            break

        num = float(input('coloque outro numero: '))
        ans *= num 
        print(f'resultado atual: {ans}')
        values_entered += 1
    return [ans, values_entered]

def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('division')

    num_1 = float(input('coloque um numero:'))
    num_2 = float(input('coloque outro numero'))

    if num_2 ==0:
        print("Erro: Divisão por zero não é permitida")
        return [None, 0]
    
    ans = num_1 / num_2
    values_entered = 2
    print(f'resultado atual: {ans}')


    continue_calc = 'y'
    while continue_calc.lower() == 'y':
        continue_calc = input('insira mais (y/n):')
        while continue_calc.lower() not in ['y', 'n']:
            print('insira \'y\' ou \'n\'')
            continue_calc = input('coloque mais(y/n):')

        if continue_calc.lower() == 'n':
            break

        num = float(input('coloque outro numero: '))
        ans == 0 
        print("Erro: Divisão por zero não é permitida")
    else:
        ans /= num
        print(f'resultado atual: {ans}')
        values_entered += 1

    return [ans, values_entered]

def calculator():
    quit = False
    while not quit:
        print('Calculadora simples em Python')
        print('Coloque a letra \'a\' para adição')
        print('Coloque a letra \'s\' para subtrair')
        print('Coloque a letra \'m\' para multiplicar')
        print('Coloque a letra \'d\' para dividir')
        print('Coloque a letra \'q\' para quit')

        choice = input('Escolha:').lower()

        if choice == 'q':
            quit = True
        elif choice == 'a':
            results = addition()
            print('Ans = ', results[0], 'total inputs:', results[1])
        elif choice == 's':
            results = subtraction()
            print('Ans = ', results[0], 'total inputs:', results[1])
        elif choice == 'm':
            results = multiplication()
            print('Ans = ', results[0], 'total inputs:', results[1])
        elif choice == 'd':
            results = division()
            print('Ans = ', results[0], 'total inputs:', results[1])
        else:
            print('Desculpa, escolha invalido')

if __name__ == '__main__':
    calculator()