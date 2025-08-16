def solution(wallpaper):
    answer = []
    lenH=len(wallpaper)
    lenW=len(wallpaper[0])
    minH=lenH; minW=lenW
    maxH=maxW=0
    for i in range(lenH):
        for j in range(lenW):
            if wallpaper[i][j]=='#':
                minH=min(i,minH)
                minW=min(j,minW)
                maxH=max(i+1,maxH)
                maxW=max(j+1,maxW)
    return [minH,minW,maxH,maxW]