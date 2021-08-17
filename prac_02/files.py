NAME_FILE = 'name.txt'
NUMBERS_FILE = 'numbers.txt'
# 1)

name = input("Enter Name: ")
file_data = open(NAME_FILE, 'w')
print(name, file=file_data)
file_data.close()

# 2)

file_in = open(NAME_FILE, 'r')
name = file_in.read()
print(f"Your name is {name}")
file_in.close()

# 3)

file_in = open(NUMBERS_FILE, 'r')
first_number = file_in.readline()
second_number = file_in.readline()
file_in.close()
result = int(first_number) + int(second_number)
print(result)

# 4)

result = 0
file_in = open(NUMBERS_FILE, 'r')
for number in file_in:
    result += int(number)
file_in.close()
print(result)

