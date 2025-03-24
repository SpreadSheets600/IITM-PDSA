import math


def findLeft(A, x, l, r):
    if l > r:
        return None

    mid = (l + r) // 2
    if A[mid] == x:
        if mid == 0 or A[mid] != A[mid - 1]:
            return mid
        else:
            return findLeft(A, x, l, mid)
    elif x > A[mid]:
        return findLeft(A, x, mid + 1, r)
    else:
        return findLeft(A, x, l, mid - 1)


def findRight(A, x, s, l, r):
    if l > r:
        return None

    mid = math.ceil((l + r) / 2)
    if A[mid] == x:
        if mid == s - 1 or A[mid] != A[mid + 1]:
            return mid
        else:
            return findRight(A, x, s, mid, r)
    elif x > A[mid]:
        return findRight(A, x, s, mid + 1, r)
    else:
        return findRight(A, x, s, l, mid - 1)


def findOccOf(L, x):
    s = len(L)
    if s < 1:
        return None

    start = findLeft(L, x, 0, s - 1)
    end = findRight(L, x, s, 0, s - 1)
    return (start, end)


A = [int(item) for item in input().split(' ')]
x = int(input())
timeout = 1.0  # Timeout in sec
