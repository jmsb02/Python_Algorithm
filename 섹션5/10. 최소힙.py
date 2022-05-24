#최소힙 - 리스트 형식, import heapq as hq 로 접근(기본 -최소힙 지원)
import heapq as hq
heap = []
while True:
    n = int(input())
    if n==-1:
        break
    if n==0:
        if len(heap)==0:
            print(-1)
        else: #최솟값
            print(hq.heappop(heap))
            #최소힙 - 이진트리에서 최솟값 구하는 법 => hq.heappop 사용
    else:
        hq.heappush(heap,n) 
        #최소합 값 추가 - hq.heappush(리스트, 원소)