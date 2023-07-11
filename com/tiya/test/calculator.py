from com.tiya.test.calculator_functions import *

val_a = input("Enter your first value: ")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

val_b = input("Enter your second value")

if choice == '1':
    add(val_a, val_b)
elif choice == '2':
    subtract(val_a, val_b)
elif choice == '3':
    multiply(val_a, val_b)
elif choice == '4':
    divide(val_a, val_b)
