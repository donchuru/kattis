"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  Resources:
  CP4

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""
from heapq import heappop, heappush

def mst(graph, ROWS, COLS):
    min_edge = float('inf')
    visited = set()
    visited.add((0,0))

    q = []
    heappush( q, (0, (0,0)) )

    while q:
        w, node = heappop(q) # handles the min requirement
        r, c = node
    
        # print(r, c)

        if r == ROWS-1 and c == COLS-1:
            min_edge = min(min_edge, w)
            break
        
        visited.add((r, c))

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if ( (nr in range(ROWS)) and (nc in range(COLS)) and ((nr, nc) not in visited) and max(0, (graph[nr][nc] - graph[r][c])) < min_edge ):
                # if jumping down (-ve) just use 0 as edge weight
                jump = max(0, (graph[nr][nc] - graph[r][c]))
                heappush( q, (max(jump, w), (nr, nc)) )
    
    print(min_edge)

graph = []
M, N = map(int, input().split())
for i in range(M):
    graph.append(list(map(int, input().split())))
mst(graph, M, N)
