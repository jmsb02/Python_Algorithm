n = int(input())
a = [list(map(int,input().split())) for _ in range(n)] #기억하기 통째로
largest = -2147000000
for i in range(n):
    sum1=sum2=0 #돌 때마다 초기화
    for j in range(n):
        sum1 += a[i][j] #행 
        sum2 += a[j][i] #열
    if largest<sum1:
        largest=sum1
    if largest<sum2:
        largest=sum2
#이 위까지 행과 열 중 최댓값 도출
sum1=sum2=0
for i in range(n):
    sum1 += a[i][i] #좌->우 대각선
    sum2 += a[i][n-i-1] #우->좌 대각선
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)
#행과 열, 좌/우 대각선 나눠서 구함
#행과 열의 최대 largest를 먼저 구하고, 좌/우 대각선이 클 때 if문 적용
#sum1, sum2 위치 잘 보기 (행/열 구할 때는 초기화), 대각선 - 밖에서(for문안에서 이전 사용되었기 때문)