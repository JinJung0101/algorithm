#input: 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
#각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.
#output: 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 
#출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

#0.소수 판별 함수정의 
#1.주어진 수를 2로 나눈다. 
#2.나누어진 숫자 모두 소수가 될때까지(for) +,- 한다. 

def sosu(x):
    if x==1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x%i==0:
                return False
    return True
    
t = int(input())

for i in range(t):
    n = int(input())
    
    tmp = n//2
    while tmp>0:
        if sosu(tmp) and sosu(n-tmp):
            print(tmp, n-tmp)
            break
        else:
            tmp -= 1