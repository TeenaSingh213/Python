import csv
with open(r"C:\Users\teena\OneDrive\Desktop\year2017.csv") as file:
    data = csv.reader(file)
    a = list(data)
   
    col = len(a[0])
    for i in  range (col ):
        print(a[0][i])