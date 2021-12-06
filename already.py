'''This function converts number in any base b to decimal numbers '''
def to_decimal(n,b):
    j=len(n)-1
    p=0
    for i in range(0,len(n)):
        p+=int(n[i])*(b**j)
        j-=1
    return p
'''This function converts decimal numbers to number in any base b
        keep dividing number by b and store remainder in string r
        and return reversed string
'''
def to_base_b(n,b):
        
        r=str()
        while(n>0):
                r+=str(n%b)
                n=n//b
        return r[::-1]

def subtract(n,b):
        n=[num for num in n] #change string to string list
        x=sorted(n,reverse=True)#sorting the list in descending and converting it back to int
        y=sorted(n)
        x="".join(x)
        y="".join(y)
        if b==10:
             return int(x)-int(y)
        else:
              return to_base_b((to_decimal(x,b)-to_decimal(y,b)),b)
    
        

def solution(n,b):
    z=n    
    result=[]
    while z not in result:
            result.append(z)
            z=str(subtract(z,b))
            z=(len(n)-len(z))*'0'+z

    print('result',result,'z',z)
    return len(result)-result.index(z)      
 
print(solution('210022',3))
print(solution('1221',10))


