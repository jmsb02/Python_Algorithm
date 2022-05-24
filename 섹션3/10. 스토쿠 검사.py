#스토쿠 검사
def check(ls):
    #행과 열 중복 처리
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[ls[i][j]]=1 #행
            ch2[ls[j][i]]=1 #열 
            #기본적으로 행과 열을 다 따졌을 때 중복이 안되면 sum=9가 되겠지([0]은 그대로 0이고)
        if sum(ch1) != 9 or sum(ch2) != 9: #행이나 열에서 중복이 생겼을 경우
            return False #False로 처리

    #그룹 단위 중복 처리
    for i in range(3): #0 1 2
        for j in range(3): #0 1 2
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[ls[i*3+k][j*3+s]]=1
            if sum(ch3) != 9:
                return False
    return True

ls = [list(map(int,input().split())) for _ in range(9)]
if check(ls): #check함수에서 True를 반환하면 
    print("YES")
else: #False를 반환하면
    print("NO")