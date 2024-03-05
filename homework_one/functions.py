import numpy as np

'''' The following program converts from degrees Celsius to degrees Fahrenheit'''


def c_to_f(celsius):
    return 1.8 * celsius + 32


'''' The following program converts from degrees Fahrenheit to degrees Celsius '''


def f_to_c(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def kinetic_energy(mass, velocity):
    return float(.5) * float(mass) * float(velocity) ** 2


def potential_energy(mass, g, height):
    return float(mass) * float(g) * float(height)


def temperature():
    print("This program converts between degrees C and degrees F, you tell it what temperature scale you're using "
          "and it converts it to the corresponding temperature scale")

    input_scale = input("What is the temperature scale? type the character F or C ")
    input_num = float(input("What is the number you are converting? "))

    if input_scale == 'f':
        print("You are converting from Fahrenheit to Celsius")
        result = f_to_c(input_num)
        print(f'It is {result} degrees Celsius.')

    elif input_scale == 'c':
        print("You are converting from Celsius to Fahrenheit")
        result_1 = c_to_f(input_num)
        print(f'It is {result_1} degrees Fahrenheit.')


def trajectory():
    v_0 = input("What is the initial velocity of your projectile in meters per second? (as a float) ")
    theta = input("What is your launch angle relative to the horizontal? (as a float) ")
    g = input("What is the gravitational constant on your planet? (as a float) ")

    max_height = (float(v_0)) ** 2 * np.sin(float(theta)) ** 2 / (2 * float(g))
    horizontal_range = float(v_0) ** 2 * np.sin(2 * float(theta)) / float(g)
    print("Your max_height is: " + str(max_height))
    print("Your horizontal_range is: " + str(horizontal_range))
    return max_height, horizontal_range


def pe_ke_energy():
    print("Hello, I am program that calculates the kinetic and potential energies of an object")
    print("I need three variables to do this, the mass in kilograms, the velocity in meters per second "
          "and the height above the ground in meters")
    mass = float(input("Please input the mass: "))
    velocity = float(input("Please input the velocity: "))
    height = float(input("Please input your height: "))
    grav_constant = float(input("Please input your gravitational constant "))
    ke = kinetic_energy(mass, velocity)
    pe = potential_energy(mass, height, grav_constant)

    print(f'Your particle has a potential energy of {pe} Joules.')
    print(f'Your particle has a kinetic energy of {ke} Joules')


temperature()
pe_ke_energy()
trajectory()
