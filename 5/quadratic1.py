import math

def quadratic_func(a, b, c):
    # Discriminant
    disc = b**2 - 4*a*c

    # Quadratic formula
    x1 = (-b - math.sqrt(disc))/(2*a)
    x2 = (-b + math.sqrt(disc))/(2*a)

    return x1, x2

# Method 1: Receiving the output as a tuple
result = quadratic_func(6, 11, -35)

print("result =", result)
print("type(result) =", type(result))


