import json

# (i) Create an empty 'orders.json' file
# Define a list of orders, each order represented as a dictionary
initial_data = [
    {
        "size": "small",
        "price": 7.24,
        "toppings": ["basil"],
        "extra_cheese": False,
        "delivery": True,
        "client": {
            "name": "James",
            "phone": "984-312-528",
            "email": "james@gmail.com"
        }
    }
]

# Specify the file name
file_path = 'orders.json'

# Write the data to the file
with open(file_path, 'w') as file:
    json.dump(initial_data, file, indent=4)

print(f"Created '{file_path}' with example data.")


# (ii) Read a file "orders.json" and print the details
with open('orders.json', 'r') as file:
    orders_data = json.load(file)
    print("Original Orders:")
    print(json.dumps(orders_data, indent=4))

# (iii) Add new details to each order
new_details = {
    "size": "large",
    "price": 7.24,
    "toppings": ["pepperoni", "basil"],
    "extra_cheese": False,
    "delivery": False,
    "client": {
        "name": "Mark James",
        "phone": "623-312-528",
        "email": "markjames@gmail.com"
    }
}

for order in orders_data:
    order.update(new_details)
    order['client']['pincode'] = '12345'  # Add a suitable pincode to the client in each order

# (iv) Write the entire content into a new file called new_orders.json
with open('new_orders.json', 'w') as new_file:
    json.dump(orders_data, new_file, indent=4)

# (v) Extract the client name and phone number
for order in orders_data:
    client_info = order['client']
    name = client_info['name']
    phone = client_info['phone']
    print(f"Client Name: {name}, Phone Number: {phone}")

# (vi) Change separators from ":" to "=" and "," to ";"
for order in orders_data:
    for key, value in order.items():
        if isinstance(value, bool):
            order[key] = str(value).lower()
        elif isinstance(value, str):
            order[key] = value.replace(":", "=").replace(",", ";")

# (vii) Get a string with the first 2 and last 2 characters of the name
for order in orders_data:
    client_info = order['client']
    name = client_info['name']
    first_last_chars = name[:2] + name[-2:]
    print(f"First 2 and last 2 characters --> '{first_last_chars}'")
    last_two_chars = name[-2:]
    print(f"4 copies of the last 2 characters --> '{last_two_chars * 4}'")

# (ix) Sort the keys and ensure readability while printing the output
for order in orders_data:
    order_sorted = dict(sorted(order.items()))
    print(json.dumps(order_sorted, indent=4))
