def solution(l):
    for i in range(0,len(l)):
        l[i]=l[i].split('.')
        l[i]=list(map(int,l[i]))
    l.sort()
    for i in range(0,len(l)):
        l[i]=list(map(str,l[i]))
        l[i]='.'.join(l[i])
    return l    
print(solution(["1.1.2","1.0","1","0.1","1.3.3","1.0.12","1.0.2"]))       
