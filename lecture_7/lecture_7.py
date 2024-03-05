try:
    f = open("XYZ.txt")
    f.write("\n 2000 3000")
except IOError:
    print("Unable to open file")
    f = open("XYZ.txt","a")
    f.write("\n 2000 3000")
else:
    print("The file is writable")

import pandas as pd