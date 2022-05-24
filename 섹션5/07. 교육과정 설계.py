from collections import deque
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft(): #plan에서 하나씩 뽑는데 걔가 dq에 있는데 dq 맨 앞에 있지 않음
                print("#%d NO"%(i+1)) #NO출력
                break
    else: #순서대로 매칭 ㅇ
        if len(dq) == 0:            
            print("#%d YES"%(i+1))
        else: #필수교육이 존재하는데 need에 안넣은 거지 -> NO
            print("#%d NO"%(i+1))
