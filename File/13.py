import csv
with open(r"C:\Users\teena\OneDrive\Desktop\year2017.csv") as file:
    data = csv.reader(file, skipinitialspace= True)
    a = list(data)
    
    wounded =[]
    for row in a[1:]:
        v = row[10]
        if v != "":
            wounded.append(int(float(v)))
    
    print(sum(wounded))