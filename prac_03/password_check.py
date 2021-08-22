MINIMUM_LENGTH = 6


def main():
    password = get_password("Enter Password: ")
    print_asterisks(password)


def get_password(prompt):
    password = input(prompt)
    while len(password) < MINIMUM_LENGTH:
        print("Invalid Password")
        password = input("Enter Password: ")
    return password


def print_asterisks(password):
    print(len(password) * "*")


main()
