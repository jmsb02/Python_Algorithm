#뮤직 비디오
def Count(capacity): #n곡을 저장하려면 dvd가 최소 몇개?
    cnt = 1 #최소 한 개의 dvd 필요
    sum = 0
    for x in ls:
        if sum+x>capacity: #기존 값에 다음 값을 더했을 때 용량 초과면
            cnt+=1 #dvd가 1개 더 필요하고
            sum=x #x(다음 값)부터 시작해야함
        else: #용량이 있을 때에는 
            sum+=x #더해줌
    return cnt

n,m = map(int,input().split())
ls = list(map(int,input().split()))
#ls.sort() #이분탐색 - 정렬된 상태에서 사용
#-> 순서대로 곡의 길이가 주어졌다했기 때문에 지금 이 자체가 정렬된 상태
#굳이 오름차순 다시 할 필요가 없네
lt = 1 #한 dvd가 가질 수 있는 최소 용량 (예시같은 경우 9개가 1씩 값을 가짐)
rt = sum(ls) #한 dvd가 가질 수 있는 최대 용량 (예시같은 경우 한 dvd가 45 먹음)
res=0

maxx= max(ls) #dvd는 최소한 ls의 가장 큰 값을 담을 수 있는 공간을 가지고 있어야 함
while lt<=rt:
    mid = (lt+rt)//2
    if mid>=maxx and Count(mid)<=m: 
         # #2장만에 저장할 수 있음 -> 3, 4, 5장도 됨
         res = mid
         rt = mid-1 
        #용량의 최소를 찾아야 되고 mid로도 답을 구할 수 있으니까
        #mid보다 큰 값은 되겠지 오른쪽 버림
    else:
        #용량이 너무 작아가지고 큰 것이 필요 작은 쪽을 버림
        lt = mid+1
print(res)