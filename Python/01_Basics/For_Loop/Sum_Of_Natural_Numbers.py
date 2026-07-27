num = int(input("Enter a limit number: "))
total_sum = 0
for i in range(1, num + 1):
    total_sum += i
print(f"The sum of numbers from 1 to {num} is: {total_sum}")