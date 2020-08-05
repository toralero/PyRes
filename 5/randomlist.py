import random

random.seed(22041997)

def random_list(length=10, min=0, max=10):
    result_list = []
    for i in range(0,length):
        result_list.append(random.randint(min,max))
    return result_list

# Using it with all arguments
list_a = random_list(20, 5, 15)

# Using it with only two arguments
list_b = random_list(min=2, max=8)

# Using it with the default arguments
list_c = random_list()

print("list_a =", list_a)
print("list_b =", list_b)
print("list_c =", list_c)

