import json

with open('students.json', 'r') as f:
    data = json.load(f)
    students = data['students']

print([s['name'] for s in students])
print([s['name'] for s in students if s['course'] == 'Python'])
print(max(students, key=lambda x: x['marks'])['name'])
print(sum(s['marks'] for s in students) / len(students))

courses = [s['course'] for s in students]
print({c: courses.count(c) for c in set(courses)})