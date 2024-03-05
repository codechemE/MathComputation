import numpy as np


def extract_data(filename):
    with open(filename, "r") as f:
        f.readline()
        numbers = [float(line.split()[1]) for line in f]
    return numbers


num = extract_data("rainfall.txt")

numpy_numbers = np.array(num)
print(numpy_numbers.mean())