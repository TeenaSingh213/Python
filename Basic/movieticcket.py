day= input("Enter day of the week:")
age= int(input("Enter your age:"))
ticket_price =12 if age >=18 else 8
if day =="Wednesday":
    ticket_price = ticket_price-2
print("Ticket price is:", ticket_price)


    
    