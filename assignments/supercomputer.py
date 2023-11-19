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

N, K = map(int, input().split())

x = [0 for i in range(N)]
ft = FenwickTree(x)

for i in range(K):
    query = list(input().split())
    
    if query[0] == 'F':
        # flip the kth bit
        k = int(query[1]) - 1
      
        # to get value at x[k], you do the rsq[k+1] - rsq[k]
        # reminder: rsq => range sum query; so cumulative sum at some index
        if (ft.query(k+1) - ft.query(k)) == 0:
            ft.update(k, 1)
        elif (ft.query(k+1) - ft.query(k)) == 1:
            ft.update(k, -1)

    elif query[0] == 'C':
        j, k = map(int, query[1:])
        print(ft.query(k) - ft.query(j-1))
