from cars.variables import problems, problems_names


def cars_list(cars):
    for car in cars:
        problems_string = ""
        for problem in car["problems"]:
            if problem == car["problems"][-1]:
                problems_string += f"{problem}."
            else:
                problems_string += f"{problem}, "
        print(
            f"car ID: {car['id']} {car['make']} {car['model']} {car['year']} VIN: {car['VIN']} has problems in: {problems_string}"
        )


def add_car(cars):
    while True:
        finished_adding = False
        try:
            new_car = {
                "id": str(int(cars[-1]["id"]) + 1),
                "VIN": input("enter VIN number must be 17 characters: "),
                "make": input("enter car make: ").capitalize(),
                "model": input("enter car model: ").capitalize(),
                "year": int(input("enter car year: ")),
            }
            if len(new_car["VIN"]) != 17:
                print("VIN number must be 17 characters!")
            else:
                new_car_problems = []
                while True:
                    new_problem = input(
                        "enter problem name or 0 to finish adding problems: "
                    )
                    if new_problem == "0":
                        break
                    elif new_problem in problems_names:
                        new_car_problems.append(new_problem)
                    else:
                        print("invalid input!")
                new_car["problems"] = new_car_problems
                problems_price = 0
                for problem in problems:
                    if problem["name"] in new_car_problems:
                        problems_price += problem["price"]
                while True:
                    fix_or_not = input(
                        f"The price to fix the problems would be: {problems_price} would you like to put the car in the garage? enter yes or no "
                    )
                    if fix_or_not == "yes":
                        cars.append(new_car)
                        print("no problem we will have it fixed up in a jiffy")
                        finished_adding = True
                        break
                    elif fix_or_not == "no":
                        print(
                            "no problem if you change your mind we are always here for you"
                        )
                        finished_adding = True
                        break
                    else:
                        print("invalid input")
        except Exception as ex:
            print(ex, "please enter valid input!")
        if finished_adding:
            break


def delete_car(cars):
    car_fixed = False
    while True:
        cars_list(cars)
        choice = input("enter car ID to delete: or 0 to exit ")
        if choice == "0":
            break
        for car in cars:
            if choice == car["id"]:
                cars.remove(car)
                car_fixed = True

        if car_fixed:
            print("We fixed her up for you! here you go")
            break
        else:
            print("no car like that here is the list again:")
