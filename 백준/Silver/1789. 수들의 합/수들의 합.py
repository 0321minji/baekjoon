import math
limit=math.sqrt(2*4294967295)
#print(limit)
s=int(input())
if s==1:
    print(1)
    exit()
for i in range(1,int(limit)+2):
    temp=(i*(i+1))/2
    if temp>s:
        print(i-1)
        break
