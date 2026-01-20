import math

zander_in_cm = float(input("Hello fisher! \nPlease enter the length of your Zander that you have caught in cm: "))
if zander_in_cm >= 42:
    print("The fish is of proper length!")    
else:
    print(f"The fish is {(42 - zander_in_cm):.3f} cm below the size limit")

print("\n")

print("The cabin classes are the following:\nLUX\nA\nB\nC")
cabin_class = str(input("Enter your cabin class: "))
cabin_class = cabin_class
if cabin_class == str("LUX"):
    print("The LUX cabin is an upper-deck cabin with a balcony.")
elif cabin_class == str("A"):
    print("Cabin A is above the car deck, equipped with a window.")
elif cabin_class == str("B"):
    print("Cabin B is a windowless cabin above the car deck.")
elif cabin_class == str("C"):
    print("Cabin C is a windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

print("\n")

bio_gen = input("Enter your biological gender, M or F: ")
hemogob = float(input("Enter your hemoglobin value (g/l): "))
if bio_gen == "M":
    if hemogob >= 134 and hemogob <= 167:
        print("Your hemoglobin level is normal")
    elif hemogob < 134:
        print("Your hemoglobin level is low")
    else:
        print("Your hemoglobin level is high")
if bio_gen == "F":
    if hemogob >= 117 and hemogob <= 155:
        print("Your hemoglobin level is normal")
    elif hemogob < 117:
        print("Your hemoglobin level is low")
    else:
        print("Your hemoglobin level is high")


    
print("\n")

year = int(input("Enter a year: "))
if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

