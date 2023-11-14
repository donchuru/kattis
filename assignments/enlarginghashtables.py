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

# build our prime table
def prime_table(n):
    global pdiv
    pdiv = list(range(n + 1))
    
    for p in range(2, n + 1):
        if pdiv[p] == p: 
            for q in range(2 * p, n + 1, p):
                pdiv[q] = p

for ip in stdin:
    if ip.strip() == "0":
        break

    n = int(ip)
    prime_table(3 * n)
    
    n2 = n * 2
    while pdiv[n2] != n2:
        n2 += 1

    print(n2)
        
