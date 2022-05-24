#9 주사위 게임
n = int(input())
res = 0
for i in range(n):
    a,b,c = map(int,input().split())
    L = [a,b,c]
    if a==b==c:
        money = 10000+1000*a
    elif a==b or b==c:
        money = 1000+b*100
    elif a==c:
        money = 1000+100*c
    else:
        money = max(L)*100
    if money > res:
        res = money
print(res)
    
