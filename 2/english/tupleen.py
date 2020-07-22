people_in_photo = ("Harry", "Hermione", "Ron")
print("In the photo are:", people_in_photo)
print("The person on the left is: ", people_in_photo)

print("Is Hermione in this photo?")
if "Hermione" in people_in_photo:
    print("Hermione is in this photo")

print("Let's see if Ron can change his name")
people_in_photo[2] = "Ronny"


