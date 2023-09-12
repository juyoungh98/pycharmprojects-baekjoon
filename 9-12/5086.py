while True:
    a, b = map(int, input().split())
    if a and b != 0:
        if a%b == 0:
            print("multiple")
        elif b%a == 0:
            print("factor")
        else:
            print("neither")
    else:
        break