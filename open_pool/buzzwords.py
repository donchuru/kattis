"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  Resources: 
  CP4, cpbook-code Repo: sa_lcp.py

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

def sort_cyclic_shifts(s):
    s = [*map(ord, s)]
    n = len(s)
    alphabet = 256
    p = [0] * n
    c = [0] * n
    cnt = [0] * max(alphabet, n)
    for i in range(n):
        cnt[s[i]] += 1
    for i in range(1, alphabet):
        cnt[i] += cnt[i-1]
    for i in range(n):
        cnt[s[i]] -= 1
        p[cnt[s[i]]] = i
    c[p[0]] = 0
    classes = 1
    for i in range(1, n):
        if s[p[i]] != s[p[i-1]]:
            classes += 1
        c[p[i]] = classes - 1
    pn = [0] * n
    cn = [0] * n
    h = 0
    while (1 << h) < n:
        for i in range(n):
            pn[i] = p[i] - (1 << h)
            if pn[i] < 0:
                pn[i] += n
        for i in range(classes):
            cnt[i] = 0
        for i in range(n):
            cnt[c[pn[i]]] += 1
        for i in range(1, classes):
            cnt[i] += cnt[i-1]
        for i in range(n-1, -1, -1):
            cnt[c[pn[i]]] -= 1
            p[cnt[c[pn[i]]]] = pn[i]
        cn[p[0]] = 0
        classes = 1
        for i in range(1, n):
            cur = (c[p[i]], c[(p[i] + (1 << h)) % n])
            prev = (c[p[i-1]], c[(p[i-1] + (1 << h)) % n])
            if cur != prev:
                classes += 1
            cn[p[i]] = classes - 1
        c, cn = cn, c
        h += 1
    return p

# returns the suffix array of s
def suffix_array_construction(s):
    return sort_cyclic_shifts(s+'\0')[1:]


from sys import stdin

for line in stdin:
    if line.strip() == "":
        break

    s = line.replace(" ", "")
    n = len(s)
    sa = suffix_array_construction(s)

    for l in range(1, n):
        cnt, max_cnt = 1, 1
        
        for i in range(1, n):
            if s[sa[i]:sa[i]+l] == s[sa[i-1]:sa[i-1]+l]: # substring repeated
                cnt += 1
                max_cnt = max(max_cnt, cnt) # track most repeated substring
            else:
                cnt = 1

        if max_cnt > 1:
            print(max_cnt)
        else:
            print()
            break
