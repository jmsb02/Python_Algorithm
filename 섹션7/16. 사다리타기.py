#사다리타기 -> dfs(깊이 우선 탐색), 열 단위로 체크하면서 1일 때 탐색 들어감
#체크리스트 하나 필요하고, 1을 시작 지점으로 두고 출발 했는데, 2가 없어 -> bfs 넘어가야지, 2가 발견되면 인덱스 출력 시작했던 1의 인덱스

import sys
input = sys.stdin.readline
 
 #사다리가 기본적으로 왼, 오니까 왼,오,위 순으로 체크
dx=[0,0,-1]
dy=[-1,1,0]

def dfs(x,y):
    ch[x][y]=1
    if x==0: #인덱스 왔을 때 
        print(y)
        sys.exit(0)
    else:
        for i in range(3):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<10 and 0<=yy<10 and ch[xx][yy]==0 and ls[xx][yy]==1:
                ch[xx][yy]=1
                dfs(xx,yy)




ls = [list(map(int,input().split())) for _ in range(10)] 
ch = [[0]*10 for _ in range(10)]

#x가 9부터 시작한다는 정보는 있으니 for문 한 번만(y) 돌려서 dfs 호출하면 됨
for y in range(10):
    if ls[9][y]==2:
        dfs(9,y)
