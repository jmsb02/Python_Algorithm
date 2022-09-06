def DFS(L):
    global cnt
    if L==m: #우리가 구하고자 하는 값은 res 리스트에 존재
        for j in range(m):
            print(res[j],end=' ')
        print() 
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                res[L]=i
                ch[i]=1
                DFS(L+1)
                ch[i]=0

n, m =map(int,input().split())
res = [0]*m #출력 리스트
ch = [0]*(n+1) #중복 검사 리스트
cnt = 0
DFS(0)
print(cnt)
