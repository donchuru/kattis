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
from collections import deque

c, p, x, l = input().split()

c = int(c)
p = int(p)

# build graph
graph = defaultdict(set)
for i in range(p):
    u, v = input().split()
    graph[u].add(v)
    graph[v].add(u)

# get neighbour count for all countries
nbr_count_tracker = dict()
for i in graph:
    nbr_count_tracker[i] = len(graph[i])

# print(nbr_count_tracker)
# print(graph)

# bfs through the whole graph
left = set()
def bfs(graph, start):
    q = deque()
    q.append(start)
    left.add(start)

    while q:
        leaving = q.popleft()

        for nbr in graph[leaving]:
            if nbr not in left:
                nbr_count_tracker[nbr] -= 1

                if nbr_count_tracker[nbr] <= (len(graph[nbr])/2):
                    left.add(nbr)
                    q.append(nbr)

bfs(graph, l)
if x in left: print("leave")
else: print("stay")
