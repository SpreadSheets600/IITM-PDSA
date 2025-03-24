def partitionPos(arr, pivot):
    arr[pivot], arr[0] = arr[0], arr[pivot]
    l = 1
    r = len(arr) - 1
    while l < r:
        while arr[l] < arr[0]:
            l += 1
        while arr[r] >= arr[0]:
            r -= 1
        arr[l], arr[r] = arr[r], arr[l]

    return l - 1


def MoM7(arr):
    if len(arr) <= 7:
        arr.sort()
        return arr[len(arr) // 2]

    # Construct list of block medians
    M = []

    for i in range(0, len(arr), 7):
        X = arr[i : i + 7]
        X.sort()
        M.append(X[len(X) // 2])

    return MoM7(M)


def MoM7Pos(arr):
    mom = MoM7(arr)
    return partitionPos(arr, arr.index(mom))


arr = [int(item) for item in input().split(' ')]
print(MoM7Pos(arr))
