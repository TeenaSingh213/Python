import csv
import numpy as np
with open (r"C:\Users\teena\OneDrive\Desktop\terrorismData.csv", mode = "r", encoding="utf-8") as file:
    data = csv.DictReader(file, skipinitialspace= True)
    casualties = []
   
    states = []
    killed = []
    wounded = []
    for row in data:
    
        states.append(row["State"])
        killed.append(float(row["Killed"]) if row["Killed"] else 0)
        wounded.append(float(row["Wounded"]) if row["Wounded"] else 0)
        if row["State"] in ["Jharkhand", "Odisha", "Andhra Pradesh", "Chhattisgarh"]:

            if row["Killed"] != "":
                casualties.append(float(row["Killed"]))

            if row["Wounded"] != "":
                casualties.append(float(row["Wounded"]))

    print(int(sum(casualties)))

states = np.array(states)
killed = np.array(killed)
wounded = np.array(wounded)
mask = np.isin(states,["Jharkhand", "Odisha", "Andhra Pradesh", "Chhattisgarh"])
casualties = killed + wounded
print(mask)


print(int(np.sum(casualties[mask])))

    




                
            