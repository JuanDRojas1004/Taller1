from addition import add
from substraction import sub
from multiplication import mult
from division import div
from exponentiation import exp
from modulation import mod




def game():
    score = 0
    while True:
        print('====== Menu ======'
              '\n1. Add'
              '\n2. Sub'
              '\n3. Mul'
              '\n4. Div'
              '\n5. Exp'
              '\n6. Mod'
              '\n0. Exit'
                )
        option = int (input('\nChoise an option: '))

        if option == 0:
            break
        
        num_1 = int (input('Enter first number:'))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter you answer: '))

        if option == 1:
            result = add(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')

        elif option == 2:
            result = sub(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')

        elif option == 3:
            result = mult(num_1, num_2)
            if result == answer:
                score += 2
                print('Correct!!')
            else:
                print('Incorrect')
        
        elif option == 4:
            result = div(num_1, num_2)
            if result == answer:
                score += 2
                print('Correct!!')
            else:
                print('Incorrect')

        elif option == 5:
            result = exp(num_1, num_2)
            if result == answer:
                score += 4
                print('Correct!!')
            else:
                print('Incorrect')

        elif option == 6:
            result = mod(num_1, num_2)
            if result == answer:
                score += 4
                print('Correct!!')
            else:
                print('Incorrect')
    print(f'======== Game Over ========'
          f'\nYou score is {score}'
          '\nKeep going!')
game()