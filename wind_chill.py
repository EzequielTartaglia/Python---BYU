#Formula of wind chill

#Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
#Where,T= Air Temperature (ºF) V= Wind Speed (mph)

#Variables in the formula:
# T is the temperature in degrees Fahrenheit
# V is the wind speed in miles per hour
# V^0.16 means V to the power of 0.16, which can be found in Python using the ** operator.

grades = float(input("What is the temperature? "))

#Function to calcule a wind chill in Fahrenheit
def wind_chill_f(grades,wind_default=0):
    wind_chill = 35.74 + (0.6215 * grades) - 35.75 * (wind_default**0.16) + 0.4275 * grades * (wind_default**0.16)
    return wind_chill

#Function to calcule a wind chill in Celcius
def wind_chill_c(grades,wind_default=0):
    grades_f_to_c = (grades * 1.8) + 32 #9/5 = 1.8
    wind_chill = 35.74 + (0.6215 * grades_f_to_c) - 35.75 * (wind_default**0.16) + 0.4275 * grades_f_to_c * (wind_default**0.16)
    return wind_chill

#Ask for the temperature:
medition = input("Fahrenheit or Celsius (F/C)? ")

if medition == "F":
    print(f'At temperature {grades}, and wind speed 5 mph, the windchill is: {wind_chill_f(grades):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 10 mph, the windchill is: {wind_chill_f(grades,5):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 10 mph, the windchill is: {wind_chill_f(grades,10):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 15 mph, the windchill is: {wind_chill_f(grades,15):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 20 mph, the windchill is: {wind_chill_f(grades,20):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 25 mph, the windchill is: {wind_chill_f(grades,25):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 30 mph, the windchill is: {wind_chill_f(grades,30):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 35 mph, the windchill is: {wind_chill_f(grades,35):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 40 mph, the windchill is: {wind_chill_f(grades,40):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 45 mph, the windchill is: {wind_chill_f(grades,45):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 50 mph, the windchill is: {wind_chill_f(grades,50):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 55 mph, the windchill is: {wind_chill_f(grades,55):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 60 mph, the windchill is: {wind_chill_f(grades,60):.2f} Fº.')

elif  medition == "C":
    print(f'At temperature {grades}, and wind speed 5 mph, the windchill is: {wind_chill_c(grades):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 10 mph, the windchill is: {wind_chill_c(grades,5):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 10 mph, the windchill is: {wind_chill_c(grades,10):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 15 mph, the windchill is: {wind_chill_c(grades,15):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 20 mph, the windchill is: {wind_chill_c(grades,20):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 25 mph, the windchill is: {wind_chill_c(grades,25):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 30 mph, the windchill is: {wind_chill_c(grades,30):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 35 mph, the windchill is: {wind_chill_c(grades,35):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 40 mph, the windchill is: {wind_chill_c(grades,40):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 45 mph, the windchill is: {wind_chill_c(grades,45):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 50 mph, the windchill is: {wind_chill_c(grades,50):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 55 mph, the windchill is: {wind_chill_c(grades,55):.2f} Fº.')
    print(f'At temperature {grades}, and wind speed 60 mph, the windchill is: {wind_chill_c(grades,60):.2f} Fº.')
    

