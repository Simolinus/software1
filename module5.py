import random
dice_list = []
dice_amount = int(input("Enter amount of dice to roll: "))
loop = 0
total = 0
dice = random.randint(1, 7)
while loop < dice_amount:
    dice = random.randint(1, 7)
    dice_list.append(dice)
    loop = loop + 1
for number_1 in dice_list:
    total = total + number_1
print(total)

print("\n")

sorted_list = []
numbers = input("Enter numbers or empty to quit: ")
while True:
    if numbers == "":
        break
    sorted_list.append(int(numbers))
    numbers = input("Enter numbers or empty to quit: ")
sorted_list.sort(reverse=True)
for sn in sorted_list:
    print(sn)

print("\n")

int_num = int(input("Enter an integer to check if it is a prime number: "))
if int_num > 1:
    for num in range(2, int_num):
        if int_num % num == 0:
            print(f"{int_num} is not a prime number")
        else:
            print(f"{int_num} is a prime number")
        break    
elif int_num == 1 or int_num == 0:
    print(f"{int_num} is not a prime number")

print("\n")

city_list = []
for q in range(5):
    cities = input("Enter the names of 5 cities: ")
    city_list.append(cities)
print ("\n")
for z in city_list:
    print(z)