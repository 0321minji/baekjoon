def solution(arr):
    answer = []
    for i in arr:
        if answer and answer[-1]==i:
            continue
        answer.append(i)
        
    #print('Hello Python')
    return answer