while True:
    try:
        age = int(input("What is your age?: "))
    except ValueError:
        print("Age has to be an integer.")
        print("Please answer the question again.")
        print()
        continue
    else:
        break

if age < 18:
    print("You are still not an adult.")
else:
    print("You are an adult!")


