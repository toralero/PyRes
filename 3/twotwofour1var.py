F = 1
O = 6
U = 9
R = 2
T = 8

for W in range(0,10):
    print("Trying W =", W)
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
   

