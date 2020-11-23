n= (int(input("how many number will you write?")))
maxnumber= (int(input("enter first number?")))
for i in range(n-1):
 x=int(input("enter number"))
 if x>maxnumber:
   maxnumber=x
print ("max value",maxnumber)