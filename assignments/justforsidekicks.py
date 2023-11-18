"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  Resources:

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

N, Q = map(int, input().split())
g_vals = list(map(int, input().split()))

gem_vals = dict()
for i in range(len(g_vals)):
    gem_vals[i + 1] = g_vals[i]

gem_type = input()
gems = [ int(i) for i in gem_type ]

# process queries
for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        gems[query[1]-1] = query[2]
    elif query[0] == 2:
        gem_vals[query[1]] = query[2]
    elif query[0] == 3:
        total = 0
        for i in range(query[1]-1, query[2]):
            total += gem_vals[gems[i]]
        print(total)
