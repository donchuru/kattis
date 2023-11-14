from heapq import heappush, heappop
from sys import stdin, stdout
from collections import defaultdict

input = stdin.readline
ds = int(input())

def prims(graph, source):
    q = []
    heappush( q, (0, source) )

    taken = set()
    activate = 0
    tracker = -1
    
    while q:
        # print("q:", q)
        # print("taken", taken)
        w, v = heappop(q)
        # print("w", w, "v", v)

        if v in taken:
            continue

        activate += w
        tracker += 1
        taken.add(v)

        for nb_w in graph[v]:
            if nb_w[0] not in taken:
                heappush(q, (nb_w[1], nb_w[0]))
                    
    return (activate, tracker)

for i in range(ds):
    input = stdin.readline
    n, m, l, s = map(int, input().split())

    sources = list(map(int, input().split()))

    graph = defaultdict(list)

    for i in range(m):
        u, v, w = map(int, input().split())

        graph[u].append((v, w))
        graph[v].append((u, w))

    for source in sources:
        graph[n+1].append((source, 0))
    
    # print(len(graph))
    
    # print(graph)

    total_energy = 0

    activate, tracker = prims(graph, n+1)
    # print("activate", activate)
    # print("tracker", tracker)
    total_energy += (activate + ((tracker-1) * l))
    for i in range(s - 1):
        total_energy -= l
    
    # print(total_energy)
    stdout.write(str(total_energy))
