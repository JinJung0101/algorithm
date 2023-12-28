# n, k = map(int(input().split()))
# things = [[0,0]]
# d = [[0]*(k+1) for _ in range(n+1)]

# for i in range(n):
#     things.append(list(map(int, input().split())))


# for i in range(1, n+1):
#     for j in range(1, k+1):
#         w = things[i][0]
#         v = things[i][0]

#         # 배낭의 무게 제한이 물건의 무게보다 작은 경우, i번째 물건을 배낭에 넣을 수 없습니다.
#         # 그러므로 i-1번째 물건까지 고려하고 배낭의 무게 제한이 j일 때의 최대 가치를 동적 프로그래밍 테이블에 저장합니다.
#         if j < w:
#             d[i][j] = d[i-1][j]
#         else:
#             d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

# print(d[n][k])

import sys

inp = sys.stdin.readline

n, k = map(int, inp().split())
things = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    things.append(list(map(int, inp().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = things[i][0]
        v = things[i][1]
        
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)
            
                 
print(d[n][k])