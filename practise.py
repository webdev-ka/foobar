import time
l={}
start_time=time.time()
n=int(input())
l=[int(x) for x in input().split()]
l.sort()
print(l[n-1]*l[n-2])
print('Duration:{}seconds'.format(time.time()-start_time))
