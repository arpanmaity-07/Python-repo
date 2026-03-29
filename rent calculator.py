rent= int(input("Enter the rent amount: "))
if rent < 0:
    print("Invalid rent amount. Please enter a positive value.")
food = int(input("Enter the food expenses: "))
if food < 0:
    print("Invalid food expenses. Please enter a positive value.")
transportation = int(input("Enter the transportation expenses: "))
if transportation < 0:
    print("Invalid transportation expenses. Please enter a positive value.")
electricity = int(input("Enter the electricity expenses: "))
if electricity < 0:
    print("Invalid electricity expenses. Please enter a positive value.")
charge_per_unit = int(input("Enter the charge per unit of electricity: "))
persons = int(input("Enter the number of persons sharing the rent: "))

total_expenses = rent + food + transportation + (electricity * charge_per_unit)
share_per_person = total_expenses / persons
print("Total expenses: ", total_expenses)
print("Share per person: ", share_per_person)