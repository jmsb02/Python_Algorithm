#10 점수 계산
n = int(input())
l = list(map(int,input().split()))
cnt = 0 
sum =0 
for x in l:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0
print(sum)
    