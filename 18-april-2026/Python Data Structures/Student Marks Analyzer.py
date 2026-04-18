students = {"Rahul": 85, "Sneha": 92, "Arjun": 78, "Priya": 88}

topper = max(students, key=students.get)
avg_marks = sum(students.values()) / len(students)
above_85 = [name for name, mark in students.items() if mark > 85]

print(f"Topper: {topper}")
print(f"Average: {avg_marks}")
print(f"Scored > 85: {above_85}")