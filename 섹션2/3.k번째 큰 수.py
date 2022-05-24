#3. k번째 큰 수
n,k = map(int,input().split())
l = list(map(int,input().split()))
result=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for b in range(j+1,len(l)):
            result.append(l[i]+l[j]+l[b])
result = set(result)
final_result = list(result)
final_result.sort(reverse=True)
print(final_result[k-1])

