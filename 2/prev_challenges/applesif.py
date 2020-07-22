import random
import time # This is just for fun hahah

# The final result may be a number between 3 and 30
# We will pick 20 to be a number that satisfies your boss

harvest = random.randint(10, 30)
print("You harvested", harvest, "apples")
a = harvest

steal = random.randint(5, 10)
print("Someone stole", steal, "apples from you")
a -= steal

donation = random.randint(3, 5)
print("A kind old man decided to give you", donation, "apples")
a += donation

# How many apples you have
print("I have", a, "apples")

# Check with your boss to see if he likes it
print("Your boss is checking")
print("...")

if a >= 20:
	time.sleep(3) # This is waiting 3 seconds... just for fun! Not part of the challenge
	print("Good job! You just landed a promotion!")
else:
	time.sleep(3)
	print("...")
	time.sleep(3)
	print("*WHAP!!*")
	time.sleep(1)
	print("*You were slapped by your boss*")
	time.sleep(3)
	print("You lost your job, and your honor.")