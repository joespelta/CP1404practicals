import random

"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

"""Fixed Code"""


def main():
    score = float(input("Enter score: "))
    # score = random.randint(0, 100)
    result = get_result(score)
    print(score, result)


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
