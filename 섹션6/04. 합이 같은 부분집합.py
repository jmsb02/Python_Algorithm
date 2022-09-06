def DFS(L,sum):
    if sum>c:
        return
    if L==n:
        if sum<c:
            result.append(sum)
    else:
        DFS(L+1,sum+ls[L])
        DFS(L+1,sum)


c,n = map(int,input().split())
ls = []
result=[]
for i in range(n):
    ls.append(int(input()))
ls.sort(reverse=True)
DFS(0,0)
print(max(result))