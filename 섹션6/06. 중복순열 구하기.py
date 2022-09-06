import sys
input = sys.stdin.readline

def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j],end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1) # DFS - 재귀 - 스택과의 연계성
                     # 출력과 호출 동시에 x


n, m = map(int,input().split())
res = [0]*m #값을 책정하기 위한 리스트
cnt = 0 
DFS(0)
print(cnt) #마지막에 cnt 구해야 해서
