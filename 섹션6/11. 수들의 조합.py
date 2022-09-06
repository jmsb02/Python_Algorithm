def dfs(l,start,sum):
    global cnt
    if l==k: #k개를 뽑아야 하니까 종찹지점
        if sum%m==0: #우리가 구한 sum이 m의 배수이면
            cnt+=1
    else:
        for i in range(start,n): #우리가 저번처럼 1부터가 아니라 ls 사용해서 인덱스 0부터니까 n임
            dfs(l+1,i+1,sum+ls[i])

n,k=map(int,input().split())
ls = list(map(int,input().split()))
m=int(input())
cnt=0
dfs(0,0,0) #인덱스,시작 지점(조합 성질), 누적 합
print(cnt) 