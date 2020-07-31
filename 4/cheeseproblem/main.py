from scoresim import *
from geneticalg import *

# PARAMETERS
pop_len = 500
chrom_len = 100
mut_rate = 0.2
n_keep = 10
iterations = 1000

# STEP 1 – INITIALIZE RANDOM POPULATION
population = gen_rand_pop(pop_len, chrom_len)

print("The initial population:")
for n, chrom in enumerate(population):
    print("C{0}: {1}".format(n,chrom))
print("-------")

for i in range(0,iterations):
    
    # STEP 2 – RUN SIMULATION AND GET INITIAL SCORES
    scores = batch_calc(population)

    # STEP 3 – RANK POPULATION BASED ON SCORE
    population, high_score = sort_pop(population, scores)

    # STEP 4 – REMOVE THE LOSERS
    population = remove_pop(population, n_keep)

    # STEP 5 – REPOPULATE
    population = repopulate(population, pop_len)

    # STEP 6 – MUTATE
    population = mutate(population, mut_rate)

    print("{0} iteration highest score: {1}".format(i+1, high_score))

scores = batch_calc(population)
population, high_score = sort_pop(population, scores)

print("RESULTS")
print("Highest profit: ${0}".format(high_score))
print("MIX:")
print("Mozarella:", population[0].count('m'))
print("Provolone:", population[0].count('p'))
print("Romano:", population[0].count('r'))
print("Asiago:", population[0].count('a'))
print("FLAVOUR PROFILE:")
profile = calculate_final_profile(population[0])
print("OTHER STATS:")
score, manufacture_price, volumes = calculate_score(population[0])
print("Price per 10kg of Mix:", manufacture_price)
print("Amount bought by China ($100/pc):", volumes['ch'])
print("Amount bought by Switzerland ($200/pc):", volumes['sw'])
print("Amount bought by United States ($90/pc):", volumes['us'])

