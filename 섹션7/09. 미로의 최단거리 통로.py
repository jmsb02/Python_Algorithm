import sys
from collections import deque
dx=[-1, 0, 1, 0]#동서남북
dy=[0, 1, 0, -1]
board=[list(map(int, input().split())) for _ in range(7)]#값, 중복 제거 리스트
dis=[[0]*7 for _ in range(7)]#이동 및 결과 출력 리스트
Q=deque() #최단경로 - bfs
Q.append((0, 0)) #첫 번째 값 삽입
board[0][0]=1 #첫 번째는 무조건 들리기 때문에 다시 못오게 하기 위해 1로 설정
while Q: #한 값 넣고 빼고 계속 반복(다 탐색 할 때까지)
    tmp=Q.popleft() #첫 번째 값부터 접근하기 위해 popleft 이용
    for i in range(4): #x,y 값 설정해주기 위해 4번씩 돌아야지
        x=tmp[0]+dx[i] #이 방법은 익혀두기
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            #조건 처리 중요 !! 범위 넘지 않고 중복되지 않았을 때
            board[x][y]=1 #왔다고 체크해주고
            dis[x][y]=dis[tmp[0]][tmp[1]]+1 #카운트해줌 (이전값+1)
            Q.append((x, y))
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])