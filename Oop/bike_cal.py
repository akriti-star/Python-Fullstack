from Oop.bikes import Bikes
brand = input("Enter brand: ")
bikename = input("Enter bikename: ")
rent = int(input("Enter rent: "))
bkobj = Bikes(brand=brand,bkname= bikename,rent = rent)
days = int(input("Enter days: "))
print(f'Rent of {bkobj.bikename}  for {days} days {bkobj.calculate_rent(days)}')

