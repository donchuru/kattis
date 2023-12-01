"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  Resources:
  cpbook-code repo: MCBM

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""
import random

match = []
vis = []
AL = []

N, M = map(int, input().split())

for i in range(N):
    AL.append(list(map(int, input().split()))[1:])

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

print(MCBM)
