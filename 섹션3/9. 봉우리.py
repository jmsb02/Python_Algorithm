n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]
ls.insert(0,[0]*n) #맨 윗 줄 0 0 0 0 0 (n=5일 때)
ls.append([0]*n) #맨 밑 줄 0 0 0 0 0 (n=5일 때)
for x in ls: #한 줄 씩 뽑으면서 각각 맨 앞과 맨 마지막에 0 추가
    x.append(0) #뒤
    x.insert(0,0) #앞

cnt = 0
dx = [-1,0,1,0] #행
dy = [0,1,0,-1] #열
    #상우하좌
for i in range(1,n+1): #0으로 하면 안되는 이유 : 0으로 주변 감쌌기 때문
    for j in range(1,n+1):
        if all(ls[i][j]>ls[i+dx[k]][j+dy[k]] for k in range(4)):
            #all = 모든 조건 만족, 상하좌우 4번 저 위에 있는 것이 조건식 확인
            cnt+=1
print(cnt)