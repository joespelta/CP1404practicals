from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


MENU = """- (C)hoose Taxi
- (D)rive
- (Q)uit"""


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare_cost = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis Available:")
            taxi_counter = -1
            for taxi in taxis:
                taxi_counter += 1
                print(f"{taxi_counter} - {taxi}")
            taxi_choice = get_valid_taxi_choice(taxis, "Choose Taxi Number: ")
            current_taxi = taxis[taxi_choice]
            print(current_taxi)
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == "D":
            if current_taxi:
                distance_driven = int(input("How far would like to travel? "))
                if current_taxi.fuel >= distance_driven:
                    current_taxi.drive(distance_driven)
                    taxi_fare = current_taxi.get_fare()
                    total_fare_cost += taxi_fare
                    print(current_taxi)
                    print(f"${taxi_fare:.2f}")
                    print(MENU)
                    choice = input(">>> ").upper()
                else:
                    print("This taxi does not have enough fuel to travel this distance")
                    print(MENU)
                    choice = input(">>> ").upper()
            else:
                print("You have not chosen a car yet!")
                print(MENU)
                choice = input(">>> ").upper()
        else:
            print("Invalid Choice")
            print(MENU)
            choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_fare_cost:.2f}")
    print("Taxis are now:")
    taxi_counter = -1
    for taxi in taxis:
        taxi_counter += 1
        print(f"{taxi_counter} - {taxi}")


def get_valid_taxi_choice(taxis, prompt):
    choice = int(input(prompt))
    if choice < 0 or choice > len(taxis):
        print("Invalid Taxi choice")
    else:
        return choice


main()
