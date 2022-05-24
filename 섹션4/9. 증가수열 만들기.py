
n=int(input())
ls = list(map(int,input().split()))
lt = 0 #왼 쪽을 가르키는 포인터 느낌
rt = n-1 #오른쪽을 가르키는 포인터 느낌
last = 0 #수열의 마지막 값을 지정해야 함 (처음 lt,rt - 첫 항으로서의 자격)
res = ""
result=[] #증가 수열을 따로 빼서 출력해야 하니 배열 생성

while lt<=rt:
    if ls[lt]>last:
        result.append((ls[lt],"L")) #(2,L)
    if ls[rt]>last:
        result.append((ls[rt],"R")) #(3,R)
    result.sort() #작은 수로 정렬해야 하니까 정렬
    if len(result)==0: #왼, 오른쪽 둘 다 첫 항의 자격x
        break
    else:
        res = res + result[0][1] #"L"이나 "R"과 같은 문자 res에 집어 넣음
        last = result[0][0] #숫자 last에 넣어줌
        if result[0][1] =="L":
            lt+=1
        else:
            rt-=1
    result.clear()

print(len(res))
print(res)
