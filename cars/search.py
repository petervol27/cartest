def search_car(cars):
    while True:
        search_results = []
        choice = input(
            "to search by make or model enter 0, by year 1,2 by VIN and by problems 3: "
        )
        if choice == "0":
            search_term = input("enter your search query: ")
            for car in cars:
                if (
                    search_term in car["make"].lower()
                    or search_term in car["model"].lower()
                ):
                    car_result = f"Car ID: {car['id']}, VIN:{car['VIN']} {car['make']} {car['model']}"
                    search_results.append(car_result)
        elif choice == "1":
            try:
                search_term = int(input("enter the year you are searching for: "))
                found = False
                for car in cars:
                    if search_term <= car["year"]:
                        car_result = f"Car ID: {car['id']},VIN:{car['VIN']} {car['make']} {car['model']} from {car['year']}"
                        search_results.append(car_result)
                        found = True
                if not found:
                    print("no cars from that year, sorry!")
            except Exception as ex:
                print(ex, "please enter valid input!")
        elif choice == "2":
            search_term = input("enter VIN number: ")
            found = False
            for car in cars:
                if search_term in car["VIN"]:
                    car_result = f"Car ID: {car['id']},VIN:{car['VIN']} {car['make']} {car['model']} from {car['year']}"
                    search_results.append(car_result)
                    found = True
            if not found:
                print("no cars with that VIN number")
        elif choice == "3":
            found = False
            search_term = input("enter the problem you are looking for: ")
            for car in cars:
                for problem in car["problems"]:
                    if search_term == problem:
                        car_result = f"Car ID: {car['id']}, VIN:{car['VIN']} {car['make']} {car['model']} with the {problem} problem "
                        search_results.append(car_result)
                        found = True
                        break
            if not found:
                print("no cars with that problem!")
        if search_results:
            for result in search_results:
                print(f"we found this car: {result}")
            break
