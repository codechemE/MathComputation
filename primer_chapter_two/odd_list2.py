import numpy as np

y = []


def odd_list(n):
    for i in range(0, n):
        if i % 2 == 1:
            y.append(i)
    print(y)


odd_list(14)
