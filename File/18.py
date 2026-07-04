import csv
with open (r"C:\Users\teena\OneDrive\Desktop\year2017.csv") as file :
    data = csv.DictReader(file, skipinitialspace= True)
    month_dict = {}
    for row in data:
        month = row["Month"]
        if month not in month_dict:
            month_dict[month] = 0
            
        if row["Killed"] != "":
            month_dict[month] += ((int(float(row["Killed"]))))      
    for key in month_dict :
        print(key , month_dict[key])
  
        