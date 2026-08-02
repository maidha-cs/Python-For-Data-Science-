temperatures = [12, 25, 38, 40, 18, 14, 30, 42, 22]
filtered_temp = [ temp for temp in temperatures if temp < 15 or temp > 35]
print(filtered_temp)