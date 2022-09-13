n=int(input())
charge=0
for i in range(n):
    s=input()
    s=s.replace(':',' ')
    h,m,ti=map(int,s.split())
    end_h,end_m=h,m

    if ti+m>=60:
        end_m=end_m+ti-60
        end_h+=1
        if end_h>23:
            end_h=0
    else:
        end_m+=ti

    if(end_h==7 or end_h==19) and m>=end_m and end_m!=0:
        if end_h==7:
            charge+=(ti-end_m)*5 + end_m*10
        elif end_h==19:
            charge+=(ti-end_m)*10+end_m*5
    else:
        if 7<=h<=18:
            charge+=ti*10
        else:
            charge+=ti*5

print(charge)
