#격자판 회문수
ls = [list(map(int,input().split())) for _ in range(7)]
cnt=0
for i in range(3): #행이든 열이든 0,1,2에서만 비교 가능하기 때문에 list기준 3으로 설정
    for j in range(7): #행과 열 7줄이니까 7번
        tmp = ls[j][i:i+5] #열 비교 [0][0:5], [0][1:6], [0][2:7] ...
        if tmp == tmp[::-1]: #[::-1]를 통해 역 비교 tmp 변수랑 함께
            cnt+=1 #역으로 뒤집었을 때 같으면 cnt 값에 하나 더해줌
        for k in range(2): #행 비교 - 슬라이싱 안 됨 행 기준 리스트 아니기 때문
            if ls[i+k][j] != ls[i+5-k-1][j]: #열 고정(0~7), 행 비교 
                break
        else:
            cnt+=1
print(cnt)
