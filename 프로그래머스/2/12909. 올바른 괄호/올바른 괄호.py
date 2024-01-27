def solution(s):
    answer = True
    left=[]
    if s[0]==')' or s[-1] == '(':
        return False
    for i in s:
        if i =='(':
            left.append(i)
        if i==')':
            if left:
                left.pop()
            else:
                return False
    if left:
        return False

    return True