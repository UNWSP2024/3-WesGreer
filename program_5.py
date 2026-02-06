# Hot Dog Stand Program
# Written by Wesley Greer on 2/6/2026

# all of the prices
hot_dog_price = 3.50
chili_dog_price = 4.50
cheese_price = 0.50
peppers_price = 0.75
onions_price = 1.00

# find out which hot dog they want
print("We have two hot dog options: 1. Hot Dog ($3.50), and 2. Chili Dog ($4.50).")
choice = input("Would you rather have option 1 or 2? ")

if choice == "1":
    subtotal = hot_dog_price
elif choice == "2":
    subtotal = chili_dog_price
else:
    print("I'm sorry, please choose either 1 or 2.")
    exit()
    
# find out what toppings they want
cheese = input("Would you like to add cheese for $0.50? (y/n): ").lower()
if cheese == "y":
    subtotal += cheese_price

peppers = input("Would you like to add peppers for $0.75? (y/n): ").lower()
if peppers == "y":
    subtotal += peppers_price

onions = input("Would you like to add grilled onions for $1.00? (y/n): ").lower()
if onions == "y":
    subtotal += onions_price

# Calculate the tax and the total
tax_rate = 0.07
tax = subtotal * tax_rate
total = subtotal + tax

# show the costs
print(f"Your subtotal is: ${subtotal:.2f}")
print(f"The sales tax is: (7%): ${tax:.2f}")
print(f"The total cost is: ${total:.2f}")
