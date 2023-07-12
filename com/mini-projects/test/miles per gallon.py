from random import randint
gals = randint(10, 25)
miles = randint(200, 400)
print("The car can travel " + str(miles // gals) + " miles per gallon. ")
print("The car's fuel tank can hold " + str(gals) + "gallons")
print("The car can travel " + str(miles) + " miles with a full tank.")

