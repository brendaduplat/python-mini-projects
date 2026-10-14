students = [
    {"name": "Ana", "grade": 7},
    {"name": "Brenda", "grade": 9},
    {"name": "Carlos", "grade": 5},
    {"name": "Daniel", "grade": 8},
    {"name": "Eduarda", "grade": 4},
    {"name": "Felipe", "grade": 4},
    {"name": "Juliana", "grade": 8},
]


def print_group(title, group):
    print(f"{title}:")
    for student in group:
        print(f"{student['name']} - {student['grade']}")
    print()


approved = [student for student in students if student["grade"] >= 7]
make_up_exam = [student for student in students if 5 <= student["grade"] < 7]
failed = [student for student in students if student["grade"] < 5]

average = sum(student["grade"] for student in students) / len(students)
highest_grade = max(student["grade"] for student in students)
lowest_grade = min(student["grade"] for student in students)
top_students = [s["name"] for s in students if s["grade"] == highest_grade]
bottom_students = [s["name"] for s in students if s["grade"] == lowest_grade]

print(f"Class average: {average:.1f}\n")

print_group("Approved", approved)
print_group("Make-up exam", make_up_exam)
print_group("Failed", failed)

print(f"Highest grade: {', '.join(top_students)} - {highest_grade}")
print(f"Lowest grade: {', '.join(bottom_students)} - {lowest_grade}")