def dijkstra(WList, s):
    infinity = 1 + len(WList.keys()) * max(
        [d for u in WList.keys() for (v, d) in WList[u]]
    )
    (visited, distance, prev) = ({}, {}, {})
    for v in WList.keys():
        (visited[v], distance[v], prev[v]) = (False, infinity, None)
    distance[s] = 0
    for u in WList.keys():
        nextd = min([distance[v] for v in WList.keys() if not visited[v]])
        nextvlist = [
            v for v in WList.keys() if (not visited[v]) and distance[v] == nextd
        ]
        if nextvlist == []:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        for v, d in WList[nextv]:
            if not visited[v]:
                if distance[v] > distance[nextv] + d:
                    distance[v] = distance[nextv] + d
                    prev[v] = nextv
    return (distance, prev)


def min_cost_walk(WList, S, D, V):
    distance1, path1 = dijkstra(WList, S)
    distance2, path2 = dijkstra(WList, V)
    tot_dist = distance1[V] + distance2[D]
    Route_S_V = []
    Route_V_D = []
    # shortest route for S to V
    if distance1[V] != 0:
        dest = V
        while dest != S:
            Route_S_V = [dest] + Route_S_V
            for i, j in path1.items():
                if dest == i:
                    dest = j
                    break
        Route_S_V = [dest] + Route_S_V
    # shortest route for V to D
    if distance2[D] != 0:
        dest = D
        while dest != V:
            Route_V_D = [dest] + Route_V_D
            for i, j in path2.items():
                if dest == i:
                    dest = j
                    break
        Route_V_D = [dest] + Route_V_D
    Route_S_D = Route_S_V[:-1] + Route_V_D
    return (tot_dist, Route_S_D)


size = int(input())
edges = eval(input())
S = int(input())
D = int(input())
V = int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:  # for create list for undirected graph
    WL[ed[0]].append((ed[1], ed[2]))
    WL[ed[1]].append((ed[0], ed[2]))
print(min_cost_walk(WL, S, D, V))
