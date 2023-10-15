"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

from collections import defaultdict
from heapq import heappop, heappush

n, m = map(int, input().split())

# build graph
graph = defaultdict(set)
for i in range(m):
    u, v = map(str, input().split())
    graph[u].add(v)
    graph[v].add(u)

armies = dict()
for i in range(n):
    armies[str(i + 1)] = int(input())

# print(armies)

def dijkstra(graph, island):
    army_sf = 0
    conquered = set()

    q = []
    heappush(q, (armies[island], island))
    i = 0 # we wanna make sure our island '1' is conquered

    while q:
        army_size, curr_island = heappop(q)

        if ( army_size < army_sf ) or i == 0:
            conquered.add(curr_island)
            army_sf += army_size
        else:
            continue # so that we dont expand the neighbours of a node we didn't conquer

        for nb in graph[curr_island]:
            if nb not in conquered:
                # let it sit in the queue for processing (to see if we can conquer it)
                heappush(q, (armies[nb], nb))
                conquered.add(nb)

        i += 1
        
    return army_sf

print(dijkstra(graph, '1'))
