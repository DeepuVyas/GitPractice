#Accept name and age from the user. Check if the user is a valid voter or not.
name = input("What is your name \n")
age = int(input("Tell us your age \n"))
if age >= 18:
    print(f"{name} you are a valid voter")
else:
    print(f"{name} you are not a valid voter")
