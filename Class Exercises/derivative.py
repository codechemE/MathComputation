import numpy as np


def derivative(f, x, ha):
    dfa = (f(x + ha) - f(x - h)) / (2 * ha)
    ddfa = (f(x - ha) - 2.0 * f(x) + f(x + ha)) / (ha ** 2)
    return dfa, ddfa


for k in range(1, 15):
    h = 10 ** -k
    df, ddf = derivative(np.arctan, 0.5, h)
    print(df, ddf)

