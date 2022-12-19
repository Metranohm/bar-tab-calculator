# Initialize the tab to 0
tab = 0

# Loop until the user is finished entering items
while True:
  # Get the name and price of the item from the user
  name = input("Enter the name of the item: ")
  price = float(input("Enter the price of the item: "))
  
  # Add the price to the tab
  tab += price
  
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