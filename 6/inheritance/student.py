class Person:

    count = 0

    def __init__(self, name, age, height=None, weight=None):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        Person.count += 1

    def introduce(self):
        print("Hello! I am", self.name)
        print("I am", self.age, "years old.")
        if self.height != None:
            print("My height is", self.height, "meters.")
        if self.weight != None:
            print("My weight is", self.weight, "kilograms.")

    def dance(self):
        print(self.name, "danced his/her heart out.")

class Student(Person):
    
    def __init__(self, name, age, studentID,  height=None, weight=None):
        Person.__init__(self, name, age, height, weight)
        self.studentID = studentID

kevin = Student("Kevin", 15, "M00541972", 1.7, 45)
print(kevin.name, "is", kevin.age, "years old, and is student nº", kevin.studentID)
kevin.dance()
print("--------")
kelly = Person("Kelly", 45)
kelly.introduce()
kelly.dance()

print("There are", Person.count, "people.")

print("What is", kelly.name, " ID? It is:")
print(kelly.studentID)


