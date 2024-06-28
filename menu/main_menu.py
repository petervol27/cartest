from cars.actions import cars_list, add_car, delete_car
from cars.calculation import calculate_total
from cars.search import search_car
from storage.save_load import load, save


def main_menu():
    print("Welcome to our garage!")
    cars = load()
    while True:
        calculate_total(cars)
        print("1 - Cars List")
        print("2 - Add Car")
        print("3 - Delete Car")
        print("4 - Search Cars")
        print("5 - Exit")
        selection = input("What would you like to do? enter number between 0 and 5: ")
        if selection == "1":
            cars_list(cars)
        elif selection == "2":
            add_car(cars)
        elif selection == "3":
            delete_car(cars)
        elif selection == "4":
            search_car(cars)
        elif selection == "5":
            save(cars)
            print("Thank you for visiting hope to see you again!")
            break
        else:
            print("invalid input! enter number between 1 and 5")
