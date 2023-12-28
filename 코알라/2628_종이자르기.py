# 가로 세로 길이의 2차원 배열 만들기
# 자르기 횟수만큼 돌며 if 가로(0) elif 세로(1) 구분하여 자르기
# 자르기를 어떻게 구현할것인가 
# return 넓이(가로*세로)


from sys import stdin

width, length = map(int, stdin.readline().split())

# 종이 만들기
paper = [[0]*width for _ in range(length)]
n = int(stdin.readline())

for i in range(n):
    w_or_l, num = map(int, stdin.readline().split())
    for j in range(length):
        for k in range(width):
            if w_or_l == 0:
                paper[j][k]
            elif w_or_l == 1:
                paper[j][k]
# 구간 나눈곳에 표시한후
# 표시된 숫자를 합쳐(넓이)제일 큰 숫자 출력