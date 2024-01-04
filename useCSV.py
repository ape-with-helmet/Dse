import csv
with open('test.csv','r') as f:
    reader = csv.reader(f,delimiter=',')
    for row in reader:
        name=row[0]
        location=row[1]
        profit=row[2]
        print(f"Name: {name}")
        print(f"Profit: ${profit}")
        print(f"Location: {location}")
        print()