
# Step 1: Create an empty list called shopping_list

# Step 2: Ask the user to enter 5 items (use input) and add them to the list

# Step 3: Print the full shopping list

# Step 4: Ask the user which item they want to remove
# Remove that item from the list

# Step 5: Ask the user to add one more item
# Add it to the list

# Step 6: Print the updated list

# Step 7: Print total number of items

# Step 8: Use a loop to display all items one by
# shopping_list=[]
# print(shopping_list)
# us1=input("Add any item to this list. ")
# us2=input("Add any item to this list. ")
# us3=input("Add any item to this list. ")
# us4=input("Add any item to this list. ")
# us5=input("Add any item to this list. ")
# shopping_list.append(us1)
# shopping_list.append(us2)
# shopping_list.append(us3)
# shopping_list.append(us4)
# shopping_list.append(us5)
# print(shopping_list)
# us6=int(input("Which item would you like to delete from this list? (Use the value. First item on the list = 0...) "))
# shopping_list.pop(us6)
# us7=(input("Which item would you like to ad to the list now?"))
# shopping_list.append(us7)
# print(shopping_list)
# print(len(shopping_list))

# def total_price():
#    qua=int(input("How many products did you buy"))
#    price=float(input("What is the price of this item"))
#    ans=qua*price
#    print(ans)
# total_price()

# def total_price():
#    qua=int(input("How many products did you buy"))
#    price=float(input("What is the price of this item"))
#    return qua*price
# ans=total_price()
# print(ans)

def area():
    len=float(input("What is the length of this rectangle?"))
    wid=float(input("What is the width of this recangle?"))
    return len*wid
ans=area()
print(ans)