def calculate_marks(m1,m2,m3):
    tot = m1+m2+m3
    return tot
name = input("Enter your name: ")
marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))
total =calculate_marks(m3=marks1,m1=marks2,m2=marks3)
print(f'Your total marks are: {total}')




