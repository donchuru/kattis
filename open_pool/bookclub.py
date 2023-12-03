"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  Resources:
  CP4, cp-code repo

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

import random

N_ip, M_ip = map(int, input().split())
graph = [[] for _ in range(N_ip)]

for _ in range(M_ip):
    u, v = map(int, input().split())
    graph[u].append(v)

N, M = N_ip, N_ip
AL = graph

match = []
vis = []

def Aug(L):
    global match, vis, AL

    if vis[L]:
        return 0
    vis[L] = 1
    for R in AL[L]:
        if match[R] == -1 or Aug(match[R]):
            match[R] = L
            return 1
    return 0

def main():
    global match, vis, AL

    V = N + M
    Vleft = N

    freeV = set()
    for L in range(Vleft):
        freeV.add(L)
    match = [-1] * V
    MCBM = 0

    for L in range(Vleft):
        candidates = []
        for R in AL[L]:
            if match[R] == -1:
                candidates.append(R)
        if len(candidates) > 0:
            MCBM += 1
            freeV.remove(L)
            a = random.randrange(len(candidates))
            match[candidates[a]] = L
 
    for f in freeV:
        vis = [0] * Vleft
        MCBM += Aug(f)

    return MCBM

matchings = main()

# print(matchings)
if matchings == N_ip:
    print("YES")
else:
    print("NO")
