# A year directly
year_3 = [["Edward", "Sally", "Oscar", "Ana"],
          ["Steve", "Julius", "Jenny", "Stacey"],
          ["Aubrey", "Kyle", "Bob", "Velma"]]

# In order to print everyone in a list like this
# we require a loop that loops through the classes
# and one INSIDE it that loops through the students
for class_n in range(0, len(year_3)):
    print("CLASS", class_n+1) # Starts counting from 0
    for student_n, student in enumerate(year_3[class_n]):
        print("STUDENT Nº", student_n+1, "IS", student)
