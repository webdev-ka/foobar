def solution(start,length):
    l=0
    for i in range(length,0,-1):
        j=i
        while j>0:
            
            l=l^start
            start+=1
            j-=1
        start+=(length-i)
        
    return l        
print(solution(17,4))            
print(solution(0,3))
print(solution(4,1))
