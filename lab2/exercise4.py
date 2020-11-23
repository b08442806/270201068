a=int(input())
x=a
if a==0:
  print("0!:1")
else:
 for i in range(1,a):
   a=a-1
   x*=a
   print(x)
