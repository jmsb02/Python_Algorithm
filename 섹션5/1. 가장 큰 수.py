#가장 큰 수
num,m = map(int,input().split())
num = list(map(int,str(num))) #str로 하나씩 쪼개고 int로 바꾼다음 얘네를 list로 묶음
stack=[] #구현해야 할 바탕 stack 작성(list로 구현)
for x in num:
    while stack and m>0 and stack[-1]<x: 
        #스택에 값 존재, 지울 수 있어야 하니까 m>0 지정, (LIFO) - 마지막 값보다 들어가는 값이 커야 삭제함
        stack.pop()
        m-=1
    stack.append(x)
if m!=0: #stack 셔터 내렸는데 m 값은 존재함 (입력 예제 2)
    stack = stack[:-m] #남은 m을 뒤집어서 그 전까지(완전한 곳까지)
res = ''.join(map(str,stack))
print(res)