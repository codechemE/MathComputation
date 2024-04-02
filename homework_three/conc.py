def concentrations(ca0, tau, k1, k2):
    ca = ca0 / (tau * k1 + 1)
    cc = ca0 / (tau * k2 + 1)
    cd = ca0 - cc * k2 * tau
    return [ca, cc, cd]


print(concentrations(2.2, 150, .03833, .075))
