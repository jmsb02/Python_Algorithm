a=input()
stack=[]

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=="+":
            a=stack.pop()
            b=stack.pop()
            stack.append(b+a)
        elif x=="-":
            a=stack.pop()
            b=stack.pop()
            stack.append(b-a)
        elif x=="*":
            a=stack.pop()
            b=stack.pop()
            stack.append(b*a)
        elif x=="/":
            a=stack.pop()
            b=stack.pop()
            stack.append(b/a)
print(stack[0])

#스택 - LIFO => 밑 쪽이 계산 결과 축적