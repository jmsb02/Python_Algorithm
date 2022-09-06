######
#가로 세로 0~4 0~4 2차원 배열 형식 생각하고 가운데부터 마름모꼴로 재귀로 거쳐간다
#12, 3, 6, 9시 방향으로 계속 재귀 처리하고, 거쳐가면 체크하면 됨
#결국 따져보면 레벨 탐색이므로 bfs - 큐(덱) 이용
import sys
input =sys.stdin.readline
from collections import deque #bfs - 큐 이용
dx=[-1,0,1,0] #12,3,6,9
dy=[0,1,0,-1]
n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)] #이 형식 기억해두기 2차원 배열
ch=[[0]*n for _ in range(n)] #중복 제거 리스트
sum=0
q=deque()
ch[n//2][n//2]=1 #시작 지점이니까 중복되지 않게 미리 1로 처리
sum+=ls[n//2][n//2] #sum에 시작하는 값 넣어주고
q.append((n//2,n//2)) #이차원 형식으로 큐  추가
l=0 #인덱스
while True:
    if l==n//2:#쉽게 n=5일 때 생각하면 됨 마름모 2개일 때 끝내야 함 3개면 안 됨
        break
    size=len(q) #레벨탐색 1, 4 .. 
    for i in range(size):
        now = q.popleft() #레벨 0일 때 1개, 레벨 1일 때 4개 ..
        for j in range(4): #4개는 고정이지 어짜피 중복으로 처리하면 되니까 겹치는 부분
            x=now[0]+dx[j] 
            y=now[1]+dy[j]
            if ch[x][y]==0: #중복이 아닐 때
                sum+=ls[x][y] #sum에 누적하고
                ch[x][y]=1 #거쳐갔으니 중복 체크해주고
                q.append((x,y)) #append를 통해 다음 값으로 이동
    l+=1
print(sum)