import numpy as np

species_mol_frac = np.array([[7, 18, 15, 24], [3, 25, 10, 65], [55, 41, 55, 9], [35, 16, 20, 2]])

# concatenate the mol frac. vectors into a matrix

# initial flow rate vector a.k.a b vector
fa0 = 80
b = np.array([15, 25, 40, 20]) * fa0
# reminder to self: doing this as a list adds 80 more elements, oops!

if np.linalg.det(species_mol_frac) == 0:
    print("Matrix is singular")
else:
    print("Matrix is not singular")

if np.linalg.cond(species_mol_frac) >= 1000:
    print("Matrix is ill-conditioned")
else:
    print("Matrix is well conditioned")


def degrees_freedom(n, m):
    if n == m:
        print("You will have a unique solution")
    elif n < m:
        print("Too many unknowns, solution will not converge. ")
    else:
        print("You have infinite solutions")


num_eqs = len(b)
num_unknowns = len(species_mol_frac)

degrees_freedom(num_eqs, num_unknowns)

z = np.linalg.solve(species_mol_frac, b)
D2 = z[0], B2 = z[1], D3 = z[2], B4 = z[3]
print(f'D2 is {D2} kg-mol / min')
print(f'B2 is {B2} kg-mol / min')
print(f'D3 is {D3} kg-mol / min')
print(f'B4 is {B4} kg-mol / min')

