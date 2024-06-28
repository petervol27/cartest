import json

FILE_PATH = "storage/cars.json"


def load():
    try:
        with open(FILE_PATH, "r") as file:
            cars = json.load(file)
            return cars
    except:
        cars = [
            {
                "id": "1",
                "VIN": "1HGCM82633A123456",
                "make": "Ford",
                "model": "Mustang",
                "year": 2021,
                "problems": ["engine", "breaks", "10000km"],
            },
            {
                "id": "2",
                "VIN": "2HNYD2H26AH123456",
                "make": "Chevrolet",
                "model": "Impala",
                "year": 2018,
                "problems": ["10000km"],
            },
            {
                "id": "3",
                "VIN": "1FTFW1ET7DKF12345",
                "make": "Toyota",
                "model": "Corolla",
                "year": 2002,
                "problems": ["filters+oil", "gear"],
            },
        ]
        return cars


def save(cars):
    with open(FILE_PATH, "w") as file:
        json.dump(cars, file)
