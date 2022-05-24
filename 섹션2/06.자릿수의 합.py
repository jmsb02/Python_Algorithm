#6 자리수
def digit_sum(x):
   sum = 0
   for i in str(x): #"125" -> "1","2","5"
      sum += int(i) #8(int형)
   return sum

n = int(input())
a = list(map(int,input().split()))
max = -2147000000
for x in a:
   tot = digit_sum(x)
   if max<tot:
      max = tot
      res = x #125,97..
print(res)
