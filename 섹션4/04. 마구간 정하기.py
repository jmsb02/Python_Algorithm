def Count(len):
    cnt = 1 #적어도 한 말은 있어야 함
    ep = ls[0] #바로 첫 번째 마굿간에는 넣어야 함 (낭비 x)
    for i in range(1, n): #n = 전역변수니까 사용 가능
        if ls[i]-ep >= len: #말 배치 가능
            cnt +=1 #가장 가까운 말의 최대 거리(가정)보다 크기 때문에
            ep = ls[i] #초기화
    return cnt



n,c = map(int,input().split())
ls = []
for i in range(n):
    tmp = int(input())
    ls.append(tmp)
ls.sort()

lt = 1
rt = ls[n-1] #두 말의 거리가 9를 넘어서는 안 됨
res = 0 
while lt<=rt:
    mid = (lt+rt)//2 #mid = 가장 가까운 말의 최대 거리라고 가정
    if Count(mid)>=c: #두 말의 거리를 넣었을 때의 말 넣을 수 있는 개수
        #이쪽이 정답 (4마리 넣을 수 있다면 3마리도 넣을 수 있기 때문)
        res = mid
        lt = mid+1
    else:
        rt = mid -1 #범위를 너무 크게 잡아서 좁혀야 함
print(res)
