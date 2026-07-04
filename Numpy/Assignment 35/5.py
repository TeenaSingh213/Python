import csv
import numpy as np
with open (r"C:\Users\teena\OneDrive\Desktop\terrorismData.csv", mode = "r", encoding="utf-8") as file:
    data = csv.DictReader(file, skipinitialspace= True)
    killed = []
    wounded = []
    cities = []
    states = []
    for row in data:
        cities.append(row["City"])
        states.append(row["Country"])
        killed.append(float(row["Killed"]) if row["Killed"] else 0)
        wounded.append(float(row["Wounded"]) if row["Wounded"] else 0)
    cities = np.array(cities)
    killed = np.array(killed)
    states = np.array(states)
    wounded = np.array(wounded)
    casualties = killed + wounded
    
    mask = (states == "India") & (cities != "Unknown")
    cities = cities[mask]
    casualties = casualties[mask]
    city_dict = {}
for city, casualty in zip(cities, casualties):

    if city not in city_dict:
        city_dict[city] = casualty
    else:
        city_dict[city] += casualty
print(city_dict)
sorted_city = sorted(city_dict.items(), key=lambda x: x[1], reverse=True)

for city, casualty in sorted_city[:5]:
    print(city, int(casualty))