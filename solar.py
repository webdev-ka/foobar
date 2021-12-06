def solution(l):
    m=[]
    for i in range((int)(l**0.5),1,-1):
        if i**2<=l:
            l=l-(i*i)
            m.append(i*i)
    if l!=0:
        while l>0:
            m.append(1)
            l=l-1            
    return m
print(solution(12))
