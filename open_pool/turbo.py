"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  Resources:
  CP4
  PyRival Repo: Fenwick Tree

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def query_range(self, start, end):
        """get sum of values from x[start] to x[end] inclusive of both bounds"""
        return self.query(end+1) - self.query(start)

N = int(input())

num_to_idx = dict()
for i in range(1, N+1):
    num_to_idx[int(input())] = i

ft = FenwickTree( [0] + ([1]*N) ) # 0 -> swapped, 1 -> not yet swapped
swaps  = []
l, r = 1, N
for i in range(1, (N+1)):
    if i % 2 == 0:
        idx = num_to_idx[r]
        ft.update(idx, -1) # swap complete for idx
        swaps.append(ft.query_range(idx, N))
        r -= 1
    else:
        idx = num_to_idx[l]
        ft.update(idx, -1) # swap complete for idx
        swaps.append(ft.query_range(1, idx))
        l += 1
    
# print(swaps)
for i in swaps:
    print(i)
