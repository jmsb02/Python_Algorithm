# BFS - 넓이 우선 탐색 (레벨 탐색) -> 가까운 것부터 처리 - 큐
# 가지 3개 뻗음 -1, +1 +5
import sys
from collections import deque
MAX=10000
ch=[0]*(MAX+1) #중복 제거 리스트 - 왔던 곳 또 가면 비효율적임
dis = [0]*(MAX+1) #결과 cnt 리스트
n,m = map(int,input().split())
ch[n]=1 #기존 위치는 다시 오지 않게 하기 위해 1로 설정
dis[n]=0 #cnt는 아직 0으로 처리
dq = deque()
dq.append(n)
while dq:
    now = dq.popleft() #for문을 돌면서 apppend 계속 되기 때문에 갱신 됨
    if now ==m:
        break
    for next in (now-1,now+1,now+5): #3가지 가지를 뻗을 때
        if 0<next<=MAX: #next는 양수값이고
            if ch[next]==0: #중복이 아닐 때
                dq.append(next)
                ch[next]=1
                dis[next]=dis[now]+1 #이전 개수 +1
print(dis[m]) #탐색이 끝나면 우리가 구하고자 하는 인덱스를 봐서 cnt가 몇인지 본다
