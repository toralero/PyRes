import time



print("Take this quiz to find out which pet you should have!")

# Initialize points
score = {"dog": 0,
         "cat": 0,
         "hamster": 0,
         "turtle": 0}

time.sleep(2)
choice = int(input("""Which one describes your schedule best?
    1. I feel like I have lots of free time!
    2. I have time, but I want to use it to rest.
    3. My schedule really full
    """))

while not (choice > 0 and choice < 4):
    choice = int(input("You didn't pick a valid choice. Pick again: "))

if choice == 1:
    score["dog"] += 10
    score["cat"] += 5
    score["hamster"] += 3
    score["turtle"] += 1
elif choice == 2:
    score["dog"] += 3
    score["cat"] += 5
    score["hamster"] += 7
    score["turtle"] += 5
elif choice == 3:
    score["dog"] += 1
    score["cat"] += 5
    score["hamster"] += 3
    score["turtle"] += 10
else:
    print("Wrong choice")

choice = int(input("""What kind of companion do you want?
    1. One that will last.
    2. An active one.
    3. An independent one.
    4. A loyal one.
    """))

while not (choice > 0 and choice < 5):
    choice = int(input("You didn't pick a valid choice. Pick again: "))

if choice == 1:
    score["dog"] += 5
    score["cat"] += 5
    score["hamster"] += 1
    score["turtle"] += 10
elif choice == 2:
    score["dog"] += 7
    score["cat"] += 5
    score["hamster"] += 7
    score["turtle"] += 1
elif choice == 3:
    score["dog"] += 1
    score["cat"] += 10
    score["hamster"] += 1
    score["turtle"] += 5
elif choice == 4:
    score["dog"] += 10
    score["cat"] += 5
    score["hamster"] += 3
    score["turtle"] += 1
else:
    print("Wrong choice")

choice = int(input("""Finally, what is your preference?
    1. A Dog
    2. A Cat
    3. A Hamster
    4. A Turtle
    """))

while not (choice > 0 and choice < 5):
    choice = int(input("You didn't pick a valid choice. Pick again: "))

if choice == 1:
    score["dog"] += 10
    score["cat"] += 0
    score["hamster"] += 0
    score["turtle"] += 0
elif choice == 2:
    score["dog"] += 0
    score["cat"] += 10
    score["hamster"] += 0
    score["turtle"] += 0
elif choice == 3:
    score["dog"] += 0
    score["cat"] += 0
    score["hamster"] += 10
    score["turtle"] += 0
elif choice == 4:
    score["dog"] += 0
    score["cat"] += 0
    score["hamster"] += 0
    score["turtle"] += 10
else:
    print("Wrong choice")

# Final results
result = max(score, key=score.get)

if result == "dog":
    print("You want a loyal companion, someone you can trust as a companion and even as a friend...")
    time.sleep(2)
    print("You should get a dog.")
elif result == "cat":
    print("You want an independent companion, sometimes cunning, but a good friend...")
    time.sleep(2)
    print("You should get a cat.")
elif result == "hamster":
    print("You like seeing your companion performing various activities, and live a small but full life...")
    time.sleep(2)
    print("You should get a hamster.")
elif result == "turtle":
    print("You want a pet that will last, and also knows how to take care of itself...")
    time.sleep(2)
    print("You should get a turtle.")
