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

n, a, b, c = map(int, input().split())

# ways = 0
# hm = dict()

# map of how many ways we can ride either of the 3 rides as the i-th ride in the sequence
tiw = [1] * n; rc = [1] * n; dt = [1] * n

# for the first ride, there is only one way to ride when starting with either type
# for ride(i.e. tiw) as the i-th(3rd) ride, we count the no. of possible sequences with either rc or dt as previous ride 
# ^ mulitply by available types of the ride to get total ways
for r in range(1, n):
    tiw[r] = b * rc[r - 1] + c * dt[r - 1]
    rc[r] = a * tiw[r - 1] + c * dt[r - 1]
    dt[r] = a * tiw[r - 1] + b * rc[r - 1]

# print(tiw)
# print(rc)
# print(dt)

print( ((a * tiw[-1]) + (b * rc[-1]) + (c * dt[-1])) % ((10 ** 9) + 7) )
