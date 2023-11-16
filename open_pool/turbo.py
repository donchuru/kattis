"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

from sys import stdin
for ip in stdin:
    N = int(ip)
    n_to_phase = dict()

    res = []

    for i in range(N):
        n_to_phase[int(input())] = i + 1

    l = 1
    r = N
    rflag = False
    while l <= r:
        if not rflag:
            i = l

            res.append(abs(n_to_phase[i] - i))
            ahead = n_to_phase[i]
            
            for k in n_to_phase:
                if n_to_phase[k] < ahead:
                    n_to_phase[k] += 1

            n_to_phase[i] = i

            l += 1
            rflag = True

        else:
            i = r

            res.append(abs(n_to_phase[i] - i))
            ahead = n_to_phase[i]
            
            for k in n_to_phase:
                if n_to_phase[k] > ahead:
                    n_to_phase[k] -= 1

            n_to_phase[i] = i

            r -= 1
            rflag = False


    for i in res:
        print(i)
