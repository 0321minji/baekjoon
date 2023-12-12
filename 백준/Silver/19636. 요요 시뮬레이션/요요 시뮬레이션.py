import sys
input=sys.stdin.readline

def nochange():
    after=w0+(i-(i0+a))*d
    if after<=0:
        print('Danger Diet')
        return
    else:
        print(after,i0)
    
        
def change():
    weight=w0
    base=i0
    for _ in range(d):
        use=base+a
        weight+=(i-use)
        if weight<=0:
            print('Danger Diet')
            return
        if abs(i-use)>t:
            base+=(i-use)//2
        if base<=0:
            print('Danger Diet')
            return
    state='NO'
    if i0-base>0:
        state='YOYO'
    print(weight,base,state)

w0,i0,t=map(int,input().split())
d,i,a=map(int,input().split())

nochange()
change()
