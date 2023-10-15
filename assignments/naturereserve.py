from heapq import heappush, heappop
from sys import stdin, stdout

ds = int(input())

def prims(graph, sources):
    q = []
    for source in sources:
        heappush(q, (0, source) )

    taken = set()
    activate = 0
    tracker = 0
    
    while q:
        w, v = heappop(q)

        if v not in taken:
            activate += w
            tracker += 1
            taken.add(v)

            for nb in range(len(graph[v - 1])):
                if (graph[v - 1][nb] != -1) and ((nb + 1) not in taken):
                    heappush( q, (graph[v - 1][nb], (nb + 1)) )
                    
    return (activate, tracker)


for i in range(ds):
    n, m, l, s = map(int, input().split())

    sources = list(map(int, input().split()))

    graph = []
    for r in range(n):
        v = []
        for c in range(n):
            v.append(-1)
        graph.append(v)

    for i in range(m):
        u, v, w = map(int, input().split())

        graph[u -1][v - 1] = w
        graph[v -1][u - 1] = w

    activate, tracker = prims(graph, sources)

    print(activate + ((tracker-1) * 10))
