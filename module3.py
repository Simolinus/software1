zander_in_cm = float(input("Hello fisher! \nPlease enter the length of your Zander that you have caught in cm: "))
if zander_in_cm >= 42:
    print("The fish is of proper length!")    
else:
    print(f"The fish is {(42 - zander_in_cm):.3f} cm too short")
