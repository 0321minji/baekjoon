
n=int(input())
charge=0
for i in range(n):
    line=input()
    h=int(line[:2])
    m=int(line[3:5])
    d=int(line[6:])

    end_h=h
    end_m=(m+d)%60

    if m+d>=60:
        end_h+=1
        if end_h+1==24:
            end_h=0

    if h==6 and end_h==7:
        charge+=(d-end_m)*5 + end_m*10
    elif h==18 and end_h==19:
        charge+=(d-end_m)*10+end_m*5
    else:
        if 6<h<19:
            charge+=10*d
        else:
            charge+=5*d
print(charge)