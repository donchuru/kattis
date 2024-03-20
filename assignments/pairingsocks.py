"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

n = int(input())
socks = list(map(int, input().split()))

aux = [-1]
count = 0

for s in range(len(socks)):
    if socks[s] == aux[-1]:
        aux.pop()
    else:
        aux.append(socks[s])
    count += 1

if (count % n) > 0 or (len(aux) > 1):
    print("impossible")
else:
    print(count)
