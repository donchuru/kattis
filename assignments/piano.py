"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  Resources: 
  CP4
  PyRival: Dinic algorithm

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

from collections import defaultdict, deque

INF = float("inf")

class Dinic:
    def __init__(self, n):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, a, b, c, rcap=0):
        self.adj[a].append([b, len(self.adj[b]), c, 0])
        self.adj[b].append([a, len(self.adj[a]) - 1, rcap, 0])

    def dfs(self, v, t, f):
        if v == t or not f:
            return f

        for i in range(self.ptr[v], len(self.adj[v])):
            e = self.adj[v][i]
            if self.lvl[e[0]] == self.lvl[v] + 1:
                p = self.dfs(e[0], t, min(f, e[2] - e[3]))
                if p:
                    self.adj[v][i][3] += p
                    self.adj[e[0]][e[1]][3] -= p
                    return p
            self.ptr[v] += 1

        return 0

    def calc(self, s, t):
        flow, self.q[0] = 0, s
        for l in range(31):  # l = 30 maybe faster for random data
            while True:
                self.lvl, self.ptr = [0] * len(self.q), [0] * len(self.q)
                qi, qe, self.lvl[s] = 0, 1, 1
                while qi < qe and not self.lvl[t]:
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
                            self.q[qe] = e[0]
                            qe += 1
                            self.lvl[e[0]] = self.lvl[v] + 1

                p = self.dfs(s, t, INF)
                while p:
                    flow += p
                    p = self.dfs(s, t, INF)

                if not self.lvl[t]:
                    break

        return flow


n = int(input())

for _ in range(n):

    m, p = map(int, input().split())

    if p <= 0:
        print("serious trouble")
        break

    p //= 2

    pianos_to_days_five = defaultdict(list)
    pianos_to_days_seven = defaultdict(list)

    v_five = set()
    v_seven = set()
    for i in range(1, m+1):
        b, e = map(int, input().split())

        for j in range(b, e + 1):
            # populate our seven day network
            pianos_to_days_seven[i].append(j + m)
            v_seven.add(j + m)

            # populate our five day network
            # skip if its a weekend
            if j % 7 == 0 or j % 7 == 6:
                continue
            
            pianos_to_days_five[i].append(j + m) # offest by m to avoid clashing pianos with days
            v_five.add(j + m)
    
    # print(pianos_to_days_five)

    # TRY FOR 5 DAYS
    v_five_count = max(v_five) if v_five else 0
    source, sink = 0, v_five_count + 1
    mf = Dinic(v_five_count + 2)
    
    # connect source to pianos
    for sp in pianos_to_days_five:
        mf.add_edge(source, sp, 1)

    # connect pianos to days they can be moved
    for pd in pianos_to_days_five:
        for day in pianos_to_days_five[pd]:
            mf.add_edge(pd, day, 1)
    
    # connect the days pianos can be moved to sink (add constraint)
    for day in v_five:
        mf.add_edge(day, sink, p)

    five_day = (mf.calc(source, sink))

    if five_day == m:
        print("fine")
        continue


    # TRY FOR 7 DAYS
    # print(pianos_to_days_seven)

    v_seven_count = max(v_seven) if v_seven else 0

    source_seven, sink_seven = 0, v_seven_count + 1
    mf_seven = Dinic(v_seven_count + 2)
    
    # connect source to pianos
    for sp in pianos_to_days_seven:
        mf_seven.add_edge(source_seven, sp, 1)

    # connect pianos to days they can be moved
    for pd in pianos_to_days_seven:
        for day in pianos_to_days_seven[pd]:
            mf_seven.add_edge(pd, day, 1)
    
    # connect the days pianos can be moved to sink (add constraint)
    for day in v_seven:
        mf_seven.add_edge(day, sink_seven, p)

    seven_day = (mf_seven.calc(source_seven, sink_seven))
    
    if seven_day == m:
        print("weekend work")
    
    else:
        print("serious trouble")
