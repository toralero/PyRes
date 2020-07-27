# A class of students
class_a = ["Edward", "Sally", "Oscar", "Ana"]
class_b = ["Steve", "Julius", "Jenny", "Stacey"]
class_c = ["Aubrey", "Kyle", "Bob", "Velma"]

# A year with multiple classes
year_3 = [class_a, class_b, class_c]

# A year directly
year_3 = [["Edward", "Sally", "Oscar", "Ana"],
          ["Steve", "Julius", "Jenny", "Stacey"],
          ["Aubrey", "Kyle", "Bob", "Velma"]]

# Accessing the Classes
print("A Class with year_3[0]:", year_3[0])
print("B Class with year_3[1]:", year_3[1])
print("C Class with year_3[2]:", year_3[2])

print("-------")

# Accessing Jenny
print("Jenny is in class B, which is year_3[1]")
print("Jenny is the third element of class B")
print("year_3[1][2] =", year_3[1][2])

# Accessing Aubrey
print("Aubrey is in class C, which is year_3[2]")
print("Aubrey is the first element of class C")
print("year_3[2][0] =", year_3[2][0])




