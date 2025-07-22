student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def scoring_critera(score):
    if score > 90 and score <=100:
        Grade = "Outstanding"
    elif score > 80 and score <=90:
        Grade = "Exceeds Expectations"
    elif score > 70 and score <= 80:
        Grade = "Acceptable"
    else :
        Grade = "Fail"
    return Grade
    

#name = ""
student_grades = {}
for name in student_scores:
    score = student_scores[name]
    student_grades[name] = scoring_critera(score)

print(student_grades)