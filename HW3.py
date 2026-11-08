#ამოცანა 1
k = int(input("Enter number:\n"))
if k % 2 == 0:
    print(f'{k} is even')
else:
    print(f'{k} is odd')

#ამოცანა 2
age = int(input("Enter age:\n"))
if age < 0:
    print('invalid age')
elif age <= 12:
    print('Child')
elif age <= 17:
    print('Teenager')
elif age <= 64:
    print('Adult')
else:
    print('Senior')
#ამოცანა 3
grade = int(input("Enter your grade:\n"))
if grade < 0 or grade > 100:
    print("Invalid number")
elif grade < 50:
    print("F")
elif grade < 60:
    print("E")
elif grade < 70:
    print("D")
elif grade < 80:
    print("C")
elif grade < 90:
    print("B")
else:
    print("A")
#ამოცანა 4
answer = input("Do you like Python? (yes/no)\n")
answer = answer.strip().lower()
if answer == "yes":
    print("Great!")
elif answer == "no":
    print("Maybe you will like it later")
else:
    print("Please answer yes or no")

#ამოცანა 5
a = float(input("Please enter number 1:\n"))
operation = input("Please enter an operation (+,-,*,/):\n")
b = float(input("Please enter number 2:\n"))
if operation not in ("+","-","*","/"):
    print("Unknown operator")
elif operation == "+":
    print(f"{a} + {b} = {a+b}")
elif operation == "-":
    print(f"{a} - {b} = {a-b}")
elif operation == "*":
    print(f"{a} * {b} = {a*b}")
else:
    print(f"{a} / {b} = {a/b}")
