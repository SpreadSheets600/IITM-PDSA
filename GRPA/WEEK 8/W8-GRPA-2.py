def mergeAndCount(A, B):
    (m, n) = len(A), len(B)
    (C, i, j, k, count) = ([], 0, 0, 0, 0)
    while k < m + n:
        if i == m:
            C.append(B[j])
            (j, k) = (j + 1, k + 1)
        elif j == n:
            C.append(A[i])
            (i, k) = (i + 1, k + 1)
        elif A[i] < B[j]:
            C.append(A[i])
            (i, k) = (i + 1, k + 1)
        else:
            C.append(B[j])
            (j, k, count) = (j + 1, k + 1, count + (m - i))
    return (C, count)


def sortAndCount(A):
    n = len(A)

    if n <= 1:
        return (A, 0)

    (L, countL) = sortAndCount(A[: n // 2])
    (R, countR) = sortAndCount(A[n // 2 :])

    (B, countB) = mergeAndCount(L, R)

    return (B, countL + countR + countB)


def countIntersection(X1, X2):
    # Sort according to one points while keeping the matching of points in X1 to X2
    combined = [(X1[i], X2[i]) for i in range(0, len(X1))]
    combined.sort()
    X1, X2 = zip(*combined)

    # Now we just need to count the inversions in X2 for number of intersection points.
    return sortAndCount(X2)[1]


L1 = [int(i) for i in input().split(' ')]
L2 = [int(i) for i in input().split(' ')]
timeout = 2.0  # Timeout in sec
