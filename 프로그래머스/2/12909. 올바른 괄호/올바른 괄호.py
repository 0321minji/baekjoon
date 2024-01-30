def solution(s):
    answer = True
    if s[0]==')' or s[-1]=='(':
        return False
    left=['(']
    for i in range(1,len(s)):
        if s[i]=='(':
            left.append(s[i])
        else:
            if left:
                left.pop()
            else:
                return False
    if left:
        return False
    return True