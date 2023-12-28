# 동전의 종류와 목표 금액을 입력받습니다.
n, k = map(int, input().split())

# 동전의 가치를 저장할 리스트를 초기화합니다.
coin = []

# 현재 고려하고 있는 동전의 인덱스와 사용한 동전의 개수를 저장할 변수를 초기화합니다.
index = 0
result = 0

# 동전의 종류 수만큼 반복하면서, 각 동전의 가치를 입력받습니다.
for i in range(n):
    x = int(input())  # 동전의 가치를 입력받습니다.
    coin.append(x)  # 입력받은 동전의 가치를 리스트에 추가합니다.

# 동전의 가치를 내림차순으로 정렬합니다. 이렇게 하면 가장 가치가 큰 동전부터 고려할 수 있습니다.
coin.sort(reverse=True)

# 동전의 종류 수만큼 반복하면서, 각 동전을 고려합니다.
for i in range(n):
    # 만약 현재 동전의 가치가 목표 금액보다 작거나 같다면, 그 동전을 최대한 많이 사용합니다.
    if coin[i] <= k:
        index = i  # 현재 고려하고 있는 동전의 인덱스를 저장합니다.
        result += k // coin[i]  # 목표 금액을 현재 동전으로 나눈 몫을 결과에 더합니다. 이것은 현재 동전으로 만들 수 있는 최대 금액을 나타냅니다.
        k = k - ((k // coin[i]) * coin[i])  # 목표 금액에서 현재 동전으로 만든 금액을 뺍니다. 이렇게 하면 남은 목표 금액을 계산할 수 있습니다.

# 필요한 동전의 최소 개수를 출력합니다.
print(result)
