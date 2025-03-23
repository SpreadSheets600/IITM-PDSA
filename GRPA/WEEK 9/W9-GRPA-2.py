def MaxCoinPath(M, x1, y1, x2, y2):
    rows = len(M)
    cols = len(M[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    dp[x1][y1] = M[x1][y1]

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if i == x1 and j == y1:
                continue

            up = dp[i - 1][j] if i > x1 else 0
            left = dp[i][j - 1] if j > y1 else 0

            dp[i][j] = M[i][j] + max(up, left)

    return dp[x2][y2]


M = eval(input())
(x1, y1) = eval(input())
(x2, y2) = eval(input())
print(MaxCoinPath(M, x1, y1, x2, y2))
