T=int(input())
for i in range(T):
    N,s,e,k = map(int,input().split())
    L = list(map(int,input().split()))
    result = L[s-1:e]
    result.sort()
    print("#%d %d"%(i+1,result[k-1]))
