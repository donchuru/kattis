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

n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))
reserves = list(map(int, input().split()))

teams = range(1, n + 1)


if teams[0] in damaged:
    if teams[1] in reserves:
        damaged.remove(teams[0])
        reserves.remove(teams[1])

if teams[n-1] in damaged:
    if teams[n-2] in reserves:
        damaged.remove(teams[n-1])
        reserves.remove(teams[n-2])


for i in range(1, len(teams) - 1):
    if teams[i] in damaged:
        if teams[i] in reserves or teams[i -1] in reserves or teams[i + 1] in reserves:
            damaged.remove(teams[i])
            
            # remove from reserves
            if teams[i] in reserves:
                reserves.remove(teams[i])
            elif teams[i - 1] in reserves:
                reserves.remove(teams[i-1])
            elif teams[i + 1] in reserves:
                reserves.remove(teams[i+1])

print(len(damaged))
