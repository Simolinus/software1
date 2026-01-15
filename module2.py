import math
name = input("Enter name: ")
print("Hello, "+name+"!")
 
print("Enter the radius of a circle")
number = input("Radius: ")
areanumber = math.pi*float(number)**2
# print("Area of circle is equal to: "+str(areanumber))
print(f"Area of circle is equal to: {areanumber:.3f}")

