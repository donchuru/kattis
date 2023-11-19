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
    def __init__(self, n):
        self.n = n
        self.ftree = [0] * (self.n + 1)

    def sum(self, index):
        out = 0
        index += 1
        while index > 0:
            out += self.ftree[index]
            index -= index & (-index)

        return out

    def update(self, index, delta):
        index += 1
        while (index <= self.n):
            self.ftree[index] += delta
            index += index & (-index)

    def construct(self, x):
        for i in range(1, self.n + 1):
            self.ftree[i] = 0

        for i in range(self.n):
            self.update(i, x[i])



    
    
    

N, K = map(int, input().split())

ft = FenwickTree(N)
x = [0 for i in range(N)]
ft.construct(x)

print(ft.ftree)

for i in range(K):
    query = list(input().split())
    
    if query[0] == 'F':
        # flip the kth bit
        k = int(query[1]) - 1
        
        if ft.ftree[k] == 0:
            ft.update(k, 1)
        elif ft.ftree[k] == 1:
            ft.update(k, -1)

        print(ft.ftree)

    elif query[0] == 'C':
        j, k = map(int, query[1:])
        print(ft.sum(k) - ft.sum(j))
