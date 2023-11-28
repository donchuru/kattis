"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

N = int(input())
p = []
for i in range(N):
    p.append(float((list(input().split()))[1]))
total = 0
p.sort(reverse=True)
for i, p in enumerate(p):
    total += (p * (i+1))
print(total)
