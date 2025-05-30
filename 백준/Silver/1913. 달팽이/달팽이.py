import sys
input=sys.stdin.readline

n=int(input())
num = int(input())
graph = [[0 for _ in range(n) ]for _ in range(n)] 

now = n**2

x=0; y=0
goal=n//2
direct =1


while True:
    if (x==goal and y==goal) or now==0 :
        graph[x][y]=now
        break
    if not graph[x][y]:
        graph[x][y]=now
        # print(x,y,now)
        
    else: now+=1
    
    if direct ==2:
        if y+1<n and not graph[x][y+1]:
            y+=1
        else:
            direct=3
    elif direct ==1:
        if x+1<n and not graph[x+1][y]:
            x+=1
        else:
            direct=2
    elif direct ==4:
        if y-1>=0 and not graph[x][y-1]:
            y-=1
        else:
            direct=1
    else:
        if x-1>=0 and not graph[x-1][y]:
            x-=1
        else:
            direct=4
    now-=1

for i in range(n):
    print(*graph[i])

for i in range(n):
    for j in range(n):
        if graph[i][j]==num:
            print(i+1, j+1)