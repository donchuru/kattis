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

n, m = map(int, input().split())

debt = dict()
for i in range(n):
    debt[str(i)] = int(input())

# build graph
graph = defaultdict(set)
for i in range(m):
    u, v = map(str, input().split())
    graph[u].add(v)
    graph[v].add(u)


all_ppl = list(debt.keys())

def find_net(graph, all_ppl):
    visited = set()
    net = 0

    for p in all_ppl:
        if p in visited:
            continue

        q = deque()
        q.append(p)

        while q:
            curr = q.popleft()
            visited.add(curr)

            net += debt[curr]
            # print("net in bfs", net)

            for nb in graph[curr]:
                if nb not in visited:
                    q.append(nb)
                    visited.add(nb)
        
        # if this group of remaining friends couldnt resolve their debts, then stop right here and return impossible
        if net != 0:
            return net      
    return net

net_found = find_net(graph, all_ppl)
# print("net found", net_found)
if net_found != 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
