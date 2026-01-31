import random

def dice_roll():
    return random.randint(1, 6)

rolls = []
while True:
    result = dice_roll()
    rolls.append(result)
    if result == 6:
        break

print(rolls)

print("\n")

def custom_dice_roll(sides):
    return random.randint(1, sides)

dice_sides = int(input("Enter number of sides for the dice: "))

rolls_custom = []
while True:
    result = custom_dice_roll(dice_sides)
    rolls_custom.append(result)
    if result == dice_sides:
        break

print(rolls_custom)

print("\n")

def gallons_to_liters(a):
    return a * 3.78541

gallons = float(input("Enter volume in gallons to stop enter a negative value: "))

while gallons >= 0:
    print(gallons_to_liters(gallons))
    gallons = float(input("Enter volume in gallons to stop enter a negative value: "))

print("\n")

def function_sum_list(num_list):
    sum = 0
    for number in num_list:
        sum = sum + number
    return sum

num_list = []
number = input("Enter interger for list to stop press enter: ")
while True:
    if number == "":
        break
    num_list.append(int(number))
    number = input("Enter interger for list to stop press enter: ")

sum = function_sum_list(num_list)
print(sum)

print("\n")

def function_remove_uneven(num_list):
    even_list = []
    for number in num_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

num_list2 = []
number2 = input("Enter interger for list to stop press enter: ")
while True:
    if number2 == "":
        break
    num_list2.append(int(number2))
    number2 = input("Enter interger for list to stop press enter: ")
even_list = function_remove_uneven(num_list2)
print(num_list2)
print(even_list)

print("\n")

import math
def pizza_price_size(diameter_cm, price_euro):
    price_per_sq_m = price_euro / (math.pi*((diameter_cm/100)/2)**2)
    return price_per_sq_m

print("Compare price of two pizzas")
print("\n")
diameter_cm = float(input("Enter diameter of pizza 1 in cm: "))
price_euro = float(input("Enter price of pizza 1 in euros: ")) 
pizza_1 = pizza_price_size(diameter_cm, price_euro)
print("\n")
diameter_cm = float(input("Enter diameter of pizza 2 in cm: "))
price_euro = float(input("Enter price of pizza 2 in euros: ")) 
pizza_2 = pizza_price_size(diameter_cm, price_euro)
print("\n")
if pizza_1 > pizza_2:
    print(f"pizza 1 costs {pizza_1:.3f}€ per square meter\npizza 2 costs {pizza_2:.3f}€ per square meter.\nTherefore pizza 2 provides better value for your money.")
elif pizza_2 > pizza_1:
    print(f"pizza 1 costs {pizza_1:.3f}€ per square meter\npizza 2 costs {pizza_2:.3f}€ per square meter.\nTherefore pizza 1 provides better value for your money.")