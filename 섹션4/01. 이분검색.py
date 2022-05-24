#이분탐색
n,m = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
lt = 0
rt = n-1
while lt<=rt: #lt>rt인 경우는 탐색을 마쳤기 때문에 굳이 생각 X
    mid = (lt+rt)//2 #while문 안에 작성해야 유동적으로 움직임
    if ls[mid] ==m:
        print(mid+1) #배열이니까 1더해줘야지
        break #탐색 완료
    elif ls[mid]>m:
        rt = mid-1
    else: #ls[mid]<m #구하고자 하는 값 오른쪽
        lt=mid+1
