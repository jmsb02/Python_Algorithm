# 숫자를 오름차순으로 정렬
# 이미 자리 잡은 숫자는 나보다 작은 숫자
# [0]*n 배열 만들어주고 0갯수만큼 뒤로 가기 
#0 만큼 가다가 그 곳 채워져있으면 그 다음 칸 가기

n=int(input())
a=list(map(int,input().split()))
seq=[0]*n

for i in range(n): #0~n-1 
    for j in range(n): #0~n-1
        if a[i]==0 and seq[j]==0: #자기보다 큰 숫자의 빈공간을 만들고, 그 때 한 곳 비워져 있으면,
            seq[j]=i+1
            break
        elif seq[j]==0: #빈자리(아직 자기자리 못 찾은거)
            a[i]-=1
for x in seq:
    print(x,end=' ')
