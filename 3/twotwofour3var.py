F = 1
R = 4
T = 8

for W in range(0,10):
    for U in range(0, 10):
        for O in range(0, 10):
            print("Trying for W =", W, "and U =", U, "and O =", O)
            if len({T, W, O, F, U, R}) >= 6:
                n = T * 100 + W * 10 + O
                res = F * 1000 + O * 100 + U * 10 + R
                if (n + n == res):
                    print("-------")
                    print("Found a Solution!")
                    print("  {0} {1} {2}".format(T,W,O))
                    print("+ {0} {1} {2}".format(T,W,O))
                    print("–––––––")
                    print("{0} {1} {2} {3}".format(F,O,U,R))
                    print("-------")


