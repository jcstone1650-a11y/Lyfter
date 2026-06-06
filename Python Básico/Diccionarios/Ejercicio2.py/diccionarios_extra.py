##Ejercicio 1
sales = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
        {'name': 'Lava Lamp', 'upc': 'ITEM-453', 'unit_price': 65.76},
        {'name': 'Iron', 'upc': 'ITEM-324', 'unit_price': 32.45},
        {'name': 'Basketball', 'upc': 'ITEM-432', 'unit_price': 12.54},    
        ]
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
        {'name': 'Lava Lamp', 'upc': 'ITEM-453', 'unit_price': 65.76},
        {'name': 'Key Holder', 'upc': 'ITEM-23', 'unit_price': 5.42},
        ]
    },
    {
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
        {'name': 'Key Holder', 'upc': 'ITEM-23', 'unit_price': 3.42},
        {'name': 'Basketball', 'upc': 'ITEM-432', 'unit_price': 17.54},
        ]
    }
]

result = {}

for sale in sales:
    for item in sale['items']:
        upc = item['upc']
        price = item['unit_price']
        
        if upc not in result:
            result[upc] = 0
        result[upc] += price

print(result)


##Ejercicio 2
employees = [
    {'name': 'Carlos', 'email': 'carlos@empresa.com', 'department': 'Ventas'},
    {'name': 'Ana', 'email': 'ana@empresa.com', 'department': 'TI'},
    {'name': 'Luis', 'email': 'luis@empresa.com', 'department': 'Ventas'},
    {'name': 'Sofia', 'email': 'sofia@empresa.com', 'department': 'RRHH'},
]

from collections import defaultdict
grounped = defaultdict(list)

for emp in employees:
    grounped[emp['department']].append(emp)

print(dict(grounped))


##Ejercicio 3
products = [
    {'name': 'Monitor', 'category': 'Electrónica', 'price': 200 },
    {'name': 'Teclado', 'category': 'Electrónica', 'price': 50},
    {'name': 'Silla', 'category': 'Muebles', 'price': 120 },
    {'name': 'Mesa', 'category': 'Muebles', 'price': 180},
    {'name': 'Mouse', 'category': 'Electrónica', 'price': 25},
]

totals = {}

for product in products:
    category = product['category']
    price = product['price']
    
    if category not in totals:
        totals[category] = 0
    totals[category] += price

print(totals)

