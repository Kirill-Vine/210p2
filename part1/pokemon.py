# 1. Find out what percentage of fire type pokemon are at or above the
# level 40.
# Your program should write (to a file, see below) the value as 
# follows (replace
# . . . with value):
# Percentage of fire type pokemon at or above level 40 = …
# The value should be rounded off using the round() function. 
# So, for instance,
# if the value is 12.3 (less than or equal to 12.5) you would print 12,
#          but if it
# was 12.615 (more than 12.5), you would print 13, as in:
# Percentage of fire type pokemon at or above level 40 = 13
# Write this string to a file named pokemon1.txt.

import math, collections, re, csv

# opening the CSV file
with open('pokemonTrain.csv', mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)
 
    #total rows in csv file
    totalRows = -1
    
    #count to hold number of pokemons having lvl >=40
    pokemonCount = 0
    
    # displaying the contents of the CSV file
    for lines in csvFile:
        splittedLine = str(lines).split(", ")
        if totalRows != -1:
            pokemonLevel = float(splittedLine[2].replace('\'',''))
            pokemonType = splittedLine[5].replace('\'','').lower()
            if pokemonLevel >= 40.0 and pokemonType == 'fire':
                pokemonCount += 1
        totalRows += 1
        
    file.close()
        
        
    #Calculating Percentage
    pokemonPercentage = round((pokemonCount / totalRows) * 100.0)
    resultString = "Percentage of fire type pokemon at or above level 40 = "+str(pokemonPercentage) + "%\n"
    print(resultString)
    # Opening a file
    file1 = open('pokemon1.txt', 'w')
    file1.write(resultString)
    file1.close()
    




# 2. Fill in the missing “type” column values (given by NaN) by mapping
# them from the corresponding “weakness” values. You will see that typically
# a given pokemon weakness has a fixed type, but there are some exceptions.
# So, fill in the type column with the most common type corresponding to the
# pokemon’s weakness value.
# For example, most of the pokemon having the weakness electric are 
# water type
# pokemon but there are other types too that have electric as 
# their weakness (exceptions in that type). But since water is the 
# most common type for weakness
# electric, it should be filled in.
# In case of a tie, use the type that appears first in alphabetical order.



#initial_count
initialCount = 0

#type-weakness dictionary
typeWeaknessDictionary = {}

# opening the CSV file
with open('pokemonTrain.csv', mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)
    

 
    # displaying the contents of the CSV file
    for lines in csvFile:
        if initialCount > 0:
            splittedLine = str(lines).split(", ")
            pokemonType = splittedLine[4].replace('\'','').lower()

            if pokemonType != 'nan':
                pokemonWeakness = splittedLine[5].replace('\'','').lower()
                keys = typeWeaknessDictionary.keys()
                if pokemonType not in keys:
                    value = [{pokemonWeakness:1}]
                    typeWeaknessDictionary[pokemonType] = value
                else:
                    values =typeWeaknessDictionary.get(pokemonType)
                    listValues = []
                    for value in values:
                        if pokemonWeakness not in value.keys():
                            listValues.append(value)
                            listValues.append({pokemonWeakness:1})
                        else:
                            incrementCountValue = value.get(pokemonWeakness)
                            incrementCountValue = int(incrementCountValue) + 1
                            value[pokemonWeakness] = incrementCountValue
                            listValues.append(value)
                    typeWeaknessDictionary[pokemonType] = listValues
        else:
            initialCount += 1
                        
    file.close()

    
# 3. Fill in the missing values in the Attack (“atk”), Defense (“def”) and
# Hit Points (“hp”) columns as follows:
# Set the pokemon level threshold to 40.
# For a pokemon having level above the threshold (i.e. > 40), 
# fill in the missing
# value for atk/def/hp with the average values of atk/def/hp of pokemon with
# level > 40. So, for instance, you would substitute the missing atk 
# value for
# Magmar (level 44), with the average atk value for pokemon with level > 40.
# Round the average to one decimal place.
# For a pokemon having level equal to or below the threshold (i.e. ≤40), 
# fill
# in the missing value for atk/def/hp with the average values of 
# atk/def/hp of
# pokemon with level ≤40. Round the average to one decimal place.
# After performing #2 and #3, write the modified data to another 
# csv file named
# pokemonResult.csv.




below40atkAvg = 0
below40defAvg = 0
below40hpAvg = 0

above40atkAvg = 0
above40defAvg = 0
above40hpAvg = 0


below40atkSum = 0
below40defSum = 0
below40hpSum = 0

above40atkSum = 0
above40defSum = 0
above40hpSum = 0


below40Count = 0
above40Count = 0

# opening the CSV file
with open('pokemonTrain.csv', mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)
 
    #total rows in csv file
    totalRows = -1
    
    #count to hold number of pokemons having lvl >=40
    pokemonCount = 0
    
    # displaying the contents of the CSV file
    for lines in csvFile:
        splittedLine = str(lines).split(", ")
        if totalRows != -1:
            pokemonLevel = float(splittedLine[2].replace('\'',''))
            if pokemonLevel > 40.0:
                above40Count += 1
                if splittedLine[6].replace('\'','') != 'NaN':
                    above40atkSum += float(splittedLine[6].replace('\'',''))
                if splittedLine[7].replace('\'','') != 'NaN':
                    above40defSum += float(splittedLine[7].replace('\'',''))
                if splittedLine[8].replace('\'','') != 'NaN':
                    above40hpSum += float(splittedLine[8].replace('\'',''))
            elif pokemonLevel <= 40.0:
                below40Count += 1
                if splittedLine[6].replace('\'','') != 'NaN':
                    below40atkSum += float(splittedLine[6].replace('\'',''))
                if splittedLine[7].replace('\'','') != 'NaN':
                    below40defSum += float(splittedLine[7].replace('\'',''))
                if splittedLine[8].replace('\'','') != 'NaN':
                    below40hpSum += float(splittedLine[8].replace('\'',''))
            pokemonCount += 1
        totalRows += 1
        
    file.close()
    
below40atkAvg = round((below40atkSum / below40Count), 1)
below40defAvg = round((below40defSum / below40Count),1)
below40hpAvg = round((below40hpSum / below40Count),1)

above40atkAvg = round((above40hpSum / above40Count),1) 
above40defAvg = round((above40hpSum / above40Count),1) 
above40hpAvg = round((above40hpSum / above40Count),1) 
csvLine = []

# opening the CSV file
with open('pokemonTrain.csv', mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)
 
    #total rows in csv file
    totalRows = -1
    
    #count to hold number of pokemons having lvl >=40
    pokemonCount = 0
    
    f = open('pokemonResult.csv', 'w+', newline='')
    
    # create the csv writer
    writer = csv.writer(f)
    
    # displaying the contents of the CSV file
    for lines in csvFile:
        splittedLine = str(lines).split(", ")
        if totalRows != -1:
            pokemonLevel = float(splittedLine[2].replace('\'',''))
            pokemonType = splittedLine[4].replace('\'','').lower()
            splittedLine[0] = splittedLine[0].replace('\'','')
            splittedLine[0] = splittedLine[0].replace('[','')
            csvLine.append(str(splittedLine[0]))
            csvLine.append(str(splittedLine[1].replace('\'','')))
            csvLine.append(str(splittedLine[2].replace('\'','')))
            csvLine.append(str(splittedLine[3].replace('\'','')))
            if pokemonType != 'nan':
            # write a row to the csv file
                csvLine.append(str(splittedLine[4].replace('\'','')))

            else:
                pokemonWeakness = splittedLine[5].replace('\'','').lower()
                pokemonTypeWeaknessList = typeWeaknessDictionary[pokemonWeakness][0].keys()
                keyString = ""
                for i in pokemonTypeWeaknessList:
                    keyString = i
                    csvLine.append(str(keyString))
            csvLine.append(str(splittedLine[5].replace('\'',''))) 


            if pokemonLevel > 40.0:
                if splittedLine[6].replace('\'','') == 'NaN':
                    csvLine.append(str(above40atkAvg))
                else:
                    csvLine.append(str(splittedLine[6].replace('\'','')))  

                if splittedLine[7].replace('\'','') == 'NaN':
                     csvLine.append(str(above40defAvg))
                else:
                    csvLine.append(str(splittedLine[7].replace('\'',''))) 

                if splittedLine[8].replace('\'','') == 'NaN':
                    csvLine.append(str(above40hpAvg))
                else:
                    csvLine.append(str(splittedLine[8].replace('\'','')))
                splittedLine[9] = splittedLine[9].replace('\'','')
                splittedLine[9] = splittedLine[9].replace(']','')
                csvLine.append(str(splittedLine[9]))
                # write a row to the csv file
                writer.writerow(csvLine)
                csvLine.clear()
            
            elif pokemonLevel <= 40.0:
                if splittedLine[6].replace('\'','') == 'NaN':
                    csvLine.append(str(below40atkAvg))
                else:
                    csvLine.append(str(splittedLine[6].replace('\'','')))

                if splittedLine[7].replace('\'','') == 'NaN':
                    csvLine.append(str(below40defAvg))
                else:
                    csvLine.append(str(splittedLine[7].replace('\'',''))) 

                if splittedLine[8].replace('\'','') == 'NaN':
                    csvLine.append(str(below40hpAvg))
                else:
                    csvLine.append(str(splittedLine[8].replace('\'','')))
                splittedLine[9] = splittedLine[9].replace('\'','')
                splittedLine[9] = splittedLine[9].replace(']','')
                csvLine.append(str(splittedLine[9]))
                # write a row to the csv file
                writer.writerow(csvLine)
                csvLine.clear()
                
           
        else:
            # write a row to the csv file
            writer.writerow(lines)
            
            pokemonCount += 1
        totalRows += 1
    
    f.close()
    file.close()
    
        
    




# 4. Create a dictionary that maps pokemon types to their personalities.
# This dictionary would map a string to a list of strings. For example:
# { "fire": ["docile", "modest", ...],
# "normal": ["mild", "relaxed", ...], ...}
# Note: You can create an empty default dictionary of list with defaultdict(list).
# Your dictionary should have the keys ordered alphabetically, and also items
# ordered alphabetically in the values list, as shown in the example above.
# Print the dictionary in the following format:
# Pokemon type to personality mapping:
# normal: mild, relaxed, ...
# fire: docile, modest, ...
# …
# Write the dictionary to a file named pokemon4.txt.



#initial_count
initialCount = 0

#type-weakness dictionary
typeWeaknessDictionary = {}

# opening the CSV file
with open('pokemonResult.csv', mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)
    

    listValues = []
    # displaying the contents of the CSV file
    for lines in csvFile:
        if initialCount > 0:
            splittedLine = str(lines).split(", ")
            pokemonType = splittedLine[4].replace('\'','').lower()
            if pokemonType != 'nan':
                pokemonPersonality = splittedLine[3].replace('\'','').lower()
                keys = typeWeaknessDictionary.keys()
                if pokemonType not in keys:
                    value = [pokemonPersonality]
                    typeWeaknessDictionary[pokemonType] = value

                else:
                    values = typeWeaknessDictionary.get(pokemonType)
                    values.sort()
                    if pokemonPersonality not in values:
                        values.append(pokemonPersonality)
                    typeWeaknessDictionary[pokemonType] = values

                    
        else:
            initialCount += 1
        
    
    file.close()
    sorted_keys = sorted(typeWeaknessDictionary.keys())
    sorted_dict = {key:typeWeaknessDictionary[key] for key in sorted_keys}
    
    # Opening a file
    file1 = open('pokemon4.txt', 'w+')
    file1.write('Pokemon type to personality mapping:\n\n')
    for key in sorted_dict:
        line = str(key) + ": "
        values = sorted_dict[key]
        for value in values:
            line += value + ", "
        line = line[:len(line)-2]
        line += '\n'
        file1.write('\t' + line)
        line = ""
    file1.close()

    
# 5. Find out the average Hit Points (“hp”) for pokemon of stage 3.0.
# Your program should print the value as follows (replace . . . with value):
# Average hit point for pokemon of stage 3.0 = …
# You should round off the value, as in #1 above.
# Write this to a file named pokemon5.txt.


# opening the CSV file
with open('pokemonResult.csv', mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)
 
    #total rows in csv file
    totalRows = -1
    
    #count to hold number of pokemons having lvl >=40
    pokemonStageThreeCount = 0
    
    #Sum of hp
    pokemonStageThreeHpSum = 0
    
    # displaying the contents of the CSV file
    for lines in csvFile:
        splittedLine = str(lines).split(", ")
        if totalRows != -1:
            splittedLine[9] = splittedLine[9].replace('\'','')
            splittedLine[9] = splittedLine[9].replace(']','')
            pokemonStage = float(splittedLine[9])
            pokemonHp = float(splittedLine[8].replace('\'',''))
            if pokemonStage == 3 :
                pokemonStageThreeHpSum += pokemonHp
                pokemonStageThreeCount += 1
            
        totalRows += 1
        
    file.close()
        
    #Calculating Percentage
    divide = (pokemonStageThreeHpSum / pokemonStageThreeCount)
    pokemonPercentage = round( divide,1)
    resultString = "Average hit point for pokemon of stage 3.0 = "+str(pokemonPercentage) + "%\n"
    print(resultString)
    # Opening a file
    file1 = open('pokemon5.txt', 'w')
    file1.write(resultString)
    file1.close()
