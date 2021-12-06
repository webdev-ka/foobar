def solution(a):
    if(len(a)==a.count(0)):
        return "0"
    elif len(a)==1:
        return str(a[0])
    elif a.count(0)==len(a)-1:
        for i in a:
            if i!=0:
                if i<0:
                    return "0"
                elif i>0:
                    return str(i)
    else:
        minimum=min(a)
        b=0
        a=list(filter(lambda i: i != 0, a))
        for i in a:
            if i<0:
                b=b+1
                minimum=max(minimum,i)        
        m=1
        for i in a:
            m*=i
               
        if b%2!=0:
            m//=minimum
        return str(m)    

print(solution([-2]))
print(solution([2,3,2,2]))
print(solution([-2,-2,-3]))
print(solution([-2,-2,-2,-3]))
print(solution([-2,-2,0,0,-2,-3]))
print(solution([2,3,0,0,2,2]))
print(solution([-2,-2,0,0,2,3]))
print(solution([0,0]))
