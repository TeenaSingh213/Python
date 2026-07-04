import csv
with open(r"C:\Users\teena\OneDrive\Desktop\year2017.csv") as file:
    data = csv.reader(file)
    a = list(data)
    i = 1
    while i<11:
        print(a[i][3])
        i += 1
        