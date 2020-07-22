import random

school_class = ["Ana", "Ben", "Carl"]
print("The first student of the list is", school_class[0])
print("The last student of the list is", school_class[-1])
print("The class has,", len(school_class), "students")
print("school_class =", school_class)

print("-------")
print("Someone is going to another school")
randn = random.randint(0,2)
print("Good-bye,", school_class[randn])
school_class.pop(randn)
print("Now the class has,", len(school_class), "students")
print("school_class =", school_class)

print("-------")
print("We will have a new student.")
print("His name is Daniel")
school_class.append("Daniel")
print("school_class =", school_class)

print("-------")
print("Daniel decided to change with Emile from the other class")
school_class[-1] = "Emile"
print("school_class =", school_class)
