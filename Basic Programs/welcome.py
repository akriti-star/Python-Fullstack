# print( 'welcome to my series''')
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
print(f'The sum of {num1} and {num2} is {num1 + num2}')
print(f'The diff of {num1} and {num2} is {num1 - num2}')
print(f'The product of {num1} and {num2} is {num1 * num2}')
print(f'The division of {num1} and {num2} is {num1 // num2}')
res= f'{num1} is a max' if num1 > num2 else f'{num2} is a max'
print(res)

# if num1 > num2:
#     print(f'max num is {num1}')
# else:
#     print(f'max num is {num2}')