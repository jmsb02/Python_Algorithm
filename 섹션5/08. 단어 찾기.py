n = int(input())
p = dict()
#인덱스 값을 숫자가 아닌 다른 값 '문자열, 튜플'을 사용하려고 할 때
#빠른 접근  / 탐색이 필요할 때(다 O(1)) #집계가 필요할 때(원소의 개수)

#접근방식
#기존 노트에 있는 애들 값을 1주고, 시에 쓰인 단어가 있으면 0으로 다시 초기화
#=>바뀌지 않은 애가 1이겠네 <- 원소로 접근 (dict)

for i in range(n):
    word = input()
    p[word]=1 #{"big":1, "good" = 1 ...}
for i in range(n-1):
    word = input()
    p[word]=0 #단어에 있는데 시에 없는 애만 1임
for key,val in p.items():
    if val==1:
        print(key) #그 때의 key 값
        break
