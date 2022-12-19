# Initialize the tab to 0
tab = 0

inventory = {}

# Add the items to the inventory
inventory["beer"] = 5.00
inventory["wine"] = 8.00
inventory["whiskey"] = 12.00
inventory["rum"] = 8.00
inventory["tequila"] = 10.00
inventory["ansinthe"] = 15.00
inventory["mescal"] = 12.00
inventory["fish & chips"] = 10.00,
inventory["chicken wings"] = 8.00
inventory["chicken tenders"] = 8.00
inventory["sour patch kids"] = 5.00

# Print the available items and prices
print("Welcome to the bar! Here are the items available for purchase:")
for name, price in inventory.items():
  print(f"{name}: ${price:.2f}")

# Loop until the user is finished entering items
while True:
  # Get the name of the item from the user
  name = input("Enter the name of the item you would like to purchase: ")
  
  # Check if the item is in the inventory
  if name in inventory:
    # Add the price of the item to the tab
    tab += inventory[name]
  else:
    print("Sorry, that item is not available.")
  
  # Check if the user is finished entering items
  finished = input("Are you finished entering items (Y/N)? ")
  if finished.upper() == "Y":
    break

# Calculate the total with tax and tip
TAX_RATE = 0.08
TIP_RATE = 0.15
total = tab + tab * TAX_RATE + tab * TIP_RATE

# Print the total
print(f"Total: ${total:.2f}")