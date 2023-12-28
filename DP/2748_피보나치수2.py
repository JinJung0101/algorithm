# 첫째 줄에 n번째 피보나치 수를 출력

N = int(input())

def dp(n):
    # n+1 길이의 리스트를 생성하고 모든 값을 0으로 초기화합니다.
    cache = [0 for i in range(n+1)]
    # 피보나치 수열의 첫 번째와 두 번째 값을 지정합니다.
    cache[0] = 0
    cache[1] = 1

    # 2부터 n까지의 각 수에 대해 피보나치 수를 계산하고 저장합니다.
    for i in range(2, n+1):
        # 현재의 피보나치 수는 이전 두 피보나치 수의 합입니다.
        # 이전에 계산된 값을 cache에서 가져와 사용합니다.
        cache[i] = cache[i-2] + cache[i-1]

    # n번째 피보나치 수를 반환합니다.
    return cache[n]

print(dp(N))

    # if n > 2:
    #     return n
    # else:
    #     ans = (n-1) + (n-2)
    #     return ans



    #변수간 관계식 만들기
    #메모하기
    #가장작은문제의 상태파악
