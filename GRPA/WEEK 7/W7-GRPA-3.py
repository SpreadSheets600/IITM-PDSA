def tuplesort(L, index):
    L_ = []
    for t in L:
        L_.append(t[index : index + 1] + t[:index] + t[index + 1 :])
    L_.sort()

    L__ = []
    for t in L_:
        L__.append(t[1 : index + 1] + t[0:1] + t[index + 1 :])
    return L__


def no_overlap(L):
    sortedL = tuplesort(L, 2)
    accepted = [sortedL[0][0]]
    for i, s, f in sortedL[1:]:
        if s > L[accepted[-1]][2]:
            accepted.append(i)
    return accepted
