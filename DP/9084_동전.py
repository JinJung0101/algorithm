# input 
# 테스트 케이스의 개수
# 동전의 가지 수 : N
# N가지 동전의 각 금액의 오름차순 : val
# N가지 동전으로 만들어야 할 금액 : 

# def coin_combination(coin_types, target_amount):
#     cache = [0] * (target_amount + 1)
#     cache[0] = 1

#     for coin in coin_types:
#         for amount in range(coin, target_amount + 1):
#             cache[amount] += cache[amount - coin]

#     return cache[target_amount]

# T = int(input())  # 테스트 케이스 수
# c_t = int(input())  # 동전의 종류 수
# coins = list(map(int, input().split()))  # 동전의 종류
# t_a = int(input())  # 목표 금액

# print(coin_combination(coins, t_a))

# solve 함수는 동전의 종류 수, 동전의 종류를 나타내는 리스트, 그리고 목표 금액을 인자로 받아 목표 금액을 만드는 경우의 수를 반환합니다.
def solve(n, coin_types, target_amount):
    # dp 배열을 초기화합니다. dp[i]는 금액 i를 만드는 경우의 수를 저장합니다.
    dp = [0 for _ in range(target_amount + 1)]
    
    # 금액 0을 만드는 방법은 동전을 아예 사용하지 않는 한 가지 방법만 있으므로 dp[0]은 1입니다.
    dp[0] = 1

    # 각 동전에 대해서
    for i in range(n):
        # 동전의 가치부터 목표 금액까지
        for j in range(coin_types[i], target_amount + 1):
            # j-coin_types[i] 금액을 만드는 방법에 현재 동전을 추가하여 j 금액을 만드는 방법을 구합니다.
            dp[j] += dp[j - coin_types[i]]
    
    # 목표 금액을 만드는 경우의 수를 반환합니다.
    return dp[target_amount]

# 테스트 케이스의 수를 입력받습니다.
T = int(input())

# 각 테스트 케이스에 대해서
for _ in range(T):
    # 동전의 종류 수를 입력받습니다.
    n = int(input())
    # 동전의 종류를 입력받습니다.
    coin_types = list(map(int, input().split()))
    # 목표 금액을 입력받습니다.
    target_amount = int(input())
    # solve 함수를 호출하여 결과를 출력합니다.
    print(solve(n, coin_types, target_amount))
