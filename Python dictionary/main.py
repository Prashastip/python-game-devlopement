# python dictionary
# A Python dictionary is a built-in data type used to store data in key–value pairs.
# Think of it like a real dictionary:
# You look up a word (key)
# And get its meaning (value)
# 🔹 Key Features
# Unordered (before Python 3.7; now it keeps insertion order)
# Mutable (you can change values)
# Keys must be unique
# Keys must be immutable types (like strings, numbers, tuples)

person={
    "name":"Agastya",
    "age":12,
    "hobby":"tennis",
    "country":"Switzerland"

}
print(person)
print(person["name"])
print(person["country"])

# looping through keys
for item in person:
    print(item)

# looping through values
for item in person.values():
    print(item)

# looping through items
for item in person.items():
    print(item)

# adding new items
person["hight"]="160cm"
print(person)

# changing value
person["hobby"]="piano"
print(person)