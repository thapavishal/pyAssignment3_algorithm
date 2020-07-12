import csv


print("===== Welcome to IT Academy =====")
print("\t Courses available")
print("1.\t Python")
print("2.\t Cyber Security with Python")
print("3.\t Machine Learning with Python")
print("4.\t Web development with Python")
print("5.\t Internet of Things with Python")

print("\n\t Select the operation you want to do:")
student_data = []


def add_student_data(name, age, course):
    student_data.append(
        {
            "name": name,
            "age": age,
            "course": course
        }
    )


def show_student_data():
    print("S.N.\tName\tRollNo\tMark")
    for x, y in enumerate(student_data):
        print(str(x + 1) + "\t" + y["name"] + "\t" +
              y["age"] + "\t" + y["course"])


def accept_input():

    print("\n1.Add \n2. Show \n3. Delete")
    operation = int(input("Please select the operation you want to perform: "))
    if operation == 1:
        print("Please enter the student details")
        name = input("Please enter student name:")
        age = input("Please enter student age:")
        course = input("Please enter course from above list :")
        add_student_data(name, age, course)
        with open('student.csv', 'w') as csvfile:
            wrt = csv.writer(csvfile, delimiter=',')
            wrt.writerow([name, age, course])

        # print(student_data)
    elif operation == 2:
        show_student_data()

    elif operation == 3:
        print("Select the item you want to delete")
        show_student_data()
        item_to_delete = input("Enter the S.N. to delete: ")
        del student_data[int(item_to_delete) - 1]
        show_student_data()
        print("Item has been deleted")

    more = input("Do you want to do more operations y/n ? ")
    if more == 'y':
        accept_input()
    else:
        print("Student Application has exited")


accept_input()
