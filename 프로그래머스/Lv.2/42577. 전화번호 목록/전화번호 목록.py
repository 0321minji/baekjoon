def solution(phone_book):
    answer = True
    h=set(phone_book)
    for i in phone_book:
        temp=''
        for j in i:
            temp+=j
            if temp in h and temp!=i:
                return False
    
    return answer