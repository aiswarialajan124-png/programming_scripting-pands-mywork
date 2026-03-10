import json

FILENAME = "studentData.json"

students = []

def writeDict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f)

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new students")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load students")
    print("\t(q) Quit")

    choice = input("Type one letter (a/v/s/q): ").strip()
    return choice

def doAdd(students):
    name = input("Enter student name: ")
    age = input("Enter student age: ")

    student = {
        "name": name,
        "age": age
    }
    
    students.append(student)
    print("Student Added.")

def doView(students):
    if len(students) == 0:
        print("No students to display.")
        return
    
    for student in students:
        print(student)

def writeDict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f)

def readDict():
    try:
        with open(FILENAME) as f:
            return json.load(f)
    except:
        return []

def doSave(students):
    writeDict(students)
    print("students saved")

def doLoad():
    return readDict()

# main program
choice = displayMenu()

while choice != 'q':

    if choice == 'a':
        doAdd(students)

    elif choice == 'v':
        doView(students)

    elif choice == 's':
        doSave(students)

    else:
        print("Please select a, v, s, l or q")

    choice = displayMenu()

print("Goodbye!")