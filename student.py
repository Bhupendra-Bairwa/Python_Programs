class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display_details(self):
        print("\n Student Details:")
        print("Student Name:", self.name)
        print("Student Roll Number:", self.roll_no)
        print("Student Marks:", self.marks)

name = input("Enter Student Name: ")
roll_no = int(input("Enter Student Roll number: "))
marks = float(input("Enter Student marks: "))

Student1=Student(name, roll_no, marks)
Student1.display_details()