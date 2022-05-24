def Count(len): #중앙값으로 나눌 때 그 자를 수 있는 횟수, 401
    cnt = 0
    for x in ls: #for문을 통해 ls의 원소들을 하나씩 뽑아내면서
        cnt += (x//len) #ex. sum = 802//401 + 743//401 + 457//401 + 539//401
    return cnt

k,n = map(int,input().split())
ls = []
for i in range(k): #k가 int형이니까 이런식으로 for문과 tmp를 통해 ls에 추가
    tmp = int(input())
    ls.append(tmp)
ls.sort() #이분 검색이니까 정렬해주고
largest = max(ls) #오른쪽 범위를 정해줘야 하니까 변수 설정 해줌


res=0 #우리가 구해야 하는 랜선 최대 길이
lt = 1 #길이니까 1부터 시작
rt = largest #범위 마지막
while lt<=rt: #이분검색 시작
    mid = (lt+rt)//2 
    if Count(mid) >= n: #count함수 = 자를 수 횟수 구하는 거 
        res = mid #그 값을 먼저 res에 저장해주고 (계속 이상적 값을 찾아갈 때까지 반복)
        lt = mid+1 #그럴 때마다 오른쪽으로 이동해줘야지 
    else:
        rt = mid-1
print(res)