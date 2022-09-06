#재귀함수와 스택 연계성
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end=' ')

n = int(input())
DFS(n)