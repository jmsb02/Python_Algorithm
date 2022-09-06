#시간초과 문제

def DFS(L,sum,tsum):
    #tsum이란 만약 진행 지점까지의 지나온 원소들이 모두 부분집합에 포함되었을 때의 합계이다
    global result
    if sum+(total-tsum)<result: ########시간복잡도 낮추기
        return 
        #우리가 누적하고 있는 합이랑 구해야 하는 값을 더했는데도 최대값보다 작으면
        #굳이 구할 필요 X
    if sum>c: #시간복잡도 낮추기
        return
    if L==n:
        if sum>result: #최댓값 갱신
            result=sum
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])

c,n = map(int,input().split())
a=[0]*n
result = -2147000000
for i in range(n):
    a[i] = int(input())
total=sum(a)
DFS(0,0,0)
print(result)
