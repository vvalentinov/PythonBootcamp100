student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    student_score = student_scores[key]
    if student_score <= 70:
        student_grades[key] = "Fail"
    elif 71 <= student_score <= 80:
        student_grades[key] = "Acceptable"
    elif 81 <= student_score <= 90:
        student_grades[key] = "Exceeds Expectations"
    else:
        student_grades[key] = "Outstanding"
