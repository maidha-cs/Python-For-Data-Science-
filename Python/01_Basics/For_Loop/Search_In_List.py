numbers = [12, 45, 67, 23, 89, 100]
target = int(input("Enter a number to search in database: "))
found = False
for num in numbers:
    if num == target:
        found = True
        break
if found:
    print(f"Yes! {target} is present in the list.")
else:
    print(f"No! {target} is not found.")