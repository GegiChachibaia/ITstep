# #ამოცანა 1
numbers = [4, 8, 15, 8, 16, 23, 4, 42, 15, 8]
unique_set = set()
for i in range(len(numbers)):
    unique_set.add(numbers[i])
print(list(unique_set))
print(len(unique_set))
print(f'is 23 in the set?\n{True if 23 in unique_set else False}')


#ამოცანა 2
ana = {'python', 'java', 'c', 'sql'}
nika = {'python', 'javascript', 'sql', 'go'}

print(ana.union(nika))
print(ana.intersection(nika))
print(ana.difference(nika))
#ამოცანა 3

votes = ['Ana', 'Nika', 'Ana', 'Mari', 'Nika', 'Ana', 'Mari', 'Ana']
result = {}
for vote in votes:
    if vote in result:
        result[vote] += 1
    else:
        result[vote] = 1
for name , count in result.items():
    print(f'{name}: {count}')
#ამოცანა 4
total_price = 0
inventory = {
    'laptop': {'price': 2500, 'quantity': 5},
    'mouse': {'price': 40, 'quantity': 0},
    'keyboard': {'price': 120, 'quantity': 12},
    'monitor': {'price': 800, 'quantity': 0},
}
print('ამოწურული პროდუქტები: ')
for item, details in inventory.items():
    total_price += details['quantity'] * details['price']

    if details['quantity'] == 0:
        print(f'-{item}')
print(f'საწყობის საერთო ღირებულება: {total_price}')

user_item = input('შეიყვანეთ პროდუქტის დასახელება: ').strip().lower()

if user_item in inventory:
    try:
        user_quantity = int(input('შეიყვანეთ სასურველი რაოდენობა: '))
        if user_quantity<=0:
            print('რაოდენობა უნდა იყოს 0-ზე მეტი')
        elif inventory[user_item]['quantity'] >= user_quantity:
            inventory[user_item]['quantity'] -= user_quantity
            purchase_cost = inventory[user_item]['price'] * user_quantity
            print(f'შეძენის ღირებულებაა: {purchase_cost}')
            print(f'დარჩენილი მარაგი: {user_item} - {inventory[user_item]['quantity']}')
        else:
            print('მარაგი არასაკმარისია')
    except ValueError:
        print('გთხოვთ შეიყვანოთ მთელი რიცხვი')
else:
    print('პროდუქტი ვერ მოიძებნა')

#ამოცანა 5
words = ['python', 'java', 'ai', 'sql', 'go', 'python']

print([i**2 for i in range(11)])
print([{word:len(word) for word in words}])
print([set(word[0] for word in words)])