"""Armstrong number"""
num = int(input('Enter a number: '))
temp = num
summ = 0
while num > 0:
    rem = num % 10
    summ = summ+(rem**3)
    num = num//10
if summ == temp:
    print(f'{temp} is an armstrong number')
else:
    print(f'{temp} is not an armstrong number')