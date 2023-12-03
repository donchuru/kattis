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
    visited = set()
    visited.add((0,0))

    dist = [[float('inf')] * COLS for _ in range(ROWS)]
    dist[0][0] = 0

    q = []
    heappush( q, (0, (0,0)) )

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    while q:
        w, node = heappop(q) # handles the min requirement
        r, c = node
    
        if w > dist[r][c]:
            continue
        
        visited.add((r, c))

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if ( (nr in range(ROWS)) and (nc in range(COLS)) and ((nr, nc) not in visited) ):
                # if jumping down (-ve) just use 0 as edge weight
                jump = max( dist[r][c] , max(0, (graph[nr][nc] - graph[r][c])) )
                
                if jump < dist[nr][nc]:
                    dist[nr][nc] = jump
                    heappush( q, (jump, (nr, nc)) )
    
    print(dist[-1][-1])

graph = []
M, N = map(int, input().split())
for i in range(M):
    graph.append(list(map(int, input().split())))
mst(graph, M, N)
