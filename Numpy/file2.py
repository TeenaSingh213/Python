import csv
with open(r"C:\Users\teena\OneDrive\Documents\year2017.csv") as file:
    data = csv.reader(file, delimiter = "," )
    a = list(data)
    print(a)
    
    i =0
    
    # for row in a:
    #     if i !=3:
    #         print(row) 
    #         print(a[1:])
    #         i+=1      


