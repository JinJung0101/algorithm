import sys
input = sys.stdin.read

def can_distribute(heights, max_diff, h):
    count, current_sum = 1, 0
    for height in heights:
        if current_sum + height > max_diff:
            count += 1
            current_sum = height
            if count > h:
                return False
        else:
            current_sum += height
    return True

def main():
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    h = int(data[2])
    
    heights = [0] * n
    index = 3
    for _ in range(m):
        for j in range(n):
            heights[j] += int(data[index])
            index += 1

    left, right = max(heights), sum(heights)
    while left < right:
        mid = (left + right) // 2
        if can_distribute(heights, mid, h):
            right = mid
        else:
            left = mid + 1
    
    print(left)

if __name__ == "__main__":
    main()
