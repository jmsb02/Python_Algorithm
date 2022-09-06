import sys
def dfs(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                board[xx][yy]=1
                dfs(xx,yy)
                board[xx][yy]=0


dx=[-1,0,1,0]
dy=[0,1,0,-1]
board = [list(map(int,input().split())) for _ in range(7)] #값 넣는 리스트
board[0][0]=1 #첫 번째 값은 무조건 들리니 1로 처리
cnt = 0
dfs(0,0) #(x,y)
print(cnt)