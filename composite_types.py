########################################################################################
#Dicts

person = {
    "first_name": "John",
    "last_name": "Doe",
    "nationality": "Canada",
    "birth_year": 1980
}

#Retrieving and setting elements:

print(person["first_name"])

person["first_name"] = "Jane"

########################################################################################
#Lists
#Basically Arrays
primes = [2, 3, 5, 7, 11]

users = ["Alice", "Bob", "Charlie"]

products = [
    {"name": "IPhone 12", "price": 949},
    {"name": "Fairphone", "price": 419},
    {"name": "Pixel 5", "price": 799}
]


#Retrieving list elements via their index (starting at 0):

users = ["Alice", "Bob", "Charlie"]

users[0]
users[1]
users[-1] # last element

#Overwriting
users[0] = "Andrew"

########################################################################################
#Tuple
date = (1973, 10, 23)

#Simular to dicts, act like lists

point_dict = {"x": 2, "y": 4}
point_tuple = (2, 4)

date_dict = {
  "year": 1973,
  "month": 10,
  "day": 23
}
date_tuple = (1973, 10, 23)

date_tuple[0] # 1973
len(date_tuple) # 3