month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
month_number = int(input("Enter month number (1-12): "))
current_month = month[month_number-1]

print(f"\nThe month is {current_month}\n")

if month_number == 12 or 1 or 2:
    print("and the season is Winter.")
elif month_number == 3 or 4 or 5:
    print("and the season is Spring.")
elif month_number == 6 or 7 or 8:
    print("and the season is Summer")
elif month_number == 9 or 10 or 11:
    print("and season is Autumn")
else:
    ("Invalid input")

print("\n")

names = set()
print("Enter names, to stop enter nothing")

while True:
    user_input = input()
    if user_input == "":
        break
    if user_input in names:
        print("Existing name")
    else:
        print("New name")
    names.add(user_input)
for x in names:
    print(x)

print("\n")

commands = ("enter new (1)\nfetch     (2)\nquit      (3)")
airports_icao = {}
existing_airports_icao = set()

print("Enter a new airport or fetch the information of an existing airport or quit.")

while True:
    print(f"\n{commands}")
    command_input = int(input())
    print("\n")
    if command_input == 3:
        break
    if command_input == 2:
        check_existing_icao = input("Enter airport's ICAO: ")
        if check_existing_icao in existing_airports_icao:
            print(f"{airports_icao[icao]}")
    if command_input == 1:
        icao = input("Enter airport's ICAO: ")
        airport = input("Enter airport's name: ")
        airports_icao[icao] = airport
        existing_airports_icao.add(icao)
print("Program stopped.")
