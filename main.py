class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("Ram", [80, 90, 100])
s2 = Student("Sushant", [70, 85, 95])
s3 = Student("Hari", [95, 92, 96])

students = [s1, s2, s3]

topper = students[0]

for student in students:
    if student.average() > topper.average():
        topper = student

print("Topper is:", topper.name, topper.average())
