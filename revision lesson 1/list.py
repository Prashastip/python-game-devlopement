fruits = ["apple", "banana", "mango"]

print(fruits[0]) # apple
print(fruits[1]) # banana

# adding elements
fruits.append("orange")
print(fruits)

 #insert() (add at specific position)
fruits.insert(1, "grapes")
print(fruits)

# remove() (by value)
fruits.remove("banana")
print(fruits)

#pop() (by index)
fruits.pop(0)   # removes first element
print(fruits)

#Changing Elements
fruits[0] = "pineapple"
print(fruits)

# 🔹 Length of list
print("Length of list:", len(fruits))

# 🔹 Looping through list
print("Looping through list:")
for fruit in fruits:
    print(fruit)

    # 🔹 Checking if item exists
if "apple" in fruits:
    print("Apple is in the list")
else:
    print("Apple is not in the list")

    # 🔹 Sorting list
numbers = [5, 2, 9, 1]
numbers.sort()
print("Sorted numbers:", numbers)

# 🔹 Reversing list
numbers.reverse()
print("Reversed numbers:", numbers)

# 🔹 Clearing list
fruits.clear()
print("After clearing list:", fruits)