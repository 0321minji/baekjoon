import sys
input=sys.stdin.readline

def notchange():
    temp=i-(a+i0)
    after=w0+temp*d
    if after<=0:
        print('Danger Diet')
        return
    print(after,i0)
    return

def change():
    base=i0
    weight=w0
    for _ in range(d):
        temp=i-(a+base)
        weight+=temp
        if weight<=0:
            print('Danger Diet')
            return
        if abs(temp)>t:
            base+=(temp//2)
        if base<=0:
            print('Danger Diet')
            return
    result='NO'
    if i0-base>0:
        result='YOYO'
    print(weight,base,result)
        

w0,i0,t=map(int,input().split())
d,i,a=map(int,input().split())
notchange()
change()
