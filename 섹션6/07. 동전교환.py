def DFS(L,sum): #개수, 합계
    global res
    if L>res: #CUT - L=3일 때 답이라는 것을 구했는데 그 레벨 밑으로 구할 필요 없음 (최소니까)
        return #DFS(3,15)로 구했다면 ex. DFS(6,15) 얜 필요 없다는 것임
    if sum>m:
        return
    if sum==m: #우리가 구하고자 하는 값이랑 주어진 값이랑 같을 때
        if L<res: 
            res=L
    else:
        for i in range(n):
            DFS(L+1,sum+a[i])
n=int(input())
a= list(map(int,input().split()))
m = int(input())
res=2147000000
a.reverse()
DFS(0,0)
print(res)