def DFS(l,sum):
    global cnt
    if sum>t:
        return
    if l==k:
        if sum==t:
            cnt+=1
    else:
        for i in range(pn[l]+1): #동전의 개수만큼 퍼짐
            DFS(l+1,sum+(pp[l]*i)) #이 때 인덱스, 합 계산
            #i 곱해야 0개,1개,2개 등 경우의 수 계산 가능


t = int(input())
k = int(input())
pp=[]
pn=[]
for _ in range(k):
    p,n = map(int,input().split())
    pp.append(p)
    pn.append(n)
cnt=0
DFS(0,0) #index, sum
print(cnt)