"""
CP1404/CP5632 Practical
Data file -> lists program
"""

subject_data_lists = []
FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_subject_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_data_lists.append(parts)
    input_file.close()
    return subject_data_lists


def print_subject_data(data):
    for subject_data in data:
        print(f"{subject_data[0]} is taught by {subject_data[1]} and has {subject_data[2]} students")


main()
