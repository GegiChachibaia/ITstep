# ამოცანა 1

word = 'programming'
print(word[0])
print(word[-1])
print(word[-4])
print(word[:4])
print(word[::2])
print(word[::-1])

# ამოცანა 2

user_email = str(input("Please enter your email:\n"))
print(user_email[0:user_email.index("@")])
print(user_email[user_email.index("@"):])
print(user_email[user_email.index("@")+1:user_email.index(".")])
# ამოცანა 3

user_phone = input("Please enter your phone number:\n")
print(user_phone.replace(' ', '').replace('-',''))
# ამოცანა 4
user_title = input("Please enter a Title for your blog:\n")
print("-".join(user_title.lower().split()))
# ამოცანა 5
user_name = input("Please enter your name:\n")
user_age = input("Please enter your age:\n")
user_city = input("Please enter your city:\n")
user_language = input("Please enter your favourite programming language:\n")
print("=========================")
print(f"Name: {user_name.title()}")
print(f"Age: {user_age}")
print(f"City: {user_city.title()}")
print(f"Favourite language: {user_language.upper()}")
print("=========================")
# ამოცანა 6