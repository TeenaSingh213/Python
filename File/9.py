import csv
with open(r"C:\Users\teena\OneDrive\Desktop\year2017.csv") as file:
    data = csv.reader(file)
    a = list(data)
    
    print(a[1:4])