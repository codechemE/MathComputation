import time
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

times = []
T = []


def temperature_engine(time_s, initial_temperature_C):
    return initial_temperature_C * np.exp(-.1 * time_s)


def temperature_simulation(starting_temp, end_temp, step_size):
    current_temp = starting_temp
    t0 = 0

    while current_temp >= end_temp:
        t0 = t0 + step_size
        times.append(t0)
        current_temp = temperature_engine(t0, starting_temp)
        T.append(current_temp)


temperature_simulation(500, 50, step_size=.1)
print(f'It takes {times[-1]} seconds to reach a temperature of {T[-1]} degrees Celsius')
