print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


Bill = 0

if size == "s" or size == "S":
    Bill += 15
    if add_pepperoni == "y" or add_pepperoni == "Y":
        Bill+= 2
elif size == "m" or size == "M":
    Bill += 20
    if add_pepperoni == "y" or add_pepperoni == "Y":
        Bill += 3
elif size == "l" or size == "L":
    Bill += 25
    if add_pepperoni == "y" or add_pepperoni == "Y":
        Bill += 3
if extra_cheese == "y" or extra_cheese == "Y":
    Bill+= 1

print(f"Final bill is ${Bill}")





