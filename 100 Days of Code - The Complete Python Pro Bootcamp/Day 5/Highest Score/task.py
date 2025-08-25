student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_exam_score = sum(student_scores)
MAX = 0
for i in student_scores:
    if i > MAX:
        MAX = i

print(MAX)
print(max(student_scores))

