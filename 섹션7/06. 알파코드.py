#접근방법, 결과 리스트를 만들고 dfs(0,0)으로 접근 #기존 인덱스, 결과값 인덱스
#else문에서 1~26씩 돌면서 가장 먼저 인덱스 0 or 0 + 1 이렇게 두 가지 경우로 계산 
#ex) res[0]==2 or res[0]==2 and res[1]==5 #즉 한 자리, 두 자리로 나눠보겠다는 말임
#l==n이 되었을 때가 인덱스 마지막이므로 이 때가 답이고 for문 + char를 통해 풀림
#그리고 결과값을 나타내는 리스트 마지막에 -1 추가 (마지막에 두 글자를 볼 수도 있으니)

def dfs(l,p):
    global cnt
    if l==n:
        cnt+=1
        for j in range(p): #마지막은 p지점에 들어감 즉, p만큼 돌면 res 출력 가능
            print(chr(res[j]+64),end='') #아스키코드->문자 chr 이용 대문자 A 65여서 처음 64 더해줌
        print()
    else:
        for i in range(1,27): #내려갈 때 1~26까지 가지 뻗는다
            if code[l]==i: #2 즉 25 전 2를 먼저 보는거 (한 자리 수)
                res[p]=i
                dfs(l+1,p+1)
            elif i>=10 and code[l]==i//10 and code[l+1]==i%10:
                #두 자리 수 확인 10보다 크면서 두 개 인덱스 각각 10으로 나눈 몫, 나눗셈이 들가야 함 23->2/3
                res[p]=i
                dfs(l+2,p+1) #p+1인 경우 한 인덱스에 25가 들어가야 위에서 바꿀 수 있음 #인덱스 차이 파악!


code = list(map(int,input()))
n = len(code) #dfs 함수에서 if 문을 통해 결과값을 도출하기 위해서는 마지막 인덱스 값인 n이 필요하기 때문
code.insert(n,-1) #위에서 언급했듯이 list 범위 나가는 에러 막기 위해서 사전 설정
res = [0]* (n+3) #결과값 인덱스
cnt = 0 
dfs(0,0) #code, res 인덱스
print(cnt)