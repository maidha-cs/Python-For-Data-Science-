num = int( input("Enter year"))
if num % 4 == 0:
    print(f" this is leap yeaar{num}")
elif num % 100 == 0:
    print(f" this is leap yeaar{num}")
elif num % 400 == 0:
    print(f" leap year {num}")
else:
            print(f" {num} is not a Leap year")