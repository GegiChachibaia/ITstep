#ამოცანა 1
def print_ticket(passenger,destination,seat_class):
    print('--- TICKET ---')
    print(f'Passenger: {passenger}')
    print(f'Destination: {destination}')
    print(f'Class: {seat_class}')

print_ticket('Nika' , 'Tbilisi','Economy')
print_ticket(passenger='Mari', destination='Kutaisi',seat_class='Business')
print_ticket('Luka','Batumi', seat_class='Economy')

#ამოცანა 2
def celsius_to_fahrenheit(cels):
    return cels*9/5 + 32
a = celsius_to_fahrenheit(0)
b = celsius_to_fahrenheit(37)
c = celsius_to_fahrenheit(100)
print(f'{0}C = {a}F')
print(f'{37}C = {b}F')
print(f'{100}C = {c}F')

def is_warm(celsius, limit = 20):
    return True if celsius > limit else False

print(is_warm(25))
print(is_warm(20,30))
print(is_warm(limit=10,celsius=15))

#ამოცანა 3
def analyze_numbers(numbers:list):
    sum_num = 0
    for i in numbers:
        sum_num += i

    k = sorted(numbers)
    return k[0] , k[-1] , sum_num / len(numbers)

lowest , highest , average = analyze_numbers([12, 7, 25, 3, 18])
print(f'Min: {lowest}, Max: {highest}, Average: {average}')
number = analyze_numbers([12,7,25,3,18])
print(number)

#ამოცანა 4
def add_student(name, group = None):
    if group is None:
        group = []
    if name not in group:
        group.append(name)

    return group

group_a = add_student('Ana')
group_b = add_student('Nika')
group_a = add_student('Mari', group_a)
group_a = add_student('Ana', group_a)

print(group_a)
print(group_b)

#ამოცანა 5
def check_password(password):
    if len(password) < 6:
        return 'Too short'
    if password.isdigit():
        return 'Weak'
    has_digit = False
    has_letter = False

    for a in password:
        if a.isdigit():
            has_digit = True
        if a.isalpha():
            has_letter = True

    if not has_letter or not has_digit:
        return 'Medium'
    return 'Strong'

passwords = ['abc', '1234567', 'qwerty', 'python3', 'Tbilisi2024']
for password in passwords:
    print(f'{password} -> {check_password(password)}')


