from cars.variables import problems


def calculate_total(cars):
    car_amount = len(cars)
    profit = 0
    problems_list = []
    for car in cars:
        for problem in car["problems"]:
            problems_list.append(problem)
    for problem in problems_list:
        for check in problems:
            if problem == check["name"]:
                profit += check["price"]
    print(f"we have {car_amount} cars in the garage with total profit of: {profit}")
