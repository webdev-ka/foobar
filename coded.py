'''https://foobar.withgoogle.com/?eid=UapHB'''
from itertools import combinations
def solution(l):
    l.sort(reverse=True)
    for i in reversed(range(1,len(l)+1)):
        for j in list(combinations(l,i)):#making list combination of len 1 to full length
            if sum(j)%3==0:
                return int("".join(map(str,j)))
            
print(solution([3,1,4,1]))   
print(solution([3,1,4,1,5,9])) 
