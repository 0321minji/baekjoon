from itertools import combinations

def solution(orders, course):
    answer = []
    menu={}
    
    for i in course:
        for order in orders:
            for temp in combinations(order,i):
                temp=sorted(temp)
                temp=''.join(temp)
                if temp not in menu:
                    menu[temp]=0
                menu[temp]+=1
    temp={}
    for food, cnt in menu.items():
        if cnt>1:
            temp[food]=cnt

    menu=sorted(temp.items(),key=lambda x:(len(x[0]),-x[1]))
    #return menu
    temp=dict(zip(course,[-1]*len(course)))
    
    for food, cnt in menu:
        if temp[len(food)]<=cnt:
            temp[len(food)]=cnt
            answer.append(food)
    answer.sort()    
    return answer