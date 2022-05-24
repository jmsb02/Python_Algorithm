#7 에라토스테네스 체 = 소수 개수 구하기
n = int(input())
ch = [0]*(n+1) #인덱스 번호 때매 n+1개
cnt = 0 #소수의 개수 초기화
for i in range(2,n+1):
   if ch[i] == 0: #소수면
      cnt+=1 #cnt+=1
      for j in range(i,n+1,i): #소수일 때 걔 배수 처리해 줘야 함
         ch[j] = 1 #소수일 때 배수 1로 맞춰져야 함 #카운트 안 더해줌
print(cnt)
