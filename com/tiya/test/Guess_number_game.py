import random
computers_number = random.randint(1,10)

users_number = 100
counter = 0

while users_number != computers_number and counter < 5:
    users_number = input("Enter your value: ")
    users_number = int(users_number)
    counter = counter + 1
    if computers_number == (users_number):
        print("You won!!!!")
    elif users_number > computers_number:
        print("My number is smaller")
    elif users_number < computers_number:
        print("My number is bigger")
if users_number != computers_number:
    print("You lose!")
