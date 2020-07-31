import random

cheese_types = ['m', 'p', 'r', 'a']

# Generate random chromosome
def gen_rand_chrom(n):
    mix_list = []
    for i in range(0,n):
        mix_list.append(cheese_types[random.randint(0,3)])

    return mix_list

# Generate a random population
def gen_rand_pop(pop_len=10, chrom_len=10):
    pop_list = []
    for i in range(0, pop_len):
        pop_list.append(gen_rand_chrom(chrom_len))
    return pop_list

# "Mixing" two chromosomes
def crossbreed(chrom1, chrom2):
    if len(chrom1) == len(chrom2):
        cross_point = random.randint(1,len(chrom1)-2)
        offspring1 = chrom1[0:cross_point] + chrom2[cross_point:len(chrom1)]
        offspring2 = chrom2[0:cross_point] + chrom1[cross_point:len(chrom1)]
        return offspring1, offspring2
    else:
        print("Chromosomes didn't match in length")
        return [],[]

# Sort the population by highest score to lowest score
def sort_pop(population, scores):
    result = []
    index_of_order = sorted(range(len(scores)), key=lambda k: scores[k], reverse=True)
    for i in index_of_order:
        result.append(population[i])
    return result, max(scores)

# Removing population not protected by nKeep
def remove_pop(population, n_keep=2):
    result = population[0:n_keep]
    return result

# Repopulate the population
def repopulate(population, pop_len=10):
    new_pop = population[:]
    while len(new_pop) < pop_len:
        # Random selection
        p1i = random.randint(0,len(population)-1)
        parent1 = population[p1i]
        p2i = random.randint(0,len(population)-1)
        while p2i == p1i:
            p2i = random.randint(0,len(population)-1)
        parent2 = population[p2i]
        offspring1, offspring2 = crossbreed(parent1, parent2)
        new_pop.append(offspring1)
        if (len(new_pop) < pop_len):
            new_pop.append(offspring2)
    return new_pop

# Make small change in the chromosome
def mutate(population, mut_rate):
    for i in range(1, len(population)):
        for j in range(0,len(population[i])):
            if random.random() <= mut_rate:
                population[i][j] = cheese_types[random.randint(0,3)]
    return population
