from numba import jit, cuda
import numpy as np
import time


def fit_curve_fit_cpu():
    start = time.time()
    x = np.array([1, 1.5, 2, 2.5], dtype=float)
    y = np.array([55, 22, 13, 10])
    sols = np.polyfit(x, y, 2)
    end = time.time()
    print(f"Without GPU: {end- start}")


@jit(target_backend='cuda')
def fit_curve_gpu():
    start = time.time()
    x = np.array([1, 1.5, 2, 2.5])
    y = np.array([55, 22, 13, 10])
    sols = np.polyfit(x, y, 2)
    end = time.time()
    print(f"With GPU: {end - start}")


def main() -> int:
    fit_curve_gpu()
    fit_curve_fit_cpu()
    return 0


if __name__ == "__main__":
    main()
