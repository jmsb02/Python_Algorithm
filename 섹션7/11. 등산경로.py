#등산경로
#최솟값 지점(sx,sy)과 최댓값 지점(ex,ey)를 먼저 구했어야 함
import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and ovl[xx][yy]==0:
                if board[xx][yy]>board[x][y]: 
                    ovl[xx][yy]=1
                    dfs(xx,yy)
                    ovl[xx][yy]=0

n = int(input())
board = [[0]*n for _ in range(n)] #옮겨적을 곳 (최소, 최대 구해야 해서)
ovl = [[0]*n for _ in range(n)] #중복 제거 리스트
max = -2147000000
min = 2147000000
for i in range(n): #5
    tmp = list(map(int,input().split()))
    for j in range(n): #5
        if tmp[j]<min:
            min=tmp[j]
            sx = i
            sy = j
        if tmp[j]>max:
            max=tmp[j]
            ex = i 
            ey = j
        board[i][j]=tmp[j] #한 줄 씩 옮겨 적음
#그럼 여기까지 min,max에 누적되어 sx,sy(start) 와 ex, ey(end) 지점을 구함
ovl[sx][sy]=1
cnt=0
dfs(sx,sy)
print(cnt)