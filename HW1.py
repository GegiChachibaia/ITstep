# ამოცანა 1

age = 10
height = 1.85
name = "Gegi"
logic = True
print(type(age))
print(type(height))
print(type(name))
print(type(logic))

#ამოცანა 2

a = float(input("Please enter number 1:\n"))
b = float(input("Please enter number 2:\n"))
print("sum is : ", a+b)
print("difference is: " ,a-b)
print("product is: ", a*b)
print("quotient is: " ,a/b)
print("integer quotient is : ", a//b)
print("remainder is: " ,a%b)
print("power is: " ,a**b)

#ამოცანა 3
name1 = str(input("Please enter your name:\n"))
surname = str(input("Please enter your surname:\n"))
fullname = name1 + ' ' + surname
print("full name is:", fullname)
print(fullname.upper())
print(fullname.lower())
print(fullname.capitalize())

#ამოცანა 4

print("ლაშა","გიორგი" , sep="-")
print(1, 2, 3, 4, 5, sep="***")
print(10, "ასაკი", False, sep="\t")

print("ეს არის პირველი სტრიქონი", end=" ")
print("ეს გაგრძელდება იმავე ხაზზე!", end="!\n")

print("იტვირთება", end="...")
print("მზადაა!")
#ამოცანა 5

age1 = 22
height1 = 185
is_student = True

print(age1, "==", 22, "=", age1 == 22)
print(age1, "!=", 18, "=", age1 != 18)
print(age1, ">", 18, "=", age1 > 18)
print(age1, "<", 15, "=", age1 < 15)
print(height1, ">=", 180, "=", height1 >= 180)
print(height1, "<=", 175, "=", height1 <= 175)


#ამოცანა 6
name2 = input("შეიყვანეთ თქვენი სახელი: ")
age_input = input("შეიყვანეთ თქვენი ასაკი: ")
height_input = input("შეიყვანეთ თქვენი სიმაღლე (მაგ. 1.75): ")


age2 = int(age_input)
height2 = float(height_input)



print("გამარჯობა, "+ name2)
print("თქვენ ხართ " ,age2 , "წლის და თქვენი სიმაღლეა ", height2 , "მეტრი.")


