def solution(n, arr1, arr2):
    answer = []
    arr =''
    m=2**n-1
    for i in range(n):
        temp=str(bin(arr1[i]|arr2[i])).zfill(n+2)
        print(temp)
        for t in temp[2:]:
            if t=='1':
                arr+="#"
            else:
                arr+=' '
        answer.append(arr)
        arr=''
                
    return answer