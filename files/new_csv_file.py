import csv
with open("starter.txt") as csvFile:
    # csvFile = csv.reader(csvFile, delimiter=",")
    # for row in csvFile:
    #     list(row)
    #     print(row, end = '\n'
    readCSV = csv.reader(csvFile, delimiter = ',')
    names = []
    dorms = []

    for row in readCSV:
        
        dorm = row[2]
        name = row[0]

        names.append(name)
        dorms.append(dorm)

    print(names, dorms, end = '\n')
        # in other for it to print in an identical form the use of dict. is important 

