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
        print(self.name, "danced his heart out.")

steve = Person("Steve", 24)
steve.introduce()
print("-------")
steve.dance()

print("-------")
print("There is", Person.count, "person.")
print("-------")

karen = Person("Karen", 40, 1.7, 80)
karen.introduce()
print("-------")
karen.dance()

print("-------")
print("There are", Person.count, "people.")
print("-------")
