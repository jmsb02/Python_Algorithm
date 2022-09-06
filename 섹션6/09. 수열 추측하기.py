#푸는 방법 3가지 리스트 1. 파스칼의 삼각형 2. 중복 처리 3. 결과값
import sys
def DFS(L,sum):
    if L==n and sum==f: #끝에 도달했을 때, 구하고자 하는 값일 때
        for x in p:
            print(x,end=' ')
        sys.exit(0) #사전 상 앞에 있는 것만 출력 후 끝냄
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1 #중복 체크
                p[L]=i #결괏값 리스트에 값을 넣어줌
                DFS(L+1,sum+(p[L]*b[L]))
                ch[i]=0

n,f = map(int,input().split())
p=[0]*n #출력 리스트
b=[1]*n #파스칼 삼각형 리스트, 1로 초기화 한 이유 = 처음과 끝은 1 고정
ch=[0]*(n+1) #중복처리 리스트 
for i in range(1,n):
    b[i]=(b[i-1]*(n-i))//i
    #스칼라 삼각형 리스트는 먼저 작성하고 들어감
DFS(0,0)