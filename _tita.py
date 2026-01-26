import csv
reader = csv.DictReader(open('titanic.csv', 'r'))
titanic = []
for row in reader:
    titanic.append(dict(row))