total_subjects = int(input("Enter total number of subjects: "))
passed_all = True
for i in range(1, total_subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    if marks < 40:
        passed_all = False
if passed_all:
    print(" Congratulations! You passed all subjects.")
else:
    print(" Failed (One or more subjects have marks below 40).")