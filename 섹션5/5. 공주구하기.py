from collections import deque
n,k=map(int,input().split())
queue = deque()
for x in range(1,n+1):
    queue.append(x)
while queue:
    if len(queue)==1:
        break
    else:
        for x in range(k-1):
            queue.append(queue.popleft())
        queue.popleft()
print(queue[0])
