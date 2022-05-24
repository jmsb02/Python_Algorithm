#최대힙 - 기본적으로 최소힙 사용
import heapq as hq
heap = []
while True:
    n = int(input())
    if n==-1:
        break
    if n==0:
        if len(heap)==0:
            print(-1)
        else: #최대힙에서 최댓값을 구할 때 
            print(-hq.heappop(heap)) #출력할 때 다시 양수로 나오게 하면 됨
             #hq.heappop 사용
    else: #최대힙 값 추가 - hq.heappush(리스트, 원소)
        hq.heappush(heap,-n) #부호가 반대로 들어가고
