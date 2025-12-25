#take the input of temperature in celsius.
temp = int(input("Enter the temperature : \n"))
if temp < 0:
    print("Freezing Cold")
elif temp > 0 and temp < 10:
    print("Very Cold")
else:
    print("Coldd")