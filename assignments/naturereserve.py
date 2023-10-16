from heapq import heappush, heappop
from sys import stdin, stdout

input = stdin.readline
ds = int(input())

def prims(graph, source):
    q = []
    heappush( q, (0, source) )

    taken = set()
    activate = 0
    tracker = 0
    
    while q:
        w, v = heappop(q)

        if v in taken:
            continue

        activate += w
        tracker += 1
        taken.add(v)

        for nb in range(len(graph[v - 1])):
            if (graph[v - 1][nb] != -1) and ((nb + 1) not in taken):
                heappush( q, (graph[v - 1][nb], (nb + 1)) )
                    
    return (activate, tracker)

for i in range(ds):
    input = stdin.readline
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

    total_energy = 0

    for source in sources:
        activate, tracker = prims(graph, source)
        # print("activate", activate)
        # print("tracker", tracker)
        total_energy += (activate + ((tracker-1) * l))
    

    stdout.write(str(total_energy))
