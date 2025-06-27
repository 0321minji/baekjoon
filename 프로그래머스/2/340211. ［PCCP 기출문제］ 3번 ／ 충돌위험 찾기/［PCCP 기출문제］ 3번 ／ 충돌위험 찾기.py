from collections import defaultdict
def solution(points, routes):
    answer = 0
    point_map= {i+1:tuple(p) for i,p in enumerate(points)}
    robot_paths=[]
    max_time=0
    
    def get_path(start,end):
        path=[]
        r1,c1=start
        r2,c2=end
        
        dr = 1 if r1<r2 else -1
        dc = 1 if c1<c2 else -1
        for r in range(r1,r2,dr):
            path.append((r,c1))
        for c in range(c1,c2,dc):
            path.append((r2,c))
        path.append((r2,c2))
        return path
    
    for route in routes:
        path=[]
        for i in range(len(route)-1):
            temp=get_path(point_map[route[i]],point_map[route[i+1]])
            if i!=0:
                temp=temp[1:]
            path.extend(temp)
        robot_paths.append(path)
        max_time=max(len(path),max_time)
    
    for t in range(max_time):
        count=defaultdict(int)
        for path in robot_paths:
            if t<len(path):
                count[path[t]]+=1
        for c in count.values():
            if c>=2:
                answer+=1
    return answer

