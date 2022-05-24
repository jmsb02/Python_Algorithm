#4 대표값
n=int(input())
l = list(map(int,input().split()))
avr = round(sum(l)/n)
min = 2147000000
for idx, x in enumerate(l): #번째 = idx, 점수 비교 = x
         #평균과의 거리를 통해 접근 - 절대값
         tmp = abs(x-avr) #변수를 통해 평균과 가까운 애 찾기
         if tmp < min:
            min = tmp #평균과 가장 가까운 거리 
            score = x #그 때의 점수
            res = idx + 1 #그 때의 인덱스(배열이니까 +1)
         elif tmp == min: #평균과 떨어진 거리가 같은 애가 나온 경우 (ex.평균 74 -> 73, 75)
            if x > score: #기존 점수가 더 클 때여야 함 (큰 수부터)
                score =x #점수
                res = idx +1 #인덱스
print(avr, res)
                
