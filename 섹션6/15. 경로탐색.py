def DFS(l): #노드번호
    global cnt
    if l==n:
        cnt+=1
    else:
        for i in range(1,n+1):
            if g[l][i]==1 and ch[i]==0: #먼저 갈 수 있느냐 #중첩 안되냐
                ch[i]=1
                DFS(i) #l에서 i로 넘어가니 i 호출
                ch[i]=0


n,m = map(int,input().split())
g=[[0]*(n+1) for _ in range(n+1)] #2차원리스트로 풂
ch = [0]*(n+1) #중복제거리스트
for i in range(m):
    a,b=map(int,input().split())
    g[a][b]=1 #먼저 1로 설정하고 DFS 함수에서 처리 #방향그래프 설정
cnt=0
ch[1]=1 #1부터 돌꺼니까 먼저 1로 설정(체크하고)
DFS(1) #1로 시작
print(cnt)