"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  Resources: 
  CP4, cpbook-code Repo: sa_lcp.py

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

from collections import defaultdict, deque

class MaxFlow:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # Residual capacity

    def ford_fulkerson(self, source, sink):
        max_flow = 0
        parent = self.bfs(source, sink)

        while parent:
            # Find the bottleneck capacity along the augmenting path
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Update capacities along the augmenting path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            # Add the bottleneck capacity to the max flow
            max_flow += path_flow

            # Find the next augmenting path
            parent = self.bfs(source, sink)

        return max_flow

    def bfs(self, source, sink):
        visited = set()
        queue = deque([source])
        parent = {source: None}

        while queue:
            u = queue.popleft()

            for v, capacity in self.graph[u].items():
                if v not in visited and capacity > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u

                    if v == sink:
                        return parent

        return None


n = int(input())

for _ in range(n):

    m, p = map(int, input().split())


    # try for 5 days
    pianos_to_days_five = defaultdict(list)
    pianos_to_days_seven = defaultdict(list)
    v = set()
    v_seven = set()
    for i in range(1, m+1):
        b, e = map(int, input().split())

        for j in range(b, e + 1):
            pianos_to_days_seven[i].append(j + m)
            v_seven.add(j + m)

            if j % 7 == 0 or j % 7 == 6:
                continue
            
            pianos_to_days_five[i].append(j + m) # offest by m to avoid clashing pianos with days

            v.add(j + m)
    
    # print(pianos_to_days_five)
    vertices = max(v)
    # print("v", v)
    source, sink = 0, vertices + 1
    mf = MaxFlow()
    
    # connect source to pianos
    for sp in pianos_to_days_five:
        mf.add_edge(source, sp, 1)

    # connect pianos to days they can be moved
    for pd in pianos_to_days_five:
        for day in pianos_to_days_five[pd]:
            mf.add_edge(pd, day, 1)
    
    # connect the days pianos can be moved to sink (add constraint)
    for day in v:
        mf.add_edge(day, sink, p//2)

    five_day = (mf.ford_fulkerson(source, sink))



    
    vertices_seven = max(v_seven)

    source_seven, sink_seven = 0, vertices_seven + 1
    mf_seven = MaxFlow()
    
    # connect source to pianos
    for sp in pianos_to_days_seven:
        mf_seven.add_edge(source_seven, sp, 1)

    # connect pianos to days they can be moved
    for pd in pianos_to_days_seven:
        for day in pianos_to_days_seven[pd]:
            mf_seven.add_edge(pd, day, 1)
    
    # connect the days pianos can be moved to sink (add constraint)
    for day in v_seven:
        mf_seven.add_edge(day, sink_seven, p//2)


    seven_day = (mf_seven.ford_fulkerson(source_seven, sink_seven))


    # print(m)
    # print(five_day)
    # print(seven_day)
    # print()

    if five_day == m:
        print("fine")

    elif seven_day == m:
        print("weekend work")
    
    elif five_day != m and seven_day != m:
        print("serious trouble")
