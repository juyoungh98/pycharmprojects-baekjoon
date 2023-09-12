while True:
    n = input()
    if int(n) > 2:
        n = int(n)
        factor = []
        for i in range(1, int(n/2) + 1):
            if n%i == 0:
                factor.append(i)
        if sum(factor) == n:
            print("%d = " %(n), end='')
            for j in range(len(factor)):
                if j == len(factor) - 1:
                    print("%d" % (factor[j]))
                else:
                    print("%d + " %(factor[j]), end='')
        else:
            print("%d is NOT perfect." %(n))
    else:
        break