"""
CS210 Class Encore 
Author: Jose Renteria

Practice with dictionaries and File I/O. 

"""
# We can initialize a dict like this, similar to JSON notation
def example():
    mustang = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    'mileage': 89_000
    # Iterable types
    }

    print(mustang)
    print('-'* 100)

    # key 'mustang' with value of type <list>
    car = {"mustang": [2010, 2011, 2012]}
    print(car)
    print('-'* 100)

    # O(1) access 

    # But in Python, dictionaries cannot store duplicates on a single key, for example:
    mustang['model'] = 'F150' # this will overwrite the model
    print(mustang)

    print('-'* 100)

    mustang.update({'model': 'Mustang'}) # can also be done like this
    print(mustang)
    print('-'* 100)

    # but lets say you are an auto dealer, you obviously carry more than one model
    # lets say you also have a F150 and a Bronco currently

    F150 = {
    "brand": "Ford",
    "model": "F150",
    "year": 2009,
    "mileage": 100_029
    }

    Bronco = {
    "brand": "Ford",
    "model": "Bronco",
    "year": 2023,
    "mileage": 1220
    }
    
    models = [mustang, F150, Bronco] # These are the current models offered
    lot = {}                         # initialize an empty lot
    key = 'Current Models Available' # what we want our key to be
    for model in models:            # iterate through the current models we want to store in our dict
        if key in lot:              # if the key already exists,
            lot[key].append(model)  # we simply append the model to the key
        else:
            lot[key] = [model]      # if not, initialize the key, and assign its 
                                    # value a LIST with the first model inside of that list, aka the Mustang
    print(lot)
    print('-'* 100)

#example()


"""
Now, time to do it on your own

We want to create a dictionary of students, and have the keys be their class standing
So if I call student_dict['Freshman'], I want to see all Freshmen in the system listed

"""


import csv  # import our csv module
# CSV documentation here https://realpython.com/python-csv/
# Optional: https://realpython.com/python-kwargs-and-args/

def create_student_roster(file_name: str, *key: str):
    student_dict = {} # Initialize an empty dict

    with open(file_name, 'r') as csv_file:  # we use 'with' so it can handle opening and closing the file
        # declare and assign the csv.reader object, with your file passed into it
        csv_reader = csv.reader(csv_file)
        # skips onto the next iteration in the object i.e. line 2 if starting at line 1
        next(csv_reader)
        # iterate over your object, your csv_reader is a collection of lines aka an ITERATOR
        # (name, age, standing) == (0, 1, 2)
        for line in csv_reader:
            # unpack the tuple from each line, this will allow you to access each variable in the line
            name, age, standing = line
            # initialize a generic student tuple with their name and age
            student = (name, int(age))
            # if the standing key already exists in our student_dict
            if standing in student_dict:
                # append the student to the corresponding key
                student_dict[standing].append(student)
            else:
            # else: (This mean it does not exist in our dict yet)
                student_dict[standing] = [student]
                # we initialize the key and create a list with the first studnet inside of it
        # Return the student dict
        # Bonus points: Utilize the optional parameter *key to return the list of students in our dict with that specified key, i.e. just Fresman
    return ((student_dict[key[0]] if key else student_dict))
    
if __name__ == '__main__':
    print("Whole Roster:" , create_student_roster('roster.csv'))
    print('-'* 100)
    print("Just Freshmen:", create_student_roster('roster.csv', 'Freshman'))