#Greater number between the 2

num1 = int(input("Enter the first number \n"))
num2 = int(input("Enter the second number \n"))

if num1 > num2:
    print(f"{num1} is greater then {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both are equal")