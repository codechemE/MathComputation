import csv

import numpy as np

try:
    with open('material_strength.csv', 'r') as file:
        read = csv.reader(file)
        headers = next(read)

        returnDict = {}
        keys = []
        values = []

        for row in read:
            key = row[0]
            value = row[1]

            keys.append(key)
            values.append(value)

            returnDict[key] = value

    total = 0

    for nums in returnDict.values():
        total += int(nums)

    max_index = np.argmax(values)
    print(f'The average UTS value of all samples is {total / len(returnDict)}')
    print(f'The maximum of the UTS_value is {values[max_index]} it corresponds to a Sample Id of {keys[max_index]}')

except FileNotFoundError:
    print(f'The file cannot be found, please check the exact name of your file.')

finally:
    print(f'Program was successful.')
