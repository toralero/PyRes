import math

def quadratic_func(a, b, c):
    # Discriminant
    disc = b**2 - 4*a*c

    # Quadratic formula
    x1 = (-b - math.sqrt(disc))/(2*a)
    x2 = (-b + math.sqrt(disc))/(2*a)

    return x1, x2

# Method 2: Receiving output as two seperate variables
r1, r2 = quadratic_func(6, 11, -35)

print("r1 =", r1)
print("r2 =", r2)
print("-------")
print("type(r1) =", type(r1))
print("type(r2) =", type(r2))


