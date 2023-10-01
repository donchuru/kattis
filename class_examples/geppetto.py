n, m = map(int, input().split())

restrictions = []
for i in range(m):
    r = tuple(map(int, input().split()))
    restrictions.append(r)

subsets = []

# generate all subsets
def dfs(i, path):

    if i >= n or len(path) >= 3:
        subsets.append(path)

    dfs(i + 1, path + [i])

    path.pop()
    dfs(i, path + [i])

dfs(1, [])

print(subsets)
