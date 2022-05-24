#6 수들의 합
n,m = map(int,input().split())
list = list(map(int,input().split()))
lt = 0 #인덱스 변수 1
rt = 1 #인덱스 변수 2
tot = list[0] #연속 부분 합 (0번째 요소로 먼저 초기화)
cnt = 0 #m이 되는 cnt 개수 (우리가 구해야 하는 값)
while True:
    if tot<m: #연속 부분 합<m(구해야 하는 값)
        if rt<n: #rt 인덱스가 밖으로 벗어나지 않았을  경우
            tot+=list[rt] #rt 값을 더해 줌 
            rt+=1 #rt 오른쪽으로 한칸
        else:
            break #rt>=n (인덱스 밖으로 벗어남)
    elif tot==m: #연속 부분합 == 우리가 구하고자 하는 값 
        cnt+=1 #cnt 하나 더 해줌 
        tot -= list[lt] #lt 값 빼주고
        lt+=1 #lt를 오른쪽으로 이동
    else: #tot>m 구하고자 하는 값보다 우리가 계산한 값이 더 큼
        tot-=list[lt] #lt를 빼고
        lt+=1 #lt 이동
print(cnt)
