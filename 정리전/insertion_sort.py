def insertion_sort(arr):
    for i in range(1, len(arr)):
        #현재 위치의 요소값을 key에 저장
        key=arr[i] 
        j = i-1
        #key보다 큰 값을 가진 요소들을 오른쪽으로 이동
        while j >=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        #key를 적절한 위치에 삽입
        arr[j+1]=key
    return arr

arr=[12,11,13,5,6]
insertion_sort(arr)
print(arr)