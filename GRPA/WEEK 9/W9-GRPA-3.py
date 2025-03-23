def LDS(L):
    if not L:
        return []

    n = len(L)
    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if L[j] > L[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

    max_length = max(dp)
    max_index = dp.index(max_length)

    lds = []
    current = max_index
    while current != -1:
        lds.append(L[current])
        current = parent[current]

    lds.reverse()

    return lds
