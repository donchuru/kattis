"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  Competitive Programming 4

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

phi_table = [ i for i in range(10000 + 1) ]
def eulerPhi():
    for i in range(2, 10000 + 1):
        if phi_table[i] == i:
            for j in range(i, 10000 + 1, i):
                phi_table[j] -= phi_table[j] // i

p = int(input())
eulerPhi()
for i in range(p):
    k, n = map(int, input().split())
    # print(phi_table)
    total = sum(phi_table[: n + 1])
    print( k, total + 1 )
