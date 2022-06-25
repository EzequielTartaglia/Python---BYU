identified = 0

interest_country = ""
interest_country_abreviation = ""
interest_year = 0
average_life_expectancy = 0
average_life_expectancy_min = 9999
interest_id = 0

print('')
interest_year = int(input("Enter the year of interest: ")) #The user put an specific year to know 
print('')

#Open the file life-expectancy.csv
with open("life-expectancy.csv") as life_expectancy_file:
    next(life_expectancy_file, None)

     ## Create an empty list
    output = []
    interest = []
    #each data's line
    for data in life_expectancy_file:
        identified += 1
            #Divide in parts ["Afghanistan", "AFG" , "1953", "29.351"]
        clean_data = data.strip()
        parts_line = data.split(",")
            
            
            #Variables 
        country = parts_line[0]
        country_abbreviation = parts_line[1]
        year = int(parts_line[2])
        life_expectative = float(parts_line[3])
        
            #Variables for the choosen year 
        if interest_year == year:
            average_life_expectancy = life_expectative 
            interest_country = country
            interest_country_abreviation = country_abbreviation
            interest_id = identified
            average_life_expectancy_min = life_expectative
            
            # Append to the list each data's line
            output.append([country, country_abbreviation, year, life_expectative,identified])
            # Append to the list for the year selected
            interest.append([interest_country,interest_country_abreviation,interest_year,average_life_expectancy,average_life_expectancy_min,interest_id])

            #When the user put a number out of range (year)
        elif interest_year > 2019 or interest_year < 1950:
            print('Sorry, the data base is only between the years 1950-2019. Please, try to choose a year between these years')
            print('')
            interest_year = int(input("Enter the year of interest: ")) #The user put an specific year to know 
            print('')

#Create the variables           
max_life = max(output, key=lambda x: x[3])
min_life = min(output, key=lambda x: x[3])
max_life_year = max(interest, key=lambda x: x[3])
min_life_year = min(interest, key=lambda x: x[4])

#General

#The overall max life expectancy
print(f'The overall max life expectancy is {max_life[3]:.2f} in {max_life[0]}')    
#The overall min life expectancy
print(f'The overall min life expectancy is {min_life[3]:.2f} in {min_life[0]}')
print('')

#Year selected prints
print(f'For the year {interest_year}:')
print('')

#Print max life expectancy in this year
print(f'The max life expectancy was in {max_life_year[0]} with {max_life_year[3]:.2f}')    

#Print min life expectancy in this year 
print(f'The min life expectancy was in {min_life_year[0]} with {min_life_year[4]:.2f}')    
print('')


