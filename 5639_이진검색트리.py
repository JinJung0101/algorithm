#input: 이진검색트리를 전위 순회한 결과
#output: 위에 주어진 트리를 후위 순회한 결과
#1.이진검색트리 전위 순회한 결과로 후위 순회한 결과를 출력한다. 
#이진검색트리의 특징이용: 
#루트 노드보다 큰 원소가 나오는 지점이 왼쪽 서브 트리와 오른쪽 서브 트리를 나누는 지점과 같다.
# 50 0
# 30 1
# 24 2
# 5  3
# 28 4
# 45 5 
# 98 6
# 52 7
# 60 8

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break


def postorder(start, end):
    if start > end:
        return
    mid = end + 1                         # 오른쪽 노드가 없을 경우

    for i in range(start+1, end+1):
        if nums[start] < nums[i]:
            mid = i
            break

    postorder(start+1, mid-1)               # 왼쪽 확인
    postorder(mid, end)                   # 오른쪽 확인
    print(nums[start])

postorder(0, len(nums)-1)