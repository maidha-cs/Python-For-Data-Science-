Number = [1,2,3,4,5,6,7,8,9]
max = 0
min = 0
for num in Number:
    if num > max:
        max = num
    if num < min:
        min = num
print("larger", max)
print("Smaller" , min)