#포인터 값 접근 형식으로 풀이
n = int(input())
l_1 = list(map(int,input().split()))
m = int(input())
l_2 = list(map(int,input().split()))
p1=p2=0
result = []
while p1<n and p2<m: #l_1,l_2 둘다 리스트 안 요소들 접근할 때에만 
    if l_1[p1] <= l_2[p2]: #동일한 위치 값 비교할 때 p1 가르키는 값이 작음
        result.append(l_1[p1]) #p1 추가
        p1+=1
    else: #그렇지 않으면 
        result.append(l_2[p2]) #p2 추가
        p2+=1
#while문 빠져나옴 = 어떤 리스트에서 요소 세는 거 끝남 (두 리스트 크기가 다름)
if p1<n: #l_2가 더 작은 리스트일 경우
    result = result+l_1[p1:]
if p2<m: #l_1가 더 작은 리스트일 경우
    result = result + l_2[p2:]
print(*result)
