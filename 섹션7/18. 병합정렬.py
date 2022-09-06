#병합정렬 = 분할 정복 알고리즘의 하나. + 후위 순회 방식
#분할 정복 : 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략이다. (대개 순환 호출을 이용하여 구현)
#병합정렬의 개념 : 하나의 리스트를 두 개의 균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법이다.
def Dsort(lt,rt): #병합정렬 Dsort
    if lt<rt:
        mid = (lt+rt)//2
        Dsort(lt,mid) #왼쪽
        Dsort(mid+1,rt) #오른쪽
        p1 = lt
        p2 = mid+1
        tmp = [] #리스트 복사(arr에서 바로 구현 x)
        while p1<=mid and p2<=rt:
            if arr[p1]<arr[p2]: #각 부분에서의 왼쪽끼리 비교
                tmp.append(arr[p1]) #더 작은 값을 넣어줘야 함 (오름차순 정렬)
                p1+=1
            else:
                tmp.append(arr[p2]) #p2가 더 작을 때
                p2+=1
        if p1<=mid: #p2가 먼저 끝났을 때(p1은 아직 다 복사하지 못했음)
            tmp = tmp+arr[p1:mid+1] #나머지 부분 삽입 #슬라이싱 성질 : mid+1
        if p2<=rt: #p1이 먼저 끝났을 때
            tmp = tmp+arr[p2:rt+1]
        for i in range(len(tmp)): #다 끝낸 뒤 tmp 배열 arr 위치에 복사
            arr[lt+i]=tmp[i] #lt기준으로 쭉 정렬해야 하니까 lt
        


arr=[23,11,45,36,15,67,33,21]
print("Before sort : ", end='')
print(arr)
Dsort(0,7)
print()
print("After sort: ", end='')
print(arr)