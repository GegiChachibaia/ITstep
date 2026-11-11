#ამოცანა 1
for i in range (1,10):
    print(f"{i} squared = {i*i}")

for j in range(10,0,-1):
    print(j)
print("Go!")

sum1 = 0
for k in range(1,100):
    if k % 2 ==0:
        sum1+=k
    else:continue
print(sum1)

#ამოცანა 2
inp = input("Enter text: ")
inp = inp.lower()
count = 0
for i in inp:
    if i in ("a","e","i","o","u"):
        count+=1
    else:continue
print(f"Vowels: {count}")

#ამოცანა 3
sum2 = 0
count1 = 0
while True:
    inp1 = input("Enter a number: ")
    if inp1 == "stop":
        break
    else:
        try:
            inp1 = int(inp1)
            if inp1 < 0:
                print("Negative numbers are not allowed")
            else:
                sum2 = sum2 + inp1
                count1 += 1
        except ValueError:
            print("Please enter a valid number")
print(f"Sum: {sum2}")
print(f"Count: {count1}")

#ამოცანა 4
triangle = int(input("n = "))
for a in range(0,triangle+1):
    for b in range(0,a):
        print("*" , end ="")
    print()
print("\n")

triangle2 = int(input("m = "))
for p in range (triangle2,0,-1):
    for q in range(0,p):
        print("*" , end="")
    print()

