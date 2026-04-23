print("Student Performance Analyzer 🚀")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("Ram", [80, 90, 100])
s2 = Student("Sushant", [70, 85, 95])

print(s1.name, s1.average())
print(s2.name, s2.average())
