# #ამოცანა 1
shopping = ['milk','bread','eggs']
drinks = ['tea','coffee']
shopping.append('cheese')
shopping.insert(0,'apple')
shopping[-1] = 'butter'
shopping.extend(drinks)
shopping.remove('bread')
print(shopping[1])
shopping.pop(1)
print(shopping)


#ამოცანა 2

scores = [85, 92, 78, 92, 65, 88, 92]
scores1 = scores[:]
count = 0
ind = 0
for score in scores1:
    if score == 92:
        count+=1
    elif score == 78:
       ind = scores1.index(score)
    else:continue

asc_scores = sorted(scores1)
desc_scores = sorted(scores1,reverse=True)


print(f"Count of 92: {count}")
print(f"Index of 78: {ind}")
print(f"Ascending: {asc_scores}")
print(f"Descending: {desc_scores}")
print(f"Highest: {desc_scores[0]}, Lowest: {asc_scores[0]}")
print(f"Original: {scores}")


#ამოცანა 3

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_count = 0
for row in matrix:
    row_count += 1
print(row_count)
print(matrix[-1])
print(matrix[1][2])
print(matrix[-2][-1])
print(matrix[-1][-3])
matrix[1][1] = 50
print(matrix)
#ამოცანა 4

numbers = []
steps = 0
while True:
    inp = input("Enter a number: ")
    if inp == 'stop':
        break
    else:
        try:
            inp = int(inp)
            numbers.append(inp)
            steps += 1
        except ValueError:
            print("Enter either a number or 'stop' to stop the code")
        except Exception as e:
            print(e)



print(steps)
print(numbers)
try:
    print(f"First: {numbers[0]}, Last: {numbers[-1]}")
except IndexError:
    print("No values were provided")
except Exception as e:
    print(e)

if len(numbers) > 0:   #ეს იმიტომ დავწერე ,რომ ცარიელი ლისტი არ დამიპრინტოს არ მომწონდა როგორც ჩანდა :)
    print(f"Descending: {sorted(numbers,reverse=True)}")