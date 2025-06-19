"""
Simple calculator
"""
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
choice = input('1.Add 2.Subtract 3.Multiply 4.Divide 5.Quit: ')
match choice:
    case 1:
       print(num1+num2)
    case 2.0:
        print(num1-num2)
    case '3':
        print(num1*num2)
    case 4:
        print(f'{(num1/num2):.2f}')
    case _:
        print('invalid choice')
print('Done')
# if choice == 1:
#     result = num1 + num2
#     print(result)
# elif choice == 2:
#     result = num1 - num2
#     print(result)
# elif choice == 3:
#     result = num1 * num2
#     print(result)
# elif choice == 4:
#     result = num1 / num2
#     print(result)
# else:
#     print('Invalid input')
