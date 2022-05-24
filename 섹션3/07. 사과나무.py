#사과나무
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
sum = 0
#####포인터 2개
s=e=n//2
for i in range(n):
    for j in range(s,e+1):
        sum += a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(sum)
#넘어가는 시점의 i 확인
