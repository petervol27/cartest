To run the program you must be in the app.py file, otherwise it will not RUN!!!!
-actions include the add, delete and list functions 
-using a json I load the cars dictionary from the cars.json file which I make sure to create in the load function 
-I use the save function upon exit from the program to update the json file 
-in each function I send the list of dictionaries so as to make sure that no error occures
-calculations include the calculation for the profit plus total cars function which I call each time inside the main menu even when you add more cars or remove them it gets updated
-the variables which are the constant variables are a list of the problems and problems names which I use to check the prices and the names of the problems inside each car object there is a list of problems which gets tested against the list of problems names so as to not make the logic too complex 
-main menu is the main menu basically where all the functions are called
-error handling has been handled either by try except or by else statements that state invalid input
function explanations:
-the car list loops over the cars object gives us the main details like VIN and so on and then loops over the problems names to give us a list of the names of each problem inside the car object
-car add adds a new car object each given an id based on the last object in the list of the cars, gives you to input every part of the dictionary checks if VIN includes 17 characters as it should and makes sure the year is a number, it then takes in the total value of the repairs and makes sure that the user agrees
-the delete function takes the ID I created for each object and tells you to choose which one to remove so as to be more effective than searching by VIN or name 
-search gives you four options to search by model or make , VIN ,year or problems, each one has a search term variable and an empty search results list that gets updated if the search term fits into the parameters set in each search option, if not then the no cars found will print
-load loads the json and if it doesnt exist creates a new file that has a prebuilt dictionary already 
-save saves the json each time you exit the program 
-validated that if the app.py is not the main the program will not run 
