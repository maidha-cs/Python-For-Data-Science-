total = 0
num = float(input("Enter a number: "))
while num != 0:
    total += num
    num = float(input("Again enter a number: "))
print(f"Total Sum: {total}")