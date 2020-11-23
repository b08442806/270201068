num= int(input("how many num?"))
n=0
for i in range(num):
  a=int(input("enter integer"))
  if (a%2==0):
    n+=1

x= 100*n/num
print("%",x)