n=int(input())
ls = []
for i in range(n):
    k,m = map(int,input().split())
    ls.append((k,m))
ls.sort(reverse=True) #키가 큰 순서대로 정렬
cnt=0 #출력해야 하는 결과값
largest=0 #2중for문 비효율적, 정렬된 위치에서 자기보다 위쪽 애들보다 몸무게에서 최대가 되면 됨(몸무게 초기화)
for x,y in ls: #키, 몸무게
    if y>largest: #첫 번째 줄 애는 무조건 cnt되지(키가 제일 크잖아)
        #자기보다 키 큰 애들보다 몸무게가 더 많이 나가야(얘 몸무게-최대여야) 뽑힘
        largest =y  #그리고 그 때의 몸무게를 최댓값 다시 초기화
        cnt+=1 #카운트 값 +1
print(cnt)
