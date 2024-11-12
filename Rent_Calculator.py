# Inputs we need from the user
# Total Rent
# Total food ordered for snacking
# Electricity units spent
# Charge per unit

## Output 
# Total amount you've to pay is

rent = int(input("\nEnter your room/hostel rent: "))
food = int(input("\nEnter the amount of food ordered: "))
electricity_spent = int(input("\nEnter the amount of electricity spent: "))
charge_per_unit = int(input("\nEnter the charge per unit: "))
persons = int(input("\nEnter the number of persons living in the room/hostel: "))

total_bill = electricity_spent * charge_per_unit

output = (rent + food + total_bill) // persons
print(f"\nEach person will pay:  {output}")