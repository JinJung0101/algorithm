def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        #가장 작은 요소의 인덱스를 찾기 위한 변수
        min_idx=i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx]= arr[min_idx], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print(arr)