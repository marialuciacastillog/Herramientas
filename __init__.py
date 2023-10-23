from operations import add, rest, multiply, divide, potencia, modulo
def game():
    score = 0
    while True:
        print('======== Menu ========'
            '\n1. Add'
            '\n2. Subtract'
            '\n3. Multiplication'
            '\n4. Division'
            '\n5. Power'
            '\n6. Module'
              
            '\n0. Exit')
        
        option = int(input('\nChoice an option: '))
        if option == 0:
            break
        num_1 = input('Enter first number: ')
        num_2 = input('Enter second number: ')
        answer = int(input('Enter you answer: '))
        
        if option == 1:
            result = add(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')  
            else:
                print('Incorrect')
        
        elif option ==2: 
            result= rest(num_1, num_2)
            if result== answer: 
                score +=1
                print('Correct!!')  
            else:
                print('Incorrect')
                
        elif option ==3:
            result= multiply(num_1, num_2)
            if result== answer: 
                score +=1
                print('Correct!!')  
            else:
                print('Incorrect')
        
        elif option ==4:
            result= divide(num_1, num_2)
            if result== answer: 
                score +=1
                print('Correct!!')  
            else:
                print('Incorrect')
        
        elif option ==5:
            result= potencia(num_1, num_2)
            if result== answer: 
                score +=1
                print('Correct!!')  
            else:
                print('Incorrect')
        
        elif option ==6:
            result= modulo(num_1, num_2)
            if result== answer: 
                score +=1
                print('Correct!!')  
            else:
                print('Incorrect')
        
        
        
                    
    print(f'======== Game Over ========'
          f'\nYou score is {score}'
          '\nKeep going!')

game()
