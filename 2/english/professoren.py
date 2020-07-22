import random

score = random.randint(0, 100)

print("You have attained the following score:", score)
print("Professor:")

if score >= 90:
    print("Very well! Keep it up!")
elif score < 90 and score >= 70:
    print("Good results, but you can still improve!")
elif score < 70 and score >= 50:
    print("You will have to put in more effort, but you've passed!")
else:
    print("I'm so sorry, but you have failed.")

