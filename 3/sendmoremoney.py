for S in range(0,10):
    for E in range(0,10):
        for N in range(0,10):
            for D in range(0,10):
                for M in range(1,10):
                    for O in range(0, 10):
                        for R in range(0, 10):
                            for Y in range(0,10):
                                if (len({S, E, N, D, M, O, R, Y}) >= 8):
                                    n1 = S * 1000 + E * 100 + N * 10 + D
                                    n2 = M * 1000 + O * 100 + R * 10 + E
                                    result = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
                                    if ((n1 + n2) == result):
                                        print("  {0} {1} {2} {3}".format(S,E,N,D))
                                        print("+ {0} {1} {2} {3}".format(M,O,R,E))
                                        print("––––––––––")
                                        print("{0} {1} {2} {3} {4}".format(M,O,N,E,Y))
                                        print("––––––––––")
                                        print()
                                        print("S =", S)
                                        print("E =", E)
                                        print("N =", N)
                                        print("D =", D)
                                        print("M =", M)
                                        print("O =", O)
                                        print("R =", R)
                                        print("Y =", Y)
