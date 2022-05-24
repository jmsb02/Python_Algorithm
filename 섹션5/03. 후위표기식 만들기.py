a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal(): #숫자형식을 띄고 있으면 True
        res+=x #그냥 추가
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1] =='*' or stack[-1] =='/'): #stack에 값이 존재하고, 맨 위가 *나 /면  
                stack.pop() #걔네를 먼저 pop해주고
            stack.append(x) #그렇지 않을 때에는 append
        elif x=='+' or x=='-': 
            while stack and stack[-1] != '(': #여는 괄호 전까지만 #괄호 안에 더하기 빼기
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1] != '(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
