from student import Student
import random

def main():

    names = []

    for i in range(1, 7):
        names.append(Student("Student" + str(i), 5))
    
    random.shuffle(names)

    print("Shuffled: ")
    for student in names:
        print(student)

    names.sort(key = lambda student: student.name)

    print("\nSorted: ")
    for student in names:
        print(student)

main()