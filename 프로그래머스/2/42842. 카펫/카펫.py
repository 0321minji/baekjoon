def solution(brown, yellow):
    answer = []
    total = brown+yellow
    
    for i in range(1,total//2):
        print(i,total//i)
        temp= total//i
        if (i-2)*(temp-2)==yellow:
            return [temp,i]

    return answer