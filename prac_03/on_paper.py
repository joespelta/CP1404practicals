minimum_length = 6

password = input("Enter Password: ")
while len(password) < minimum_length:
    print("Invalid Password")
    password = input("Enter Password: ")
print(len(password) * "*")
