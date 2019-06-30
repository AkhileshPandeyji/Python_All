import csv

dates_list = list()
color_list = list()

with open('example.csv') as csvFile:
    csvData = csv.reader(csvFile,delimiter=',')
    for row in csvData:
        print(row)
        print(row[0],row[1],row[2],row[3])
        dates_list.append(row[0])
        color_list.append(row[3])



print(dates_list)
print(color_list)


index = int(input('Which color u want?'))
print(color_list[index])
csvFile.close()