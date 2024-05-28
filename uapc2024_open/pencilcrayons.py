N, K = map(int, input().split())

res = 0
for _ in range(N):
    res += (K - len(set(input().split())))

print(res)
