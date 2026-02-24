student = {
    "name": "Mary",
    "modules": [
        {"courseName": "Programming", "grade": 45},
        {"courseName": "History", "grade": 99}
    ]
}

print(f"Student: {student['name']}")

for module in student["modules"]:
    print(f"\t{module['courseName']} : {module['grade']}")