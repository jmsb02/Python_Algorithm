dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global cnt
    ls[x][y]=0 #다시 같은 곳으로 가면 안되기 때문에 0으로 초기화 해줌
    cnt+=1 #들렸으니까 1 더해주고
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and ls[xx][yy]==1: #12,3,6,9 방향 돌면서 범위 체크하고 1일 때
            dfs(xx,yy) #회귀

n = int(input())
ls = [list(map(int,input())) for _ in range(n)] #값 받는 리스트
res = [] #카운트 리스트

for i in range(n): #이중 for문 = 2차원 배열 형식으로 되어서 x,y 둘 다 볼려면 2중 for문 i,j로 접근하는게 합당하기 때문
    for j in range(n):
        if ls[i][j]==1:
            cnt=0 #돌 때마다 초기화 (7->cnt//8->cnt//9->cnt.. 이런식)
            dfs(i,j) 
            res.append(cnt) #dfs 한 번 끝날 때 마다 그 때 돌아서 더해진 cnt값들을 res에 추가함
res.sort() #오름차순이니까 sort() 해주고 
print(len(res))
for i in res:
    print(i)