##Ejercicio 1 
hotel = {
    "name": "Hotel las Pulgas",
    "number_of_stars": 2,
    "rooms": [
        {"number": 1, "floor": 1, "price_per_night": 10},
        {"number": 2, "floor": 1, "price_per_night": 15},
        {"number": 3, "floor": 1, "price_per_night": 8},
        {"number": 4, "floor": 1, "price_per_night": 5},
        {"number": 5, "floor": 1, "price_per_night": 20},
        {"number": 6, "floor": 1, "price_per_night": 16},
        {"number": 7, "floor": 1, "price_per_night": 7},
        {"number": 8, "floor": 1, "price_per_night": 11},
        {"number": 9, "floor": 1, "price_per_night": 25},
        {"number": 10, "floor": 1, "price_per_night": 6},
    ]
}

print(hotel)


##Ejercicio 2
list_a = ['first_name', 'middle_name', 'last_name']
list_b = ['Tom', 'Angel', 'Stone']

new_dictionary = dict(zip(list_a, list_b))

print(new_dictionary)


##Ejercicio 3
list_of_keys = ['access_level', 'age']
employee = {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28,
}

for key in list_of_keys:
    if key in employee:
        del employee[key]
        
print(employee)


