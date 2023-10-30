"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  KMP algorithm lifted from PyRival

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

"""
Tip: This is a KMP problem. Think about a property of the input that does not change if the input values were rotated around the clock (by the same amount). Also recall the trick mentioned in the slides for dealing with cyclic sequences: it is sometimes helpful to deal with the sequence concatenated with itself once so you don't have to worry about the cyclic part.
"""

# KMP lifted from PyRival
def partial(s):
    g, pi = 0, [0] * len(s)
    for i in range(1, len(s)):
        while g and (s[g] != s[i]):
            g = pi[g - 1]
        pi[i] = g = g + (s[g] == s[i])

    return pi

def string_find(s, pat):
    pi = partial(pat)

    g = 0
    for i in range(len(s)):
        while g and pat[g] != s[i]:
            g = pi[g - 1]
        g += pat[g] == s[i]
        if g == len(pi):
            return True

    return False


n = int(input())

clock1 = sorted(list(map(int, input().split()))); clock1 += clock1
clock2 = sorted(list(map(int, input().split()))); clock2 += clock2

# print(clock1)
# print(clock2)

c1diff, c2diff = [], []
for i in range(1, n*2):
    c1diff.append(((clock1[i] - clock1[i-1])) % 360000)
    c2diff.append(((clock2[i] - clock2[i-1])) % 360000)

# print(c1diff)
# print(c2diff)

if (string_find(c1diff, c2diff[:n])):
    print("possible")
else:
    print("impossible")
