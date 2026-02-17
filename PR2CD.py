# write your code here

temperature = float(input("Enter temperature in degree Celsius: "))

if (temperature < -273.15):
    print("Invalid temperature: below absolute zero")

elif (temperature == -273.15):
    print("Temperature is absolute zero")

elif (-273.15 < temperature < 0):
    print("Temperature is below freezing")

elif (temperature == 0):
    print("Temperature is at the freezing point")

elif (0 < temperature < 100):
    print("Temperature is in the normal range")

elif (temperature == 100):
    print("Temperature is at the boiling point")

elif (temperature > 100):
    print("Temperature is above the boiling point")
