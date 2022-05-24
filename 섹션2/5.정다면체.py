#5 정다면체
n,m = map(int,input().split())
cnt = [0]*(m+n+3) #개수세는 리스트 생성
max=0 #cnt 개수 최대 저장 변수
for i in range(1,n+1):
   for j in range(1,m+1): #횟수 넣은 cnt 리스트 구성
      cnt[i+j]+=1
#여기 cnt 함수 구성됨
for i in range(n+m+1): #가장 많이 cnt된 애들 찾아야 함
   if cnt[i] > max:
      max = cnt[i]
#밑 사례 때문에 for문 끝내고 해결함
for i in range(n+m+1):
   if cnt[i] ==max:
      print(i,end=' ')

   # elif cnt[i]==max: #이렇게 구성시 [0,0] 앞 부분 문제 발생
   #    print(i, end=' ')