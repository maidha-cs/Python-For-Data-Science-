
obtained_marks = float(input("Enter total obtained marks of all subjects: "))
total_marks = float(input("Enter total maximum marks  "))
percentage = (obtained_marks / total_marks) * 100
print("  Result Summary ")
print(f"Percentage: {round(percentage, 2)}%")
if percentage >= 40:
    print("Status: Congratulations! You are PASS.")
else:
    print("Status: FAIL (Percentage is below 40%).")