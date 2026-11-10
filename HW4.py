#ამოცანა 1
age = int(input("Enter age:\n"))
money = int(input("Enter money:\n"))
if age >= 12 and money >= 15:
    print("Enjoy the movie")
else:
    print("Access denied")

#ამოცანა 2
year = int(input("Enter year:\n"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

#ამოცანა 3
user_pin = int(input("Enter PIN: "))
amount = int(input("Enter amount: "))
pin = 1234
balance = 500
if user_pin != pin:
    print("Wrong PIN!")
else:
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Not enough money")
    else:
        print(f"Take your money: {amount}\nNew balance: {balance-amount}")

#ამოცანა 4
'''
Enter name: john
Enter age: 20
Enter a number to divide 100 by: 5
100 / 5 = 20.0
Traceback (most recent call last):
  File "/Users/gegi/ITstep/HW4.py", line 37, in <module>
    print('Hello, ' + name + '! Next year you will be ' + (age + 1) + ' years old.')
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~
TypeError: can only concatenate str (not "int") to str
ეს დამიბრუნა (john ,20 ,5)

Enter name: john
Enter age: abc
Traceback (most recent call last):
  File "/Users/gegi/ITstep/HW4.py", line 33, in <module>
    age = int(input('Enter age: '))
ValueError: invalid literal for int() with base 10: 'abc'

ეს დამიბრუნა (john,abc,5)

Enter name: john
Enter age: 20
Enter a number to divide 100 by: 0
Traceback (most recent call last):
  File "/Users/gegi/ITstep/HW4.py", line 36, in <module>
    print('100 /', number, '=', 100 / number)
                                ~~~~^~~~~~~~
ZeroDivisionError: division by zero
ეს დამიბრუნა (john,20,0)
'''
try:
    user_name = input('Enter name: ')
    user_age = int(input('Enter age: '))
    user_number = int(input('Enter a number to divide 100 by: '))

    print(f"100 / {user_number} = {100 / user_number}")
    print(f"Hello, {user_name}! Next year you will be {user_age+1} years old.")

except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError:
    print("Cannot join text and number")
except Exception as e:
    print(e)

'''except TypeError:
    print("Cannot join text and number")
    ეს ნაწილი არ მჭირდება იმიტორო f სტრინგით მაქვს დაწერილი მაგრამ მაინც დავტოვე ამოცანის მოთხოვნების გამო.'''