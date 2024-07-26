import sys
input = sys.stdin.read

def bubble_sort(arr):
    swap_count = 0
    n = len(arr)
    for i in range(n):
        for j in range(1, n - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swap_count += 1
    return swap_count

def main():
    data = input().splitlines()
    p = int(data[0])  # 테스트 케이스의 수
    results = []
    
    for i in range(1, p + 1):
        line = data[i].split()
        index = line[0]
        array = list(map(int, line[1:]))
        swap_count = bubble_sort(array)
        results.append(f"{index} {swap_count}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
