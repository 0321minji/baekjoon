def solution(s):
    answer = ''
    words=['zero','one','two','three','four','five','six','seven','eight','nine']
    temp=''

    for word in s:
        if word.isdigit():
            answer+=word
        else:
            temp+=word
            if temp in words:
                answer+=str(words.index(temp))
                temp=''
                    
    return int(answer)