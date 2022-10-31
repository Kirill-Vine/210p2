import math, collections, re, csv

# part 1 & 2

with open('covidTrain.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    f = open('covidResult.csv', 'w+', newline ='')
    writer = csv.writer(f)
    for lines in csvFile:
        splittedLine = str(lines).split(", ")
        # replace dates and age
        age = splittedLine[1].replace('\'','')
        splittedLine[0] = splittedLine[0].replace('\'','')
        splittedLine[0] = splittedLine[0].replace('[','')
        eight = splittedLine[8].replace('\'','')
        nine = splittedLine[9].replace('\'','')
        ten = splittedLine[10].replace('\'','')
        line = []
        line.append(str(splittedLine[0]))

        # if age is a range
        if '-' in age:
            numbers = []
            t = age.split('-')
            numbers += range(int(t[0]), int(t[1]) + 1)
            avg = int(round(sum(numbers) / len(numbers), 0))
            line.append(str(avg))
        else:
            line.append(str(splittedLine[1].replace('\'','')))

        line.append(str(splittedLine[2].replace('\'','')))
        line.append(str(splittedLine[3].replace('\'','')))
        line.append(str(splittedLine[4].replace('\'','')))
        line.append(str(splittedLine[5].replace('\'','')))
        line.append(str(splittedLine[6].replace('\'','')))
        line.append(str(splittedLine[7].replace('\'','')))
        line.append((re.sub(r'(\d{1,2}).(\d{1,2}).(\d{4})', '\\2.\\1.\\3', eight)))
        line.append((re.sub(r'(\d{1,2}).(\d{1,2}).(\d{4})', '\\2.\\1.\\3', nine)))
        line.append((re.sub(r'(\d{1,2}).(\d{1,2}).(\d{4})', '\\2.\\1.\\3', ten)))
        splittedLine[11] = splittedLine[11].replace('\'','')
        splittedLine[11] = splittedLine[11].replace(']','')
        line.append(str(splittedLine[11]))
        # write a row to the csv file
        writer.writerow(line)
        line.clear()
    f.close() 
    file.close()

# part 3
with open('covidTrain.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    latDict =  {}
    longDict = {}
    for lines in csvFile:
        splittedLine = str(lines).split(", ")
        provinceName = splittedLine[4].replace('\'','')
        lat = splittedLine[6].replace('\'','')
        long = splittedLine[7].replace('\'','')
        if lat != 'NaN':
            if lat != 'latitude':
                lat = float(lat)
                if provinceName in latDict:
                    latDict[provinceName].append(lat)
                else:
                    latDict[provinceName] = []
                    latDict[provinceName].append(lat)
        if long != 'NaN':
            if long != 'longitude':
                long = float(long)
                if provinceName in longDict:
                    longDict[provinceName].append(long)
                else:
                    longDict[provinceName] = []
                    longDict[provinceName].append(long)            
file.close()

# part 4
with open('covidTrain.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    totalDict =  {}
    for lines in csvFile:
        splittedLine = str(lines).split(", ")
        provinceName = splittedLine[4].replace('\'','')
        cityName = splittedLine[3].replace('\'','')
        cityName = cityName.replace('"','')
        if cityName != 'NaN':
            if cityName != 'city':
                if provinceName not in totalDict:
                    totalDict[provinceName] = {}
                    totalDict[provinceName][cityName] = 1
                else:
                    if cityName not in totalDict[provinceName]:
                        totalDict[provinceName][cityName] = 1
                    else:
                        totalDict[provinceName][cityName] += 1
    sortedDict = {}
    for provinces in totalDict:
        prov = totalDict[provinces]
        sortedDict = {key: value for key, value in sorted(prov.items())}
    file.close() 

# part 5
with open('covidTrain.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    totalDict1 =  {}
    for lines in csvFile:
        splittedLine = str(lines).split(", ")
        symptoms = splittedLine[11].replace('\'','')
        symptoms = splittedLine[11].replace(']','')
        provinceName = splittedLine[4].replace('\'','')
        symptoms = symptoms.replace("'", "")
        if symptoms != 'NaN':
            if symptoms != 'symptoms':
                if ';' in symptoms:
                    symptomsNew = symptoms.split(";")
                    for all in symptomsNew:
                        all = all.strip()
                        all = all.replace("'", "")
                        if 'fever' in all:
                            all = re.sub(r'\([^)]*\)', '', all)
                            all = all.replace('C', '')
                            all = all.replace('.', '')
                            all = re.sub(" \d+", " ", all)
                            all = all.strip()
                        if provinceName not in totalDict1:
                            totalDict1[provinceName] = {}
                            totalDict1[provinceName][all] = 1
                        else: 
                            if all not in totalDict1[provinceName]:
                                totalDict1[provinceName][all] = 1
                            else:
                                totalDict1[provinceName][all] += 1
                else:
                    if 'fever' in symptoms:
                        symptoms = re.sub(r'\([^)]*\)', '', symptoms)
                        symptoms = symptoms.replace('C', '')
                        symptoms = symptoms.replace('.', '')
                        symptoms = re.sub(" \d+", " ", symptoms)
                        symptoms = symptoms.replace('C', '').strip()
                    if provinceName not in totalDict1:
                            totalDict1[provinceName] = {}
                            totalDict1[provinceName][symptoms] = 1
                    else: 
                        if symptoms not in totalDict1[provinceName]:
                            totalDict1[provinceName][symptoms] = 1
                        else:
                            totalDict1[provinceName][symptoms] += 1
    file.close()

# writing to file, final result
with open('covidTrain.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    f = open('covidResult.csv', 'w+', newline ='')
    writer = csv.writer(f)
    for lines in csvFile:
        splittedLine = str(lines).split(", ")
        symptoms = splittedLine[11].replace('\'','')
        symptoms = splittedLine[11].replace(']','')
        provinceName = splittedLine[4].replace('\'','')
        symptoms = symptoms.replace("'", "")
        age = splittedLine[1].replace('\'','')
        cityName = splittedLine[3].replace('\'','')
        lat = splittedLine[6].replace('\'','')
        long = splittedLine[7].replace('\'','')
        # dates
        eight = splittedLine[8].replace('\'','')
        nine = splittedLine[9].replace('\'','')
        ten = splittedLine[10].replace('\'','')

        splittedLine[0] = splittedLine[0].replace('\'','')
        splittedLine[0] = splittedLine[0].replace('[','')
        line = []
        line.append(str(splittedLine[0]))

        # part 1
        if '-' in age:
            numbers = []
            t = age.split('-')
            numbers += range(int(t[0]), int(t[1]) + 1)
            avg = int(round(sum(numbers) / len(numbers), 0))
            line.append(str(avg))
        else:
            line.append(str(splittedLine[1].replace('\'','')))

        line.append(str(splittedLine[2].replace('\'','')))

        # part 4
        if cityName == 'NaN':
            prov = totalDict[provinceName]
            sortedDict = {key: value for key, value in sorted(prov.items())}
            maxCity = max(sortedDict, key=sortedDict.get)
            line.append(str(maxCity))
        else:
            line.append(str(splittedLine[3].replace('\'','')))

        line.append(str(splittedLine[4].replace('\'','')))
        line.append(str(splittedLine[5].replace('\'','')))

        # part 3
        if lat == 'NaN':
            latAvg = float(round(sum(latDict[provinceName]) / len(latDict[provinceName]), 2))
            line.append(str(latAvg))
        else:
            line.append(str(splittedLine[6].replace('\'','')))
        if long == 'NaN':
            longAvg = float(round(sum(longDict[provinceName]) / len(longDict[provinceName]), 2))
            line.append(str(longAvg))
        else:
            line.append(str(splittedLine[7].replace('\'','')))

        # part 2
        line.append((re.sub(r'(\d{1,2}).(\d{1,2}).(\d{4})', '\\2.\\1.\\3', eight)))
        line.append((re.sub(r'(\d{1,2}).(\d{1,2}).(\d{4})', '\\2.\\1.\\3', nine)))
        line.append((re.sub(r'(\d{1,2}).(\d{1,2}).(\d{4})', '\\2.\\1.\\3', ten)))

        # part 5
        if symptoms == 'NaN':
            prov = totalDict1[provinceName]
            sortedDict = {key: value for key, value in sorted(prov.items())}
            maxSym = max(sortedDict, key=sortedDict.get)
            line.append(str(maxSym))
        else:
            splittedLine[11] = splittedLine[11].replace('\'','')
            splittedLine[11] = splittedLine[11].replace(']','')
            line.append(str(splittedLine[11]))

        writer.writerow(line)
        line.clear()
    f.close() 
    file.close()
