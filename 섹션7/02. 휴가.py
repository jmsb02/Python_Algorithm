#패턴 익숙해지기
def DFS(l,sum):
    global res
    if l==n+1:
        if sum>res:
            res=sum
    else:
        if l+pt[l]<=n+1: #현재 날+ 그 날에 걸리는 날이 n+1 넘으면 안 됨
            DFS(l+pt[l],sum+ps[l]) #다음 인덱스 날로 이동, sum 더해줌
        DFS(l+1,sum) #(넣다) 뺐을 때 조n건 = 다음 날로 이동, sum 놔둠

n=int(input())
pt=[]
ps=[]
for _ in range(n):
    a,b=map(int,input().split())
    pt.append(a)
    ps.append(b)
res=-2147000000
pt.insert(0,0)
ps.insert(0,0) #인덱스를 날짜로 볼 것이기 때문에 인덱스 0번 자리에 0 추가
DFS(1,0) #인덱스(1일부터니까 1로 넣기),합계
print(res)

