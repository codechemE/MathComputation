import datetime

molecule = {"species": ["0", "H", "H"], "coords": [[0.0, 0.0, 0.0], [0.75, 0.0, 0.0, 0.54], [0.75, 0.0, -.54], [0.75
    , 0.0, -0.54]], "charge": [-0.5, 0.24, 0.25]}

if "species" in molecule:
    print(molecule["species"])

#  molecule.update({"species": ["S","O","O"]})

for x in molecule:
    print(x, molecule[x])

for x, y in molecule.items():
    print(x, y)

lab_notebook = {"experiment1": {"date": datetime.datetime(2024, 2, 1),
                                "measurement": "conductivity",
                                "result": "0.05muS/cm"},
                "experiment2": {"date": datetime.datetime.now(),
                                "measurement": "viscosity",
                                "result": "0.89 Cp"}}
print(lab_notebook.keys())

print(lab_notebook["experiment1"]["measurement"])
