import sys
input = sys.stdin.readline

score_sum = 0
grade_sum = 0
dic_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
             'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for _ in range(20):
    subject, grade, score = map(str, input().split())
    if score != 'P':
        score_sum += float(grade)
        grade_sum += dic_score[score] * float(grade)
result = grade_sum / score_sum
print(result)