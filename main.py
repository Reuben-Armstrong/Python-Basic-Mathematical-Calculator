# Basic Mathematical Calculator


# Title
print('------------------------------------------------------------------------------')
print(' Basic Calculator')
print('------------------------------------------------------------------------------')
print(' What would you like to do?:')
print('------------------------------------------------------------------------------')
print(' [1] Addition       (+)')
print(' [2] Subtraction    (-)')
print(' [3] Multiplication (*)')
print(' [4] Division       (/)')
print('------------------------------------------------------------------------------')
print('')

# Choose what will happen
while True:
    function_choice = input('What Function would you like to use?: ')

    # Addition
    if function_choice == '1':
        while True:
            try:
                print('')
                operator = '+'
                num1 = float(input('What is the first number?: '))
                num2 = float(input('What is the second number?: '))

                answer = num1 + num2
                break

            except ValueError:
                print('That is not a valid number! Try again.')

    # Subtraction
    elif function_choice == '2':
        while True:
            try:
                print('')
                operator = '-'
                num1 = float(input('What is the first number?: '))
                num2 = float(input('What is the second number?: '))

                answer = num1 - num2
                break

            except ValueError:
                print('That is not a valid number! Try again.')

    # Multiplication
    elif function_choice == '3':
        while True:
            try:
                print('')
                operator = '*'
                num1 = float(input('What is the first number?: '))
                num2 = float(input('What is the second number?: '))

                answer = num1 * num2
                break

            except ValueError:
                print('That is not a valid number! Try again.')
            
    # Division
    elif function_choice == '4':
        while True:
            try:
                print('')
                operator = '/'
                num1 = float(input('What is the first number?: '))
                num2 = float(input('What is the second number?: '))

                if num2 == 0:
                    print('You can not divide by 0.')
                    continue

                answer = num1 / num2
                break

            except ValueError:
                print('That is not a valid number! Try again.')

    # If user does not input a valid option
    else:
        print('Please enter either  1 or 2 or 3 or 4 for the chosen function.')
        continue

    break

# Output
print('')
print('------------------------------------------------------------------------------')
print(f' {num1} {operator} {num2} = {round(answer, 3)} Rounded to 3 D.P.')
print('------------------------------------------------------------------------------')
print('')
input('Press the Enter Key to Exit...')