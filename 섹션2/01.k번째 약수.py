import sys
# sys.stdin = open("input.txt","rt")
n,k = map(int,input().split())
L=[]
for i in range(1,n+1):
    if n%i==0:
        L.append(i)
    else:
        pass
L.sort()
if len(L) >=k:
    print(L[k-1])
else:
    print(-1)
