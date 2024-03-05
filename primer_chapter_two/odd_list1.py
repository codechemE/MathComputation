import numpy as np

y = []


def odd_array(n):
    m = 1
    y.append(m)

    while m < n:
        m += 2
        if m > n:
            break
        y.append(m)

    print(y)


odd_array(14)
