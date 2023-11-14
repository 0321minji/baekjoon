import sys
input=sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0]]

def solve(a,b,k):
    st=[[a,b]]
    count=0
    while st:
        x,y=st.pop()
        for a,b in move:
            nx=x+a; ny=y+b;
            if 0<=nx<n and 0<=ny<n and apart[nx][ny]==k:
                st.append([nx,ny])
                apart[nx][ny]=0
                count+=1
                
    return count
    
n=int(input())

apart=[list(map(int,list(input().rstrip()))) for _ in range(n)]

result=[]
for i in range(n):
    for j in range(n):
        if apart[i][j]:
            temp=solve(i,j,apart[i][j])
            if not temp:
                result.append(1)
            else:
                result.append(temp)
result.sort()
print(len(result),*result,sep='\n')
