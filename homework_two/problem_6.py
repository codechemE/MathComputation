import time
import numpy as np
from numpy import linalg

t = []


def temperature_engine(time_s, initial_temperature_C):
    return initial_temperature_C * np.exp(-.1 * time_s)


def temperature_simulation(starting_temp,  end_temp, step_size):
    current_temp = temperature_engine()
    while current_temp >= end_temp:
        current_temp -= step_size
        t.append(current_temp)


temperature_simulation(500, 500, 50)
