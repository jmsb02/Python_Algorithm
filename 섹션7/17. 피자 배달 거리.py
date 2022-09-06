#피자 배달 거리 #15686
# 푸는 방법 :  최소가 되는 M값이 제시되니까 피자집 좌표 중에 M개를 선택하는 조합을 구하고(DFS) 이 조합들 중 가장 최소의 도시 피자배달거리를 구하면 됨
# 한 번 선형탐색 돌면서 집, 피자집 좌표들을 담아놓고 피자집 좌표들 중 M개를 고르는 조합을 DFS 탐색으로 구한 후, 개별 조합을 구할 때마다 도시의 피자배달거리를 구하면서 최솟값을 갱신

def dfs(l,s):
    global res
    if l==m:
        sum = 0 #도시의 피자배달 거리
        for j in range(len(hs)):
            x1=hs[j][0] #튜플 형식으로 접근 했을 때의 x값
            y1=hs[j][1] #집의 좌표
            dis = 2147000000  #각 집의 피자 배달 거리
            for x in cb: #피자집의 인덱스 번호
                x2 = pz[x][0] #피자집의 좌표
                y2 = pz[x][1]
                dis = min(dis,abs(x1-x2)+abs(y1-y2)) #집의 피자배달 거리 최솟값 갱신
            sum+=dis #for문이 끝날 때 마다 조합 경우의 수 1개 경우 마다 나오는 sum 값 갱신
        if sum<res: #2중 for문이 끝나는 경우(dfs 한 번 탐색)
            res=sum
    else:
        for i in range(s,len(pz)): #조합 구하는 경우의 수
            cb[l]=i
            dfs(l+1,i+1)



n,m = map(int,input().split())
ls = [list(map(int,input().split())) for _ in range(n)]
hs = [] #집 
pz = [] #피자 #작성 이유 : 인덱스를 통해 해결하기 위해서
cb = [0]*m #n*n개에서의 m개의 피자를 넣는 경우(조합의 경우의 수)를 담기 위한 리스트
res = 2147000000
#추가적으로 이 문제는 인덱스 1부터 시작하지만 평소대로 0부터 시작해도 됨, 거리를 구하는 것이 목표이기 때문에
for i in range(n):
    for j in range(n):
        if ls[i][j]==1:
            hs.append((i,j))
        elif ls[i][j]==2:
            pz.append((i,j))
dfs(0,0)
print(res)
