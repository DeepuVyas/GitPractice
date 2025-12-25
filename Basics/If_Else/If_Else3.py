#Accept a year and check if it a leap year or not (google to find out what is a leap year)
year = int(input("Enter your year : \n"))
if year%4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")