"""n = int(input('Enter a number: '))
summ= 0
for i in range(1,n+1):
    summ += i**2
print(f'The sum of {n} natural numbers is {summ}"""
sample = {1:10,2:20,3:30}
# for ele in sample:
#     print(ele,'\t',sample[ele]**2)
for key,value in sample.items():
    print(f'{key} is {value}')