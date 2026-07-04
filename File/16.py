import csv
with open(r"C:\Users\teena\OneDrive\Desktop\year2017.csv") as file:
    data = csv.DictReader(file, skipinitialspace= True)
   
    casualties = []
   
    for row in data:
     
        if row["Weapon_type"] == "Explosives":
            if row["casualities"] != "":
                casualties.append(int(float(row["casualities"])))
    
    print(sum(casualties))
        
              
   
            