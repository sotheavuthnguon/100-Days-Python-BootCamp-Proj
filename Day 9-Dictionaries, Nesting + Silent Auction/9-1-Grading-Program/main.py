student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student_key in student_scores:
    score = student_scores[student_key]
    if score >= 91:
        student_grades[student_key] = "Outstanding"
    elif score >= 81:
        student_grades[student_key] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student_key] = "Acceptable"
    else:
        student_grades[student_key] = "Fail"

print(student_scores)
print(student_grades)