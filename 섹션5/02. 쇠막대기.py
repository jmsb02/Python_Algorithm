#쇠막대기

s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i] =="(":
        stack.append(s[i])
    else: #s[i]==")"
        stack.pop() #지금 스택 상태엔 ( 계속 있을 거자너 자기와 맞는 ( pop해줌
        #밑에 if,else 공통 요소여서 위로 뺌
        if s[i-1]=="(": #돌 때 자기보다 앞에 있는 애가 "("인 경우에는 
            cnt+=len(stack)
        else:
            #pop하는 이유 - 쇠막대기를 여기서 끊어줘야 함
            cnt+=1
print(cnt)
