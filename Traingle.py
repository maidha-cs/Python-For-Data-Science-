Triangle = input(" Triangle Valid or Not")
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
if  (a + b > c) and  (b + c > a) and ( a + c > b ):
    print("triangle are valid  ")
else:
    print("Triangle are not valid")
