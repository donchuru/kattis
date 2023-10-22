"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  binomial coefficient formula lifted from eClass (and ported to Python)

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""
from sys import stdin, stdout

input = stdin.readline
n, k = map(int, input().split())
keys = sorted(list(map(int, input().split())), reverse=True)

P = 1000000007

# compute binomial coefficients modulo a prime P
fact = [1] * (n+1)
for i in range(1,n+1):
    fact[i] = (i * fact[i-1]) % P
    # fact.append(factorial(i))

# print(fact)

def binom(n, k):
    denom = (fact[k] * fact[n-k]) % P
    inv = pow(denom, P-2, P)
    return (fact[n] * inv) % P

# print(binom(n, k))
# high = n - k # top m elements
total = 0
for i in range(n - k + 1):
    # count the number of ways where keys[i] is the max element in the set of keys pressed
    # binom(n - i - 1, ... ) cause there are i elements bigger than keys[i] and keys i takes one spot
    # k - 1) cause the one spot has already been taken by keys[i]
    # print("binom", (binom(n - i, k - 1)))
    total += (keys[i] * (binom(n - i - 1, k - 1) % P)) % P

stdout.write(str(total % P))
