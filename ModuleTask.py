# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are of legal voting age")
# else:
#     print(f"You must be {18 - age:.0f} years older to vote")
 
# print("\n")

# e_consumption = float(input("Enter your electricity consumption in kilowatt-hours: "))
# e2_consumption = e_consumption
# if e_consumption <= 50:
#     print(f"Your total electricity bill will be {e_consumption * 0.10:0.2f}€")
# elif e_consumption > 50 >= 200:
#     print(f"Your total electricity bill will be {(e_consumption - 50) * 0.08:0.2f}€")
# else:
#     print(f"Your total electricity bill will be {e_consumption - 200}")

# print("\n")
      
# math = int(input("Enter your performance in math (0-100): "))
# physics = int(input("Enter your performance in physics (0-100): "))
# chemistry = int(input("Enter your performance in chemistry (0-100): "))
# print("\n")
# if math and physics > 90 or chemistry > 95:
#     if math and physics > 90:
#         print("Your math and physics score qualify you for a scholarship")
#     elif chemistry > 95:
#         print("Your chemistry score qualifies you for a scholarship")
# if math < 50:
#     print("Your math score is too low")
# if physics < 50:
#     print("Your physics score is too low")
# if chemistry < 50:
#     print("Your chemistry score is too low")
# else:
#     print("You have not receieved a scholarship")

# rounds = int(input("Enter number of rounds: "))
# finished_rounds = 0

# while finished_rounds < rounds:
#     print("Good Morning")
#     finished_rounds = finished_rounds + 1

# command = input("Enter command: ")

# while command != "stop":
#     print(f"Executing command: {command}")
#     command = input("Enter command: ")
# print("Execution ended.")

# password = "python123"
# password = input("Enter password: ")
# while password != "python123":
#     print("try again")
#     password = input("Enter password: ")
# else:
#     print("access granted")

# import random

# dice1 = dice2 = dice3 = dice4 = rolled = 0
# while dice1 != 6 or dice2 != 6 or dice3 != 6 or dice4 != 6:
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     dice3 = random.randint(1, 6)
#     dice4 = random.randint(1, 6)
#     rolled = rolled + 1
# print(f"Rolled the dice {rolled} times")

# first = 1

# while first <= 100:
#     second = 1
#     while second <= 100:
#         print(f"{first} times {second} is equal to {first*second}")
#         second = second + 1
#     first = first + 1
# import random
# rounds = 0
# total_rolls = 0
# while rounds <= 100000:
#     dice1 = dice2 = rolled = 0
#     while dice1 != 6 or dice2 != 6:
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         rolled = rolled + 1
#     total_rolls = total_rolls + rolled
#     rounds = rounds + 1
# average = total_rolls / rounds
# print(f"The average is {average:.2f}")

command = input("Enter a command: ")
while command != "stop":
    if command == "HELP":
        break
    print(f"Executing command: {command}")
    command = input("Enter a command: ")
else:
    print("Cya!")
print("Program Stopped")