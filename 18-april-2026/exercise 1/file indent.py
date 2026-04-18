import json
students = {
"students": [
{"name": "Priya", "marks": 88},
{"name": "Karan", "marks": 75}
]}

with open("output.json", "w") as file:
    json.dump(students, file, indent=4)