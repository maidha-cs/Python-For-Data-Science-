raw_data = [25, -5, 40, 120, 18, -2, 35]
clean_data = [ x for x in raw_data if x > 0 and x < 100]
print(clean_data)