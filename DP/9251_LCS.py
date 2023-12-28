def lcs(X, Y):
# LCS 테이블 초기화
    m = len(X)
    n = len(Y)
    lcs_table = [[0 for _ in range(n+1)] for _ in range(m+1)]
# LCS 테이블 채우기
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0 
            elif X[i-1] == Y[j-1]:
                lcs_table[i][j] = lcs_table[i-1][j-1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])
    
    return lcs_table[m][n]

X = input()
Y = input()

print(lcs(X,Y))
    