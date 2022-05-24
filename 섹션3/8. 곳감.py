#곳감 (모래시계)
n=int(input())
ls = [list(map(int,input())) for _ in range(n)]
m = int(input())
for i in range(m):
    h,t,k = map(int,input().split()) #각각 행, 방향, 개수
    if t==0: #오른쪽으로 갈 때는 앞에 것을 지우고(pop(0)) 뒤에 추가(append)
        #pop()하면 자동적으로 땡겨짐
        for _ in range(k):
            ls[h-1].append(ls[h-1].pop(0))
    else: #왼쪽으로 갈 때는 뒤에 것을 지우고(pop()), 0번째 자리에 insert
        for _ in range(k):
            ls[h-1].insert(0,ls[h-1].pop())
s = 0
e = n-1
sum=0
for i in range(n): #모래시계 형식 - 포인터 각각 0,n-1 좁,넓 유동적으로 처리
    for j in range(s,e+1):
        sum+=ls[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(sum)