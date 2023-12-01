"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""
from collections import defaultdict

N = int(input())

p = []
cnt = 0
x_cnt = defaultdict(int); y_cnt = defaultdict(int)

for i in range(N):
    x, y = map(int, input().split())
    x_cnt[x] += 1; y_cnt[y] += 1
    p.append((x,y))

rats = 0 # right angled triangles
for x, y in p:
    rats += (x_cnt[x] - 1) * (y_cnt[y] - 1)

print(rats)
