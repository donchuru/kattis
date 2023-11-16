"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""
from math import sqrt
N, M = map(int, input().split())

cnt = 0
sqrt_M = int(sqrt(M))
for i in range(1, min(sqrt_M, N) + 1):
    if M % i == 0 and (M // i) <= N:
        cnt += 1
        if i != M // i:  # count the reverse if the factors are different
            cnt += 1

print(cnt)
