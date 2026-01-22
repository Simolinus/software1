#Task 1
first = 1
second = 3
while first <= 1000:
    if first % second == 0:
        print(f"{first} is divisible by 3")
    first = first + 1

print("\n") #Task 2

inches = float(input("Enter number of inches: "))
while inches > 0:
    print(f"{inches} inches are {inches * 2.54} cm")
    inches = float(input("Enter number of inches: "))
print("No negatives! Stopping program.")

print("\n") #Task 3

print("Enter numbers and stop by entering nothing")
number_input = input("Enter a number: ")
while number_input != "":
    number = float(number_input)
    largest = number
    smallest = number
    while True:
            if number_input == "":
                break

            if number > largest:
                largest = number
            if number < smallest:
                smallest = number

            number_input = input("Enter a number: ")
            if number_input == "":
                break
            number = float(number_input)
    print(f"The largest number is {largest} and the smallest number is {smallest}.")

print("\n") #Task 4

import random

number_game = int(input("Guess number between 1-10: "))
correct_number = random.randint(1, 10)
while number_game != correct_number:
    if number_game < correct_number:
        print("Too low! Guess again.")
    if number_game > correct_number:
        print("Too high! Guess again")
    number_game = int(input(""))
print("Correct!")

print("\n") #Task 5

username = input("Enter username: ")
password = input("Enter password: ")
if username != "python" and password != "rules":
    print("Incorrect username or password")
tries = 0
while username != "python" and password != "rules":
    if tries <= 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("Incorrect username or password!")
        tries = tries + 1
    else:
        print("Access Denied")
        exit(1)
print("Welcome")

print("\n") #Task 6

import random

user_input_points = input("Enter number of random points to generate to approximate pi: ")
random_points = int(user_input_points)
radius = float(1)

N = random_points
n = 0
loop = 0
while loop < N:

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n = n + 1
    loop = loop + 1
    pi_a = 4 * n / N
print(f"the approx of pi = {pi_a}")