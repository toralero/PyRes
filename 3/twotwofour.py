for T in range(1,10):
    for W in range(0,10):
        for O in range(0,10):
            for F in range(1,10):
                for U in range(0,10):
                    for R in range(0,10):
                        if len({T, W, O, F, U, R}) >= 6:
                            n = T * 100 + W * 10 + O
                            res = F * 1000 + O * 100 + U * 10 + R
                            if (n + n == res):
                                print("-------")
                                print("Found a solution!")
                                print("  {0} {1} {2}".format(T,W,O))
                                print("+ {0} {1} {2}".format(T,W,O))
                                print("–––––––")
                                print("{0} {1} {2} {3}".format(F,O,U,R))
                                print("-------")
                                print("T =", T) 
                                print("W =", W)
                                print("O =", O)
                                print("F =", F)
                                print("U =", U)
                                print("R =", R)


