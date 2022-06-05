#Speed of a Falling Object

import math

    #Header
print('')
print("Welcome to the velocity calculator. Please enter the following:")
    #User inputs
print('')
mass_m = float(input("Mass (in kg): "))
gravity_g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time_t = float(input("Time (in seconds): "))
density_p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sectional_A = float(input("Cross sectional area (in m^2): "))
drag_constant_C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

    #c Formula 
value_of_c =  (1 / 2) * density_p * cross_sectional_A * drag_constant_C
print('')
print(f'The inner value of c is: {value_of_c:.3f}')

    #speed Formula 
value_of_velocity = math.sqrt(mass_m * gravity_g / value_of_c) * (1 - math.exp((-math.sqrt(mass_m * gravity_g * value_of_c) / mass_m) * 10))
print(f'The velocity after {time_t} seconds is: {value_of_velocity:.3f} m/s')
