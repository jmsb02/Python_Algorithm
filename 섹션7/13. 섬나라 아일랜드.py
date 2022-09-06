#섬나라 아일랜드 (BFS 활용)

 

from collections import deque

 

 

def bfs(x, y):

    global cnt

    q = deque()

    q.append((x, y))  #튜플형식으로 삽입

    while q:

        tmp = q.popleft()

        xx = tmp[0]  #x값 변수

        yy = tmp[1]  #y값 변수

        for i in range(8):  #8방향 돌면서 (12,3,6,9 + 대각선)

            res_x = xx + dx[i]

            res_y = yy + dy[i]

            if 0 <= res_x < n and 0 <= res_y < n and ls[res_x][

                    res_y] == 1:  #범위를 넘지 않고 다음값이 1일 경우

                ls[res_x][res_y] = 0  #넘어가기 전 값을 0으로 초기화 해주고

                q.append((res_x, res_y))  #deque에 삽입한다

    cnt += 1  #while문이 끝날 때마다 정상적으로 처리되었다는 소리이기 때문에 cnt+=1 더해줌

 

 

#

dx = [-1, -1, 0, 1, 1, 1, 0, -1]

dy = [0, 1, 1, 1, 0, -1, -1, -1]

 

n = int(input())

ls = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):

    for j in range(n):

        if ls[i][j] == 1:

            ls[i][j] = 0  #중복 처리하지 않기 위해 0으로 초기화 해주고

            bfs(i, j)  #bfs 호출

print(cnt)