n,h=map(int,input().split())
m=list(map(int,input().split()))
w=0
for i in m:
  if i <= h:
    w+=1
  else:
    w+=2
print(w)
