from collections import deque #기본 리스트에서의 pop(0) - 앞으로 다 끌고옴 = 비효율적
n,m = map(int,input().split()) #인원 수, 보트 한 개 당 총 무게
ls = list(map(int,input().split())) #각각 인원 몸무게
ls.sort()
ls = deque(ls)
#구명 보트는 2명 이하로 탈 수 있다
cnt = 0 
while ls:
    if len(ls)==1: #요소가 1개밖에 없을 때는 논리적 모순(두 번 더하거나 두 번 pop 안 됨)
        cnt+=1 
        break
    if ls[0]+ls[-1]>m: #맨 앞과 맨 뒤 더해서 리미트값 초과
        ls.pop() #맨 뒤에 몸무게 나간 사람만 보트 탐
        cnt+=1
    else: #맨 앞과 맨 뒤 몸무게 더해서 리미트보다 작거나 같으면
        ls.popleft() #두 명 보냄 (맨 앞) #popleft는 옮길 필요 없이 포인터만 옮기기 때문 시간 절약
        ls.pop() #맨 뒤
        cnt+=1
print(cnt)