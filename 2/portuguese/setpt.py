gallagher_family = {"Sweeny", "Thomas", "Paul", "Liam", "Noel"}

oasis_members = {"Noel", "Liam", "Gem", "Andy"}

print("gallagher_family =", gallagher_family)
print("oasis_members =", oasis_members)

print("-------")
gallagher_diff = gallagher_family.difference(oasis_members)
print("Membros de Gallagher que não estão no Oasis: ", gallagher_diff)

print("-------")
intersection = gallagher_family.intersection(oasis_members)
print("Membros que estão no Oasis e na família Gallagher: ", intersection)


