def find_longest_subarray(arr, n, k):
    count = {}
    start = 0
    max_length = 0

    for end in range(n):
        # 현재 숫자의 빈도수 업데이트
        if arr[end] in count:
            count[arr[end]] += 1
        else:
            count[arr[end]] = 1

        # 조건을 위반할 때까지 start 포인터 이동
        while count[arr[end]] > k:
            count[arr[start]] -= 1
            start += 1

        # 최대 길이 갱신
        max_length = max(max_length, end - start + 1)

    return max_length

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()
n, k = int(data[0]), int(data[1])
arr = list(map(int, data[2:]))

# 결과 출력
print(find_longest_subarray(arr, n, k))
