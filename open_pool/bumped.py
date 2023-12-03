"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

from collections import defaultdict
from heapq import heappop, heappush

n, m, f, s, t = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u].append((c, v))
    graph[v].append((c, u))

flights = defaultdict(list)
for _ in range(f):
    u, v = map(int, input().split())
    # graph[u].append((0, v))
    flights[u].append((0, v))


def dijkstra(start, goal):
    visited = defaultdict(lambda: float('inf'))
    q = []
    heappush(q, (0, start, False))

    while q:
        # print(q)
        running_cost, node, flew = heappop(q)

        if node == goal:
            return(running_cost)

        visited[node] = min(running_cost, visited[node])

        for nb_cost, nb_node in graph[node]:
            new_cost = running_cost + nb_cost # update running cost
            if (new_cost) < visited[nb_node]:
                heappush(q, (new_cost, nb_node, flew))
                visited[nb_node] = new_cost

        if flew: # if he already took a flight on this route
            continue

        for nb_cost, nb_node in flights[node]:
            if running_cost < visited[nb_node]:
                heappush(q, (running_cost, nb_node, True))
                visited[nb_node] = running_cost
                    

print( dijkstra(s, t) )
