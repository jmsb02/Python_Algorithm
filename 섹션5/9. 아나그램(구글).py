#논리 - 위 값으로 CNT해주고 밑 값으로 다시 빼줌
#다 했을 경우 아니그램이면 dict에 value 값이 0이여야겠지
a = input()
b = input()
str1 = dict()

for x in a:
    str1[x] = str1.get(x,0)+1 #key,val(찾고자 하는 키,없을 때 넣을 값) 

for x in b:
    str1[x] = str1.get(x,0)-1 #있을 때 마다 빼줌

#그럼 아니그램일 경우에는 0이 되겠지 (완전히 수행되었을 때)

for x in a:
    if str1[x]>0: #완전히 수행되지 못한거지 (key통해 value접근)
        print("NO")
        break
else:
    print("YES")

# #리스트 해쉬 - 아스키코드
# a = input()
# b = input()
# str1=[0]*52
# str2=[0]*52

# for x in a:
#     if x.isupper():
#         str1[ord(x)-65]+=1 #대문자 A 아스키코드 65
#     else:
#         str1[ord(x)-71]+=1 #소문자 A 아스키코드 71
# for x in b:
#     if x.isupper():
#         str2[ord(x)-65]+=1
#     else:
#         str2[ord(x)-71]+=1
# for i in range(52):
#     if str1[i] != str2[i]:
#         print("NO")
#         break
# else:
#     print("YES")
