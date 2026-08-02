raw_features = [10, 50, 20, 100, 80]
maximum = max(raw_features)
print(maximum)
scaled_data= [x/maximum for x in raw_features]
print(scaled_data)
