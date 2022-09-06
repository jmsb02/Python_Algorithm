# 양팔 저울 - 다시 볼 필요 ㅇ

# 0으로 시작해서 선택지 3개 (그릇을 오른쪽에 놓는 경우, 왼쪽에 놓는 경우, 놓지 않는 경우)

def dfs(l, sum):

    global res

    if l == n:

        if 0 < sum <= s:

            res.add(sum)

 

    else:

        dfs(l + 1, sum + ls[l])

        dfs(l + 1, sum - ls[l])

        dfs(l + 1, sum)

 

 

n = int(input())

ls = list(map(int, input().split()))

s = sum(ls)

res = set()

dfs(0, 0)

print(s - len(res))

#되는 경우를 구해서 빼줌