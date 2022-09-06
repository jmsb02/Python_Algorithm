#퀵정렬 = 분할 정복 알고리즘의 하나. +  전위 순회 방식
#하나의 리스트를 피벗(pivot)을 기준으로 두 개의 비균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법이다.

def Qsort(lt,rt):
    if lt<rt:
        pos = lt #pos가 화살표 변수
        pivot = arr[rt] #얘를 기준으로 좌우 분할되고 정렬 됨
        for i in range(lt,rt):
            if arr[i]<=pivot:
                arr[i], arr[pos] = arr[pos], arr[i] #ex) 21<=33 -> 45,21 = 21,45 이런식으로 pivot보다 작은 값을 앞으로 가게 바꿈
                pos+=1
        arr[rt],arr[pos]=arr[pos],arr[rt]
        #여기까지 가운데에 있는 pivot을 중심으로 왼쪽은 작은 값, 오른쪽은 큰 값으로 배치 됨 여기서 분할(순회) 들어감
        Qsort(lt,pos-1) #pos는 지금 pivot의 위치, pivot 기준으로 왼쪽 순회
        Qsort(pos+1,rt) #오른쪽 순회




arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
print("Before sort : ", end='')
print(arr)
Qsort(0,9) #인덱스 0~9 총 10개가 들어있는 리스트
print("After sort : ", end= '')
print(arr)