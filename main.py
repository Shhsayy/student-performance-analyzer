print("Student Performance Analyzer 🚀")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("Ram", [80, 90, 100])

print(s1.name)
print(s1.average())
