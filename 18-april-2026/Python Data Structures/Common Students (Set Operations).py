classA = {"Rahul", "Sneha", "Amit", "Neha"}
classB = {"Sneha", "Amit", "Karan", "Riya"}

print(f"Both classes: {classA & classB}")
print(f"Only in Class A: {classA - classB}")
print(f"All unique students: {classA | classB}")