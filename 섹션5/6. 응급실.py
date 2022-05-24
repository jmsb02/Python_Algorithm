from collections import deque
n,m = map(int,input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int,input().split())))]
#enumarate = 인덱스와 원소를 동시에 접근 , 튜플 형식으로 받음
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft() #(0,60) 튜플 형식으로 값을 받았으니까
    if any(cur[1]<x[1] for x in Q): #[1] = 원소 값
        #any는 한 가지라도 만족하면 True #자기보다 큰 값이 존재한다는 거니까
        Q.append(cur) #popleft한 값을 append 해줘야 함
    else:
        #자기보다 큰 애가 하나도 없음
        cnt+=1
        if cur[0] ==m: #우리가 원하는 값이라면
            print(cnt)
            break