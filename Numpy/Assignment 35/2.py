import csv
import numpy as np
with open(r"C:\Users\teena\OneDrive\Desktop\terrorismData.csv", mode="r",encoding= 'utf-8') as file :
    data = csv.DictReader(file , skipinitialspace= True)
    date = []
    attack = []
    

    for month in data:
        if month["Month"] == "1":
            if month["Day"] !="":
                date.append(int(float(month["Day"])))
            
    
    
    date = np.array(date)
    count = np.sum((date >=1) & (date <= 31))
    print(count)