#최대점수 구하기 푸는 법
#for문으로 다 값을 받고, score,time 리스트에 따로 저장(인덱스 사용하려고)
#인덱스 1부터 시작해서 푼다 안 푼다해서 l==m일 때 값 처리
#즉 if문으로 정답 처리, else로 푼다 안 푼다 처리
#res를 정해줘서 최대값 갱신

def DFS(l,score,time):
    global result
    if time>m:
        return #가지치기
    if l==n:
        if score>result:
            result=score
    else:
        DFS(l+1,score+ps[l],time+pt[l]) #sum,time 들어오기 전 0으로 초기화해서 사용 가능
        DFS(l+1,score,time)



n,m=map(int,input().split())
ps = []
pt = []
result = -2147000000
for _ in range(n):
    s,t = map(int,input().split())
    ps.append(s)
    pt.append(t)
DFS(0,0,0) #인덱스 값 시간
print(result)