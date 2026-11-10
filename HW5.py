# ამოცანა 1
n = 2
m = 1
while n <= 50:
    print(n)
    n += 2
# ბევრი წვალების გარეშე

while m <= 50:
    if m % 2==0:
        print(m)
        m+=1
    else:
        m+=1
#წვალებით

#ამოცანა 2
sum = 0
k = int(input("Enter N: "))
while k > 0:
    sum = sum + k
    k -= 1
print(f"Sum: {sum}")

#ამოცანა 3
product = 1
a = int(input("Enter n: "))
b = a
if a < 0:
    print("Please enter a non-negative number")
elif a == 0:
    print("0! = 1")
else:
    while a > 0:
        product = product * a
        a -= 1
    print(f"{b}! = {product}")

#ამოცანა 4
count = 0
total_sum = 0

while True:
    number = float(input("Enter a number: "))
    if number == 0:
        break

    total_sum += number
    count += 1

print(f"Count: {count}")
print(f"Sum: {total_sum}")

if count > 0:
    average = total_sum / count
    print(f"Average: {average}")
else:
    print("Average: 0")

#ამოცანა 5

secret = 9
count1 = 0
while count1 < 5:
    guess = int(input("Guess: "))
    if guess < secret:
        print("Too low")
        count1 +=1
    elif guess > secret:
        print("Too high")
        count1 +=1
    else:
        print("You win!")
        break
print("Game Over!")