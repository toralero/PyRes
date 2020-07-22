gallagher_family = {"Sweeny", "Thomas", "Paul", "Liam", "Noel"}

oasis_members = {"Noel", "Liam", "Gem", "Andy"}

print("gallagher_family =", gallagher_family)
print("oasis_members =", oasis_members)

print("-------")
gallagher_diff = gallagher_family.difference(oasis_members)
print("Members of Gallagher which are not in Oasis:", gallagher_diff)

print("-------")
intersection = gallagher_family.intersection(oasis_members)
print("Members which are in Oasis and Gallagher ", intersection)


