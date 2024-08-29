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



#다른풀이 ------------------------------------------
def update(index, value, tree, max_val):
    while index <= max_val:
        tree[index] += value
        index += index & (-index)

def query(index, tree):
    sum = 0
    while index > 0:
        sum += tree[index]
        index -= index & (-index)
    return sum

def count_inversions(array):
    max_val = max(array)
    tree = [0] * (max_val + 1)
    inversions = 0
    for i in range(len(array)):
        inversions += query(max_val, tree) - query(array[i], tree)
        update(array[i], 1, tree, max_val)
    return inversions

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    p = int(data[0])  # 테스트 케이스의 수
    results = []

    for i in range(1, p + 1):
        line = data[i].split()
        index = line[0]
        array = list(map(int, line[1:]))
        inversions = count_inversions(array)
        results.append(f"{index} {inversions}")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
