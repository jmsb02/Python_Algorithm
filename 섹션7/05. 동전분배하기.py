def dfs(l):
    global res
    if l==n: #맨 마지막 지점 도달
        sum = max(money)-min(money)
        if sum<res: #최솟값 갱신
             tmp = set() #세 개가 다 다른 값 조건 -> 집합 & len을 통해 처리
             for x in money:
                tmp.add(x)
                if len(tmp)==3: #3가지 값이 다르다는 조건
                    res=sum
    
    else:
        for i in range(3):
            money[i]+=ls[l] #더해주고
            dfs(l+1) #내려가고 
            money[i]-=ls[l] #백트래킹할 때 다시 빼주고



n = int(input())
ls =[]
for _ in range(n):
    ls.append(int(input()))
money = [0]*3 #a,b,c
res = 2147000000 #차의 최소 갱신
dfs(0) 
print(res) #마지막에 출력