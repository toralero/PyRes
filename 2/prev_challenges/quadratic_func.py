# For this challenge, we need to add the "cmath" library;
# This program will accept a negative discriminant;
import cmath

# Getting the inputs
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Discriminant
disc = b**2 - 4*a*c

# Quadratic formula
x1 = (-b - cmath.sqrt(disc))/(2*a)
x2 = (-b + cmath.sqrt(disc))/(2*a)

# Results
print("The solutions are {0} and {1}".format(x1,x2))
