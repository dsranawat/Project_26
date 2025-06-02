print ("Student Grade Calculator")

subjects = []
marks = []

num_subjects = int(input("Enter the number of subjects: "))

for i in range(num_subjects):
    subject = input(f"Enter name of subject {i + 1}: ")
    score = float(input(f"Enter marks for {subject}: "))
    subjects.append(subject)
    marks.append(score)

total = sum(marks)
percentage = (total / (num_subjects * 100)) * 100


if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'F'

print("\n Result Summary:")
for subject, score in zip(subjects, marks):
    print(f"{subject}: {score}/100")

print(f"\nTotal: {total}/{num_subjects * 100}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

