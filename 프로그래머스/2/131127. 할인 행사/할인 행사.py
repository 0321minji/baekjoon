from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    #zip 함수로 묶어줌
    for w, n in zip(want, number):
        check[w] = n
    
    for i in range(len(discount)-9):
        temp = Counter(discount[i:i+10])
        if temp == check:
            answer += 1

    return answer