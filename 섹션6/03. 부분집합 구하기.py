def DFS(v):
    if v==n+1: #ex.DFS(4)
        for i in range(1,n+1): #인덱스 1부터 봐야 함
            if ch[i]==1: #이때 값이 1이면 
                print(i,end=" ") #출력을 해줌
    else:
        ch[v]=1 #
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

n=int(input())
ch = [0]*(n+1) #원소를 사용하는지 사용하지 않았는지 확인하는 체크 변수
DFS(1) #1부터 호출