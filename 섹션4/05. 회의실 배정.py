#회의실 배정 - 그리디 알고리즘 -정렬 !
n = int(input())
meeting = []
for i in range(n):
    s,e = map(int,input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x: (x[1],x[0])) #끝나는 시간을 기준으로 정렬해야 함 - lambda
et = 0 #끝나는 시간 초기화 
cnt = 0 #result값
for s,e in meeting:
    if s>=et: #시작 시간이 끝나는 시점보다 크거나 같아야 시간표를 짤 수 있음
        et=e #그 때 끝나는 시간을 meeting에서의 e 값으로 다시 초기화
        cnt+=1 #그 때 시간표를 짤 수 있으니까 우리가 구하고자 하는 개수 1개 더해줌
print(cnt)
