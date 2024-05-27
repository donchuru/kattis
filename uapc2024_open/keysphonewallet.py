item_cnt = int(input())
items = set()

for _ in range(item_cnt):
    items.add(input())

np = []

if "keys" not in items:
    np.append("keys")

if "phone" not in items:
    np.append("phone")

if "wallet" not in items:
    np.append("wallet")

if len(np) == 0:
    print("ready")
else:
    for i in np:
        print(i)
