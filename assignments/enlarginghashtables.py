"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

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
from collections import defaultdict

def factors(n):
    n_og = n
    primes = defaultdict(int)
    p = 2
    while (p*p) <= n:
        while n % p == 0:
            primes[p] += 1
            n = n // p
        p += 1
    
    if n > 1:
        primes[n] += 1

    if primes[n_og] == 1:
        return False
    return True


for ip in stdin:
    if ip.strip() == "0":
        break

    n = int(ip)

    flag = False
    if factors(n): # if n has factors (is not a prime number)
        flag = True

    n2 = 2 * n
    while True:
        if not factors(n2): # if n2 is a prime number
            if flag:
                print(n2, "(%d is not prime)" %n)
            else:
                print(n2)
            break

        n2 += 1
