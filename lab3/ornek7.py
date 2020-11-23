x=int(input("1.number"))
y=int(input("2.number"))
n=0

while x>=1 or  y>=1:
  
  if x%10==y%10:
    n+=1
    
  x=x//10
  y=y//10
  if x <1 or y<1:
    break
    



print(n)