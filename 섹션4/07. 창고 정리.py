l = int(input())
ls = list(map(int,input().split()))
m = int(input())
ls.sort()

for _ in range(m):
    ls[0]+=1
    ls[-1]-=1
    ls.sort()
print(ls[-1]-ls[0])
