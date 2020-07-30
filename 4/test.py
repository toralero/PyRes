from scoresim import *
from geneticalg import *
# 'm' = Mozarella
# 'p' = Provolone
# 'r' = Romano
# 'a' = Asiago
# calculateScore(mix)
# calculateFinalProfile(mix)
test_profile = ['m', 'r', 'r', 'r', 'r', 'r', 'r', 'm', 'r', 'a']

print(gen_rand_pop(3))

test_pop = []

test_pop.append(generate_random_chrom(10))
test_pop.append(generate_random_chrom(10))

print("Chromosome1:", test_pop[0])
print("Chromosome2:", test_pop[1])

os1, os2 = crossbreed(test_pop[0],test_pop[1])

test_pop.append(os1)
test_pop.append(os2)

print("Offspring 1:", os1)
print("Offspring 2:", os2)
print("Batch calculation:")
scores = batch_calc(test_pop)
print(scores)
sorted_pop = sort_pop(test_pop, scores)
reduced_pop = remove_pop(sorted_pop, 2)
repopulated_pop = repopulate(reduced_pop, 10)
print("REPOPULATED:")
for chrom in repopulated_pop:
    print(chrom)
print("MUTATED:")
mutated_pop = mutate(repopulated_pop, 0.2)
for chrom in mutated_pop:
    print(chrom)
