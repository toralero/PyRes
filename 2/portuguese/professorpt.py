import random

score = random.randint(0, 100)

print("Recebeste a seguinte nota:", score)
print("Professor:")

if score >= 90:
    print("Muito bem! Continua assim!")
elif score < 90 and score >= 70:
    print("Bom resultado, mas consegues melhorar!")
elif score < 70 and score >= 50:
    print("Vais ter de te dedicar mais, mas passaste!")
else:
    print("Lamento muito, mas chumbaste.")

