student_scores={
    "harry": 81,
    "ron":78,
    "hermione":99,
    "draco":74,
    "neville":62,
}
student_grades={}

for student in student_scores:
    score=student_scores[student]
    
    if score > 90:
        student_grades[student] = "Excellent"
    elif score > 80:
        student_grades[student] = "Good"
    elif score > 70:
        student_grades[student] = "This is okay"
    elif score > 60:
        student_grades[student] = "You pass"
    else:
        student_grades[student] = "You fail"

print(student_grades)        



