import numpy as np
from fractions import Fraction

def form_identity_matrix(r):
    return np.identity(r,dtype=int)

def form_inverse_matrix(m):
    return np.linalg.inv(np.array(m))

def to_fraction(b):
    temp=[]
    for i in b[0]:
        temp.append(Fraction(i).limit_denominator(10).numerator)
    return temp

def split(m):
    transient,terminal=split_states(m)
    q=[]
    r=[]
    for i in transient:
        s=[]
        for j in transient:
            s.append(m[i][j])
        q.append(s)    
    for i in transient:
        s=[]
        for j in terminal:
            s.append(m[i][j])
        r.append(s)    
    return q,r    
        
def split_states(m):
    terminal=[]
    transient=[]
    for i in range(0,len(m)):
        if len(m[0])==m[i].count(0):
            terminal.append(i)
        else:
            transient.append(i)
    return transient,terminal 
    
    
def solution(m):
    q,r=split(m)
    i=form_identity_matrix(len(q))
    minus=i-q
    n=form_inverse_matrix(minus)
    b=np.dot(n,r)
    b=to_fraction(b)
    print('Q',q,'\nR\n',r,'\nIdentity\n',i,'\nminus\n',minus,'\nans\n',b)
    
solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
#print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
