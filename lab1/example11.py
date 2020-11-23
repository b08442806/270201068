age = int(input("how old are you?"))
ticket= 3
new_ticket=3
if 0<=age<6 or age>60:
 new_ticket= 0

elif 6<=age<=18:
   new_ticket= ticket/2 
else:
  ticket=3
  

print(new_ticket)