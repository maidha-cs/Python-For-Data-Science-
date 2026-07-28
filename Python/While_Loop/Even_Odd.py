limit = int(input("Enetr a Limit"))
num = 1
while num <= limit:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    num += 1
print()