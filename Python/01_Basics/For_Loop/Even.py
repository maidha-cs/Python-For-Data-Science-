from selectors import SelectSelector

Num = int(input("Enter a number:"))
for i in range(1,Num+1):
    if i % 2==0:
        print(i , "is even")
    else:
        print(i, "is odd")
