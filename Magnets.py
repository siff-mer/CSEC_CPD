n=int(input())
result=0
a=""
for i in range (n):
  m=input()
  if a!=m:
    result+=1
  a=m
print(result)
