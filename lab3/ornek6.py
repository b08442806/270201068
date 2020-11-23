num=int(input("how many number?"))
fibo=[0,1]
for i in range (num+1):
  a=fibo[i]+fibo[i+1]
  fibo.append(a)
print(fibo[1:num+1])
  

  
  


