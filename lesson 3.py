# Task 1
total_floors = 9
apartments_per_floor = 4
total_entrances = 4
apartment_number = int(input("Enter the apartment number: "))
if 1 <= apartment_number <= 144:
    NUMBERS = total_floors * apartments_per_floor
    entrance = (apartment_number - 1) // NUMBERS + 1
    print(f"Entrance: {entrance}")
    floor = (apartment_number + apartments_per_floor - 1) // apartments_per_floor
    print(f"Floor: {floor}")
    apartment_on_floor = ((apartment_number - 1) % apartments_per_floor) + 1
    print(f"apartament on floor: {apartment_on_floor}")
else:
    print("There's no such apartment in this building.")
# Task 2
years = int(input("Number of years: "))
day = years * 365
if years % 4 == 0 or years % 400 == 0 and years % 100 != 0:
    print(f"Day: {years * day}")
else:
    print("Error")
# Task 3
a, b, c = int(input("a:")), int(input("b:")), int(input("c:"))
if a + b > c:
    print("you`re good")
else:
    print("Error. Please writing new values")
