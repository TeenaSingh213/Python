import csv
import numpy as np
with open(r"C:\Users\teena\OneDrive\Desktop\terrorismData.csv", mode="r",encoding= 'utf-8') as file :
    data = csv.DictReader(file , skipinitialspace= True)
    date = []
    
    for row in data:
        if row["Day"] !="":
            date.append(int(float(row["Day"])))
    
    date = np.array(date)
    count = np.sum((date >= 10) & (date <= 20))
    print(count)