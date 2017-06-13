def fact(n):
    print("*****", n, "th time")
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
fact(6)