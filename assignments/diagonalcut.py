"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

from math import gcd
M, N = map(int, input().split())
gcd_val = gcd(M, N)

M //= gcd_val; N //= gcd_val
# if any of the sides is even
if M % 2 == 0 or N % 2 == 0: 
  print(0)
else: # if the normalized versions are both 0 or odd
  print(gcd_val)
