import math
import sys
import random

name = input("Enter name: ")
print("Hello, "+name+"!")

print("Enter the radius of a circle")

number = input("Radius: ")
areanumber = math.pi*float(number)**2

# print("Area of circle is equal to: "+str(areanumber))
print(f"Area of circle is equal to: {areanumber:.3f}")

print("Enter the length and witdth of a rectangle")

length = float(input("Length: "))
width = float(input("Width: "))
perimiter = (length + width)*2
area_rectangle = length * width

print(f"Perimiter of the rectangle is {perimiter:.3f} and the area is {area_rectangle:.3f}")

print("Enter three integer numbers")

first_integer = float(input("Enter number one: "))
second_integer = float(input("Enter number two: "))
third_integer = float(input("Enter number three: "))

sum_integer = first_integer + second_integer + third_integer
product_integer = first_integer * second_integer * third_integer
average_integer = sum_integer / 3

print(f"The sum of the numbers is {sum_integer}, the product is {product_integer} and the average is {average_integer}")

print("Enter a mass in the three following medieval untis")

talents_amount = float(input("Enter a mass in talents: "))
pounds_amount = float(input("Enter a mass in pounds: "))
lots_amount = float(input("Enter a mass in lots: "))

lot_in_grams = 13.3
pound_in_grams = lot_in_grams * 32
talent_in_grams = pound_in_grams * 20

talents_kg = talents_amount * talent_in_grams * 0.001
pounds_kg = pounds_amount * pound_in_grams * 0.001
lots_kg = lots_amount * lot_in_grams * 0.001

sum = lots_kg + pounds_kg + talents_kg
sum_int = int(sum)
sum_dec_in_grams = (sum - sum_int) * 1000

print(f"The weight in modern units:\n{sum_int} kilograms and {sum_dec_in_grams:.2f} grams.")

rn1 = random.randrange(10)
rn2 = random.randrange(10)
rn3 = random.randrange(10)

rn4 = random.randrange(1, 7)
rn5 = random.randrange(1, 7)
rn6 = random.randrange(1, 7)
rn7 = random.randrange(1, 7)

print(f"3-digit code:\n{rn1}{rn2}{rn3}")
print(f"4-digit code:\n{rn4}{rn5}{rn6}{rn7}")