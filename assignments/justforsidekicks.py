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
    
    # use as rsq operation i.e. rsq(i, j) = rsq(j) - rsq(i)
    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def query_range(self, start, end):
        return self.query(end+1) - self.query(start)
    


# ft = FenwickTree([1,2,3,4,5,6])
# print(ft.query_range(3, 5))


N, Q = map(int, input().split())
type_vals = list(map(int, input().split()))

gem_type = input()

gem_trees = [0] + [ FenwickTree([0] * 200001) for i in range(6) ]
for i in range(len(gem_type)):
    # print(gem_type[i])
    gem_trees[int(gem_type[i])].update(i+1, 1)

# process queries
for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        k = query[1]
        p = query[2]
        for i in range(1, 7):
            # print(gem_trees[i].query_range(k, k))
            if gem_trees[i].query_range(k, k) == 1:
                gem_trees[i].update(k, -1)
                break
            
        gem_trees[p].update(k, 1)



    elif query[0] == 2:
        type_vals[query[1]-1] = query[2]


    elif query[0] == 3:
        total = 0

        for i in range(1, len(gem_trees)):
            # print("range sum", gem_trees[i].query_range(query[1], query[2]))
            total += gem_trees[i].query_range(query[1], query[2]) * type_vals[i - 1]

        print(total)
