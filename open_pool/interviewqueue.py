"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

N = int(input())
candidates = list(map(int, input().split()))
cnt = 0
res = []
while True:
    if len(candidates) == 1:
        print(cnt)
        for left in res:
            if len(left) > 0:
                print(*left)
        print(*candidates)
        break

    tbr = [] # indices of candidates to be removed

    if candidates[0] < candidates[1]:
        tbr.append(0)

    for i in range(1, len(candidates)-1):
        if candidates[i] < candidates[i-1] or candidates[i] < candidates[i+1]:
            tbr.append(i)

    if candidates[-1] < candidates[-2]:
        tbr.append(-1)

    res.append( [candidates[i] for i in tbr] )
    # print(res)
    cnt += 1

    for i in sorted(tbr, reverse=True):
        del candidates[i]

    if len(tbr) == 0:
        print(cnt-1)
        for left in res:
            if len(left) > 0:
                print(*left)
        print(*candidates)
        break
