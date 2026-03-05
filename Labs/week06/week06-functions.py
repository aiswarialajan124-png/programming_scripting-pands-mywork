# function to display menu
def displayMenu():
    print("What would you like to do? ")
    print("\t(a) Add new student")
    print("\t(v) View Student")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

# function to read modules
def readModules():
    modules = []

    moduleName = input("\tEnter the first module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))

        modules.append(module)

        moduleName = input("\tEnter new module name (blank to quit): ").strip()
    
    return modules

# function to add students
def doAdd(students):
    currentStudent = {}

    currentStudent["name"] = input("Enter student name: ")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)

# display modules
def displayModules(modules):
    print("\tName\tGrade")
    for module in modules:
        print(f"\t{module["name"]}\t{module['grade']}")

# view students
def doView(students):
    for student in students:
        print(student["name"])
        displayModules(student["modules"])

# main program
students = []

choice = displayMenu()

while choice != 'q':
    
    if choice == 'a':
        doAdd(students)
    
    elif choice == 'v':
        doView(students)

    else:
        print("Please select either a,v, or q")
    
    choice = displayMenu()