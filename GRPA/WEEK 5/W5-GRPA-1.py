def kruskal(WList):
    (edges, component, TE) = ([], {}, [])
    for u in WList.keys():
        edges.extend([(d, u, v) for (v, d) in WList[u]])
        component[u] = u
    edges.sort()
    for d, u, v in edges:
        if component[u] != component[v]:
            TE.append((u, v))
            c = component[u]
        for w in WList.keys():
            if component[w] == c:
                component[w] = component[v]
    return TE


def FiberLink(distance_map):
    R = kruskal(distance_map)
    S = 0
    for e in R:
        for ed in distance_map[e[0]]:
            if ed[0] == e[1]:
                S += ed[1]
    return S


size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1], ed[2]))
    WL[ed[1]].append((ed[0], ed[2]))
print(FiberLink(WL))
