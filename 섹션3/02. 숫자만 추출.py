#2 숫자만 추출
n = input()
res = 0
for x in n:
    if x.isdigit(): #숫자인지 확인 하는 애 = isdigit
        res = res*10 + int(x) #앞에 0 못오게 하는거 
print(res)
cnt=0
for i in range(1,res+1):
    if res%i==0: #약수 구하는거 
        cnt+=1
print(cnt)
