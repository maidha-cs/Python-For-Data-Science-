def check_grade(score):
    if score >= 85:
        return "A+ (Outstanding Performance!)"
    elif score >= 70:
        return "A (Good Job!)"
    elif score >= 50:
        return "B (Satisfactory, keep improving.)"
    else:
        return "Fail (Mehnat ki zaroorat hai!)"

# Marks check karte hain
student1_result = check_grade(92)
student2_result = check_grade(45)

print(f"Student 1: {student1_result}")
print(f"Student 2: {student2_result}")