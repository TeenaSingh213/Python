import csv
import numpy as np
with open (r"C:\Users\teena\OneDrive\Desktop\terrorismData.csv", mode = "r", encoding="utf-8") as file:
    data = csv.DictReader(file, skipinitialspace= True)
    casualties = []
    for row in data:
        if row["City"] == "Kargil District" :
            casualties.append(row["Killed"])
            casualties.append(row["Wounded"])
    print(casualties)
    a = np.array(casualties)
    a[a == ""] = "0"
    a = a.astype(float)
    print(a)
    print(sum(a))
            
    

    